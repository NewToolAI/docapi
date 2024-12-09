import os
import sys
from pathlib import Path
from time import time

from fire import Fire
from dotenv import load_dotenv

from docapi.docapi import DocAPI


VERSION = '0.1.4'


class Main:
    '''DocAPI is a Python package that automatically generates API documentation using LLM. '''        


    @staticmethod
    def generate(app_path, doc_dir='docs', model=None, lang='zh', template=None, env='.env', workers=1):
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
        '''
        start = time()

        if Path(env).exists():
            load_dotenv(override=True, dotenv_path=env)

        model = model or os.getenv('DOCAPI_MODEL')
        if model is None:
            raise ValueError('The parameter --model is required, or you must provide the DOCAPI_MODEL environment variable. For example: --model=openai:gpt-4o-mini.')

        docapi = DocAPI.build(model, lang, template, workers)
        docapi.generate(app_path, doc_dir)
        
        end = time()
        time_used = end - start
        print(f'Time used: {time_used:.2f}s.\n')

    @staticmethod
    def update(app_path, doc_dir='docs', model=None, lang='zh', template=None, env='.env', workers=1):
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
        '''
        start = time()

        if Path(env).exists():
            load_dotenv(override=True, dotenv_path=env)

        model = model or os.getenv('DOCAPI_MODEL')
        if model is None:
            raise ValueError('The parameter --model is required, or you must provide the DOCAPI_MODEL environment variable. For example: --model=openai:gpt-4o-mini.')

        docapi = DocAPI.build(model, lang, template, workers)
        docapi.update(app_path, doc_dir)

        end = time()
        time_used = end - start
        print(f'Time used: {time_used:.2f}s.\n')

    @staticmethod
    def serve(doc_dir='./docs', ip='127.0.0.1', port=8080):
        '''Start the document web server.
        Args:
            doc_dir (str, optional): Path to the documentation directory. Defaults to './docs'.
            lang (str, optional): Language of the documentation. Defaults to 'zh'.
            ip (str, optional): IP address of the document web server. Defaults to '127.0.0.1'.
            port (int, optional): Port of the document web server. Defaults to 8080.
            config (str, optional): Path to the configuration file. Defaults to None.
        '''
        docapi = DocAPI.build_empty()
        docapi.serve(doc_dir, ip, port)


def run():
    if sys.argv[1].strip() in ['--version', '-v']:
        print(VERSION)
        sys.exit(0)

    return Fire(Main)


if __name__ == '__main__':
    run()
