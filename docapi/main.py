from fire import Fire

from docapi import DocAPI


class Main:

    def __init__(self):
        self.docapi = DocAPI.build_flask()

    def generate(self, app_path, doc_dir='./docs'):
        self.docapi.generate(app_path, doc_dir)
    
    def update(self, app_path, doc_dir='./docs'):
        self.docapi.update(app_path, doc_dir)

    def init_config(self):
        ...

    def serve(self, doc_dir='./docs'):
        ...


if __name__ == '__main__':
    Fire(Main)
