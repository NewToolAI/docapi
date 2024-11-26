import re

from docapi.scanner.flask_scanner import FlaskScanner
from docapi.scanner.django_scanner import DjangoScanner 


def build_scanner(app_path):
    with open(app_path) as f:
        code = f.read()

    import_code = ''
    for line in code.split('\n'):
        if re.match(r'from .{1,20} import .*|import .*', line):
            import_code += line + '\n'

    if import_code.count('flask') > import_code.count('django'):
        return FlaskScanner()
    else:
        return DjangoScanner()
