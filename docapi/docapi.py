from pathlib import Path

from llm import llm_builder
from prompt import doc_prompt
from scanner import flask_scanner


DOC_HEAD = '''# {filename}

*path: `{path}`*
'''

API_HEAD = '''## 接口: {url}

*md5: `{md5}`*
'''


class DocAPI:

    @classmethod
    def build_flask_doc(self):
        llm = llm_builder.build_llm()
        return self(llm, flask_scanner, doc_prompt)

    def __init__(self, llm, scanner, prompt):
        self.llm = llm
        self.scanner = scanner
        self.prompt = prompt

    def __call__(self, path, output):
        routes = self.scanner.scan(path)
        output = Path(output)
        output.mkdir(parents=True, exist_ok=True)

        for path, info in routes.items():
            path = Path(path)
            print('filename:', path.name)

            doc_str = ''
            doc_head = DOC_HEAD.format(filename=path.name, path=str(path))
            doc_str += doc_head + '\n'
            for url, md5, code in zip(info['url_list'], info['md5_list'], info['code_list']):
                print('\turl:', url)
                print()

                api_head = API_HEAD.format(url=url, md5=md5)
                doc_str += api_head + '\n'

                api_content = self.llm(model='gpt-4o-mini', system=self.prompt.system, input=self.prompt.user.format(code=code))
                doc_str += api_content + '\n'

            doc_path = output / f'{path.stem}.md'
            doc_path.write_text(doc_str)


if __name__ == '__main__':
    import dotenv
    dotenv.load_dotenv()

    docapi = DocAPI.build_flask_doc()
    docapi('../test/flask_server.py', '../test/docs')
