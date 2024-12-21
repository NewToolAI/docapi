import re


def build_scanner(app_path, static=False):
    with open(app_path) as f:
        code = f.read()

    import_code = ''
    for line in code.split('\n'):
        line = line.strip()
        if re.match(r'from .{1,100} import .*|import .*', line):
            import_code += line + '\n'

    flask_import_count = import_code.count('flask')
    django_import_count = import_code.count('django')

    if flask_import_count == 0 and django_import_count == 0:
        raise ValueError('This is not a Flask or Django project.')
    elif flask_import_count > django_import_count: 
        if static:
            from docapi.scanner.flask_static_scanner import FlaskStaticScanner
            return FlaskStaticScanner()
        else:
            from docapi.scanner.flask_scanner import FlaskScanner
            return FlaskScanner()
    else:
        if static:
            raise NotImplementedError('Django static scanner is not implemented yet.')
        else:
            from docapi.scanner.django_scanner import DjangoScanner 
            return DjangoScanner()
