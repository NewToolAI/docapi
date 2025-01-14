import os
import sys
from pathlib import Path
from time import time

from fire import Fire
from dotenv import load_dotenv

from docapi.docapi import DocAPI


VERSION = '1.1.8'


class Main:
    '''DocAPI is a Python package that automatically generates API documentation using LLM. '''        

    @staticmethod
    def generate(app_path, doc_dir='docs', model=None, lang='zh', template=None, env='.env', workers=1, static=False):
        '''Generate API documentation.
        Args:
            app_path (str, necessary): Path to the API service entry.
            doc_dir (str, optional): Path to the documentation directory. Defaults to './docs'.
            model (str, optional): LLM model. Defaults to None.
            lang (str, optional): Language of the documentation. Defaults to 'zh'.
            config (str, optional): Path to the configuration file. Defaults to None.
            template (str, optional): Path to the template file. Defaults to None.
            env (str, optional): Path to the environment file. Defaults to '.env'.
            workers (int, optional): Number of workers. Defaults to 1.
            static (bool, optional): Scan the routing structure in a static manner. This approach is independent of the project environment. Defaults to False.
        '''
        start = time()

        if Path(env).exists():
            load_dotenv(override=True, dotenv_path=env)

        app_path = Path(app_path)
        if not app_path.is_file():
            raise ValueError(f'Invalid app_path: {app_path}')

        doc_dir = Path(doc_dir)
        if doc_dir.exists():
            user = input(f'The `{doc_dir.name}` directory already exists. Do you want to overwrite it? (y/n): ')
            print()
            if user.lower() != 'y':
                sys.exit(0)
        
        model = model or os.getenv('DOCAPI_MODEL')
        if not model:
            raise ValueError('Missing model parameter. Either pass it as an argument or set the DOCAPI_MODEL environment variable. Example: --model=openai:gpt-4o-mini.')

        docapi = DocAPI.build(model, lang, template, workers, static)
        docapi.generate(app_path, doc_dir)
        
        print(f'Time used: {time() - start:.2f}s.\n')

    @staticmethod
    def update(app_path, doc_dir='docs', model=None, lang='zh', template=None, env='.env', workers=1, static=False):
        '''Update API documentation.
        Args:
            app_path (str, necessary): Path to the API service entry.
            doc_dir (str, optional): Path to the documentation directory. Defaults to './docs'.
            model (str, optional): LLM model. Defaults to None.
            lang (str, optional): Language of the documentation. Defaults to 'zh'.
            config (str, optional): Path to the configuration file. Defaults to None.
            template (str, optional): Path to the template file. Defaults to None.
            env (str, optional): Path to the environment file. Defaults to '.env'.
            workers (int, optional): Number of workers. Defaults to 1.
            static (bool, optional): Scan the routing structure in a static manner. This approach is independent of the project environment. Defaults to False.
        '''
        start = time()

        if Path(env).exists():
            load_dotenv(override=True, dotenv_path=env)

        app_path = Path(app_path)
        if not app_path.is_file():
            raise ValueError(f'Invalid app_path: {app_path}')

        doc_dir = Path(doc_dir)
        if not doc_dir.is_dir():
            raise ValueError(f'Doc directory does not exist: `{doc_dir.name}`')

        user = input(f'Updating the documentation will first remove the API files in `{doc_dir.name}` folder.\nDo you want to continue? (y/n): ')
        print()
        if user.lower() != 'y':
            sys.exit(0)
        
        model = model or os.getenv('DOCAPI_MODEL')
        if not model:
            raise ValueError('Missing model parameter. Either pass it as an argument or set the DOCAPI_MODEL environment variable. Example: --model openai:gpt-4o-mini.')

        docapi = DocAPI.build(model, lang, template, workers, static)
        docapi.update(app_path, doc_dir)

        print(f'Time used: {time() - start:.2f}s.\n')

    @staticmethod
    def serve(doc_dir='./docs', ip='127.0.0.1', port=8080):
        '''Start the document web server.
        Args:
            doc_dir (str, optional): Path to the documentation directory. Defaults to './docs'.
            ip (str, optional): IP address of the document web server. Defaults to '127.0.0.1'.
            port (int, optional): Port of the document web server. Defaults to 8080.
        '''
        doc_dir = Path(doc_dir)
        if not doc_dir.exists():
            raise ValueError(f'Doc directory does not exist: `{doc_dir.name}`')

        docapi = DocAPI.build_empty()
        docapi.serve(doc_dir, ip, port)


def run():
    if len(sys.argv) > 1 and sys.argv[1].strip() in ['--version', '-v']:
        print(VERSION)
        sys.exit(0)

    try:    
        Fire(Main)
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    run()
