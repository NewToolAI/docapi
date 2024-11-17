from fire import Fire
from docapi.docapi import DocAPI


class Main:
    '''DocAPI is a Python package that automatically generates API documentation using LLM. '''        

    @staticmethod
    def generate(app_path=None, doc_dir='./docs', lang='zh'):
        '''Generate API documentation.
        Args:
            app_path (str): Path to the API service entry.
            doc_dir (str, optional): Path to the documentation directory. Defaults to './docs'.
            lang (str, optional): Language of the documentation. Defaults to 'zh'.
            config (str, optional): Path to the configuration file. Defaults to None.
        '''
        docapi = DocAPI.build(lang)
        docapi.generate(app_path, doc_dir)

    @staticmethod
    def update(app_path=None, doc_dir='./docs', lang='zh'):
        '''Update API documentation.
        Args:
            app_path (str): Path to the API service entry.
            doc_dir (str, optional): Path to the documentation directory. Defaults to './docs'.
            lang (str, optional): Language of the documentation. Defaults to 'zh'.
            config (str, optional): Path to the configuration file. Defaults to None.
        '''
        docapi = DocAPI.build(lang)
        docapi.update(app_path, doc_dir)

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
        docapi = DocAPI.build()
        docapi.serve(doc_dir, ip, port)


def run():
    return Fire(Main)


if __name__ == '__main__':
    run()
