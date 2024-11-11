import sys
from pathlib import Path
import hashlib
import inspect
import importlib


def scan(server_path):
    server_path = Path(server_path)
    server_dir = server_path.parent
    sys.path.insert(0, str(server_dir))

    package = server_path.stem
    package = importlib.import_module(package)
    sys.path.pop(0)
    code = inspect.getsource(package)

    for line in code.split('\n'):
        if 'Flask(__name__)' in line:
            app_name = line.split('=')[0].strip()
            break

    app = getattr(package, app_name)
    routes = {}

    for rule in app.url_map.iter_rules():
        view_func = app.view_functions[rule.endpoint]
        path = inspect.getfile(view_func)

        if path.endswith('/site-packages/flask/app.py'):
            continue

        comments = inspect.getcomments(view_func)
        code = inspect.getsource(view_func)

        if comments is not None:
            code = comments + code

        md5 = hashlib.md5(code.encode('utf-8')).hexdigest()

        if path not in routes:
            routes[path] = {
                'url_list': [],
                'md5_list': [],
                'code_list': []
            }

        routes[path]['url_list'].append(rule.rule)
        routes[path]['md5_list'].append(md5)
        routes[path]['code_list'].append(code)
        
    return routes
