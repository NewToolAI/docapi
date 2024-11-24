from time import time
from fire import Fire
from docapi.docapi import DocAPI


class Main:
    '''DocAPI is a Python package that automatically generates API documentation using LLM. '''        

    @staticmethod
    def generate(app_path, doc_dir='./docs', lang='zh', template=None, workers=4):
        '''Generate API documentation.
        Args:
            app_path (str, necessary): Path to the API service entry.
            doc_dir (str, optional): Path to the documentation directory. Defaults to './docs'.
            lang (str, optional): Language of the documentation. Defaults to 'zh'.
            config (str, optional): Path to the configuration file. Defaults to None.
            template (str, optional): Path to the template file. Defaults to None.
            workers (int, optional): Number of workers. Defaults to 4.
        '''
        start = time()

        docapi = DocAPI.build(lang, template, workers)
        docapi.generate(app_path, doc_dir)
        
        end = time()
        time_used = end - start
        print(f'Time used: {time_used:.2f}s.\n')

    @staticmethod
    def update(app_path, doc_dir='./docs', lang='zh', template=None, workers=4):
        '''Update API documentation.
        Args:
            app_path (str, necessary): Path to the API service entry.
            doc_dir (str, optional): Path to the documentation directory. Defaults to './docs'.
            lang (str, optional): Language of the documentation. Defaults to 'zh'.
            config (str, optional): Path to the configuration file. Defaults to None.
            template (str, optional): Path to the template file. Defaults to None.
            workers (int, optional): Number of workers. Defaults to 4.
        '''
        start = time()

        docapi = DocAPI.build(lang, template, workers)
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
    return Fire(Main)


if __name__ == '__main__':
    run()
