import json
from pathlib import Path
from datetime import datetime
import yaml

from docapi.llm import llm_builder
from docapi.prompt import doc_prompt_zh, doc_prompt_en
from docapi.scanner import flask_scanner
from docapi.web import web_builder


DOC_HEAD = '''# {filename}

*PATH: `{path}`*
'''

API_HEAD = '''## API: {url}

*UPDATE TIME: {time}*
'''


class DocAPI:

    @classmethod
    def build_flask(self, lang='zh', config=None):
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
        else:
            raise ValueError(f'Unknown language: {lang}')

        return self(llm, flask_scanner, prompt)

    def __init__(self, llm, scanner, prompt):
        self.llm = llm
        self.scanner = scanner
        self.prompt = prompt

    def generate(self, app_path, doc_dir):
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

                item['doc'] = self.llm(system=self.prompt.system, user=self.prompt.user.format(code=code))

            print()

        self._write_doc(doc_dir, structures)

    def update(self, app_path, doc_dir):
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
                    item['doc'] = self.llm(system=self.prompt.system, user=self.prompt.user.format(code=item['code']))
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
                            item['doc'] = self.llm(system=self.prompt.system, user=self.prompt.user.format(code=item['code']))
                            print(f'- Update document for {url}.')
                    else:
                        item['doc'] = self.llm(system=self.prompt.system, user=self.prompt.user.format(code=item['code']))
                        print(f'- Create document for {url}.')

                    merged_item_list.append(item)

                merged_structures[path] = merged_item_list

            print()

        self._write_doc(doc_dir, merged_structures)

    def serve(self, doc_dir, ip='127.0.0.1', port=8080):
        web_builder.serve(doc_dir, ip, port)

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

                api_head = API_HEAD.format(url=url, time=time)
                doc_str += api_head + '\n' + doc + '\n'

            doc_path = doc_dir / f'{path.stem}.md'
            doc_path.write_text(doc_str, encoding='utf-8')

        doc_json_path = doc_dir / 'doc.json'
        doc_json_path.write_text(json.dumps(structures, indent=2, ensure_ascii=False), encoding='utf-8')
