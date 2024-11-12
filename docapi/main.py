import shutil
from pathlib import Path
from fire import Fire

from docapi import DocAPI


class Main:

    @staticmethod
    def generate(app_path, doc_dir='./docs', lang='zh', config=None):
        docapi = DocAPI.build_flask(lang, config)
        docapi.generate(app_path, doc_dir)

    @staticmethod
    def update(app_path, doc_dir='./docs', lang='zh', config=None):
        docapi = DocAPI.build_flask(lang, config)
        try:
            docapi.update(app_path, doc_dir)
        except FileNotFoundError:
            docapi.generate(app_path, doc_dir)

    @staticmethod
    def init(output='./'):
        raw_path = Path(__file__).parent / 'config.yaml'
        shutil.copy(str(raw_path), output)

    @staticmethod
    def serve(doc_dir='./docs'):
        ...


if __name__ == '__main__':
    Fire(Main)
