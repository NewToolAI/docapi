from fire import Fire

from docapi import DocAPI


class Main:

    def __init__(self):
        self.docapi = DocAPI.build_flask_doc()

    def generate(self, app_path, doc_dir='./docs'):
        self.docapi(app_path, doc_dir)
    
    def update(self, app_path, doc_dir='./docs'):
        ...

    def serve(self, doc_dir='./docs'):
        ...


if __name__ == '__main__':
    Fire(Main)
