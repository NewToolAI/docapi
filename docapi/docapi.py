import json
from pathlib import Path
from datetime import datetime
import hashlib
import yaml
import shutil

from docapi.llm import llm_builder
from docapi.prompt import doc_prompt_zh, doc_prompt_en
from docapi.scanner import flask_scanner
from docapi.web import web_builder


DOC_HEAD = '''# {filename}

*Path: `{path}`*
'''


class DocAPI:

    @classmethod
    def build(self, lang=None, config=None):
        if config:
            with open(config, 'r') as f:
                config = yaml.load(f, Loader=yaml.FullLoader)
                llm = llm_builder.build_llm(**config)
        else:
            llm = llm_builder.build_llm()

        if lang == 'zh':
            prompt = doc_prompt_zh
        elif lang == 'en':
            prompt = doc_prompt_en
        elif lang == None:
            prompt = None
        else:
            raise ValueError(f'Unknown language: {lang}')

        return self(llm, flask_scanner, prompt, config)

    def __init__(self, llm, scanner, prompt, config=None):
        self.llm = llm
        self.scanner = scanner
        self.prompt = prompt
        self.config = config

    def init(self, output):
        raw_path = Path(__file__).parent / 'config.yaml'
        output = Path(output) / 'config.yaml'
        shutil.copy(str(raw_path), str(output))
        print(f'Create config file to {str(output)}')

    def generate(self, file_path, doc_dir, auto_scan=False):
        if auto_scan:
            self.auto_generate(file_path, doc_dir)
        elif self.config:
            for path in self.config['api_files']:
                self.file_generate(path, doc_dir)
                print(f'- Create document for {path}')
        else:
            raise Exception('Input is wrong.')

        self._write_index(doc_dir)

    def update(self, file_path, doc_dir, auto_scan=False):
        if auto_scan:
            self.auto_update(file_path, doc_dir)
        elif self.config:
            for path in self.config['api_files']:
                if self.file_update(path, doc_dir):
                    print(f'- Update document for {path}')
        else:
            raise Exception('Input is wrong.')

        self._write_index(doc_dir)

    def serve(self, doc_dir, ip='127.0.0.1', port=8080):
        web_builder.serve(doc_dir, ip, port)

    def file_generate(self, file_path, doc_dir):
        file_path = Path(file_path)
        doc_dir = Path(doc_dir)
        doc_file = (doc_dir / file_path.name).with_suffix('.md')
        doc_json_file = doc_dir / 'doc.json'

        time = datetime.now().strftime('%Y-%m-%d %H:%M')

        code = file_path.read_text(encoding='utf-8')
        doc = self.llm(system=self.prompt.system.format(time=time), 
                       user=self.prompt.user.format(code=code))
        md5 = hashlib.md5(code.encode('utf-8')).hexdigest()
        doc = DOC_HEAD.format(filename=file_path.name, path=str(file_path.resolve())) + '\n' + doc

        item = {
            'path': str(file_path.resolve()),
            'code': code,
            'md5': md5
        }

        if doc_json_file.exists():
            doc_json = json.loads(doc_json_file.read_text(encoding='utf-8'))
            if not isinstance(doc_json, list):
                doc_json = []

            doc_json.append(item)
        else:
            doc_json = [item]
        
        doc_json_file.write_text(json.dumps(doc_json, ensure_ascii=False, indent=2), encoding='utf-8')
        doc_file.write_text(doc, encoding='utf-8')

    def file_update(self, file_path, doc_dir):
        file_path = Path(file_path)
        doc_dir = Path(doc_dir)
        doc_json_file = doc_dir / 'doc.json'

        code = file_path.read_text(encoding='utf-8')
        new_md5 = hashlib.md5(code.encode('utf-8')).hexdigest()
        old_item_list = json.loads(doc_json_file.read_text(encoding='utf-8'))

        for item in old_item_list:
            old_md5 = item['md5']
            old_path = item['path']

            if str(file_path.resolve()) == old_path and new_md5 == old_md5:
                break
        else:
            self.file_generate(str(file_path), str(doc_dir))
            return True

        return False

    def auto_generate(self, app_path, doc_dir):
        doc_dir = Path(doc_dir)
        doc_dir.mkdir(parents=True, exist_ok=True)

        structures = self.scanner.scan(app_path)

        for path, item_list in structures.items():
            path = Path(path).resolve()
            print(f'Create document for {path.name}.')

            for item in item_list:
                url = item['url']
                md5 = item['md5']
                code = item['code']
                print(f'- Create document for {url}.')

                time = datetime.now().strftime('%Y-%m-%d %H:%M')
                item['doc'] = self.llm(system=self.prompt.system.format(time=time), 
                                       user=self.prompt.user.format(code=code))

            print()

        self._write_doc(doc_dir, structures)

    def auto_update(self, app_path, doc_dir):
        doc_dir = Path(doc_dir)
        doc_dir.mkdir(parents=True, exist_ok=True)

        new_structures = self.scanner.scan(app_path)
        old_structures = json.loads((doc_dir / 'doc.json').read_text(encoding='utf-8'))
        merged_structures = {}

        for path, item_list in new_structures.items():
            path = Path(path).resolve()
            print(f'Update document for {path.name}.')
            path = str(path)

            if path not in old_structures:
                for item in item_list:
                    time = datetime.now().strftime('%Y-%m-%d %H:%M')
                    item['doc'] = self.llm(system=self.prompt.system.format(time=time),
                                           user=self.prompt.user.format(code=item['code']))
                    url = item['url']
                    print(f'- Create document for {url}.')

                merged_structures[path] = item_list        
            else:
                new_item_list = item_list
                old_item_list = old_structures[path]
                old_url_list = [i['url'] for i in old_item_list]
                merged_item_list = []

                for item in new_item_list:
                    url = item['url']
                    md5 = item['md5']

                    if url in old_url_list:
                        old_item = old_item_list[old_url_list.index(url)]
                        if old_item['md5'] == md5:
                            item['doc'] = old_item['doc']
                        else:
                            time = datetime.now().strftime('%Y-%m-%d %H:%M')
                            item['doc'] = self.llm(system=self.prompt.system.format(time=time),
                                                   user=self.prompt.user.format(code=item['code']))
                            print(f'- Update document for {url}.')
                    else:
                        time = datetime.now().strftime('%Y-%m-%d %H:%M')
                        item['doc'] = self.llm(system=self.prompt.system.format(time=time),
                                               user=self.prompt.user.format(code=item['code']))
                        print(f'- Create document for {url}.')

                    merged_item_list.append(item)

                merged_structures[path] = merged_item_list

            print()

        self._write_doc(doc_dir, merged_structures)

    def _write_doc(self, doc_dir, structures):
        doc_dir = Path(doc_dir)
        doc_dir.mkdir(parents=True, exist_ok=True)

        time = datetime.now().strftime('%Y-%m-%d %H:%M')

        for path, item_list in structures.items():
            path = Path(path).resolve()

            doc_str = ''
            doc_head = DOC_HEAD.format(filename=path.name, path=str(path))
            doc_str += doc_head + '\n'

            for item in item_list:
                url = item['url']
                md5 = item['md5']
                code = item['code']
                doc = item['doc']

                doc_str += doc + '\n---\n\n'

            doc_path = doc_dir / f'{path.stem}.md'
            doc_path.write_text(doc_str, encoding='utf-8')

        doc_json_path = doc_dir / 'doc.json'
        doc_json_path.write_text(json.dumps(structures, indent=2, ensure_ascii=False), encoding='utf-8')

    def _write_index(self, doc_dir):
        index_path = Path(doc_dir) / 'index.md'
        index_path.write_text(f'''## DocAPI is a Python package that automatically generates API documentation using LLM.

## DocAPI是一个Python包，它使用LLM自动生成API文档。

#### [Github: https://github.com/Shulin-Zhang/docapi](https://github.com/Shulin-Zhang/docapi)                      
''')

