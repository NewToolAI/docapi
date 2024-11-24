from docapi.scanner.base_scanner import BaseScanner


class DjangoScanner(BaseScanner):

    def scan(self, app_path):
        raise NotImplementedError
