import json
from pathlib import Path
from datetime import datetime
import shutil

from docapi.llm import llm_builder
from docapi.prompt import doc_prompt_zh, doc_prompt_en
from docapi.scanner import flask_scanner
from docapi.web import web_builder


DOC_HEAD = '''# {filename}

*Path: `{path}`*
'''

INDEX_STR = '''## DocAPI is a Python package that automatically generates API documentation using LLM.

## DocAPI是一个Python包，它使用LLM自动生成API文档。

#### [Github: https://github.com/Shulin-Zhang/docapi](https://github.com/Shulin-Zhang/docapi)                      
'''


class DocAPI:

    @classmethod
    def build(self, lang=None):
        llm = llm_builder.build_llm()

        if lang == 'zh':
            prompt = doc_prompt_zh
        elif lang == 'en':
            prompt = doc_prompt_en
        elif lang == None:
            prompt = None
        else:
            raise ValueError(f'Unknown language: {lang}')

        return self(llm, flask_scanner, prompt)

    def __init__(self, llm, scanner, prompt):
        self.llm = llm
        self.scanner = scanner
        self.prompt = prompt

    def init(self, output):
        raw_path = Path(__file__).parent / 'config.yaml'
        output = Path(output) / 'config.yaml'
        shutil.copy(str(raw_path), str(output))
        print(f'Create config file to {str(output)}')

    def generate(self, file_path, doc_dir):
        self.auto_generate(file_path, doc_dir)
        self._write_index(doc_dir)

    def update(self, file_path, doc_dir):
        self.auto_update(file_path, doc_dir)
        self._write_index(doc_dir)

    def serve(self, doc_dir, ip='127.0.0.1', port=8080):
        web_builder.serve(doc_dir, ip, port)

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
                print(f' - Create document for {url}.')

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

        new_path_set = set(new_structures.keys())
        old_path_set = set(old_structures.keys())

        add_path_set = new_path_set - old_path_set
        del_path_set = old_path_set - new_path_set
        keep_path_set = new_path_set & old_path_set

        for path in del_path_set:
            print(f'Delete document for {Path(path).name}.')

        add_structures = {path: item_list for path, item_list in new_structures.items() if path in add_path_set}
        keep_structures = {path: item_list for path, item_list in new_structures.items() if path in keep_path_set}

        for path, item_list in add_structures.items():
            path = Path(path).resolve()
            print(f'Add document for {path.name}.')
            path = str(path)

            merged_item_list = []
            for item in item_list:
                url = item['url']
                time = datetime.now().strftime('%Y-%m-%d %H:%M')
                item['doc'] = self.llm(system=self.prompt.system.format(time=time),
                                       user=self.prompt.user.format(code=item['code']))
                merged_item_list.append(item)
                print(f' - Add document for {url}.')

            merged_structures[path] = merged_item_list

        for path, item_list in keep_structures.items():
            path = Path(path).resolve()
            print(f'Update document for {path.name}.')
            path = str(path)

            new_item_list = item_list
            old_item_list = old_structures[path]
            old_url_list = [i['url'] for i in old_item_list]
            old_url_set = {i['url'] for i in old_item_list}
            new_url_set = {i['url'] for i in new_item_list}
            merged_item_list = []

            del_url_set = old_url_set - new_url_set
            add_url_set = new_url_set - old_url_set
            keep_url_set = new_url_set & old_url_set

            add_item_list = [item for item in new_item_list if item['url'] in add_url_set]
            keep_item_list = [item for item in new_item_list if item['url'] in keep_url_set]

            for url in del_url_set:
                print(f' - Delete document for {url}.')

            for item in add_item_list:
                url = item['url']
                time = datetime.now().strftime('%Y-%m-%d %H:%M')
                item['doc'] = self.llm(system=self.prompt.system.format(time=time),
                                       user=self.prompt.user.format(code=item['code']))
                merged_item_list.append(item) 
                print(f' - Add document for {url}.')

            for item in keep_item_list:
                url = item['url']
                md5 = item['md5']

                old_item = old_item_list[old_url_list.index(url)]

                if old_item['md5'] == md5:
                    item['doc'] = old_item['doc']
                    print(f' - Keep document for {url}.')
                else:
                    time = datetime.now().strftime('%Y-%m-%d %H:%M')
                    item['doc'] = self.llm(system=self.prompt.system.format(time=time),
                                           user=self.prompt.user.format(code=item['code']))
                    print(f' - Update document for {url}.')

                merged_item_list.append(item)

            merged_structures[path] = merged_item_list

            print()

        self._write_doc(doc_dir, merged_structures)

    def _write_doc(self, doc_dir, structures):
        doc_dir = Path(doc_dir)
        doc_dir.mkdir(parents=True, exist_ok=True)
        doc_json_path = doc_dir / 'doc.json'
        doc_json_path.unlink(missing_ok=True)

        for doc_file in doc_dir.glob('*.md'):
            doc_file.unlink()

        for path, item_list in structures.items():
            path = Path(path).resolve()

            doc_str = ''
            doc_head = DOC_HEAD.format(filename=path.name, path=str(path))
            doc_str += doc_head + '\n'

            item_list = sorted(item_list, key=lambda x: x['url'])

            for item in item_list:
                doc = item['doc']
                doc_str += doc + '\n---\n\n'

            doc_path = doc_dir / f'{path.stem}.md'
            doc_path.write_text(doc_str, encoding='utf-8')

        doc_json_path.write_text(json.dumps(structures, indent=2, ensure_ascii=False), encoding='utf-8')

    def _write_index(self, doc_dir):
        index_path = Path(doc_dir) / 'index.md'
        index_path.write_text(INDEX_STR, encoding='utf-8')

