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

    for name in dir(package):
        module = getattr(package, name)

        from flask import Flask
        if isinstance(module, Flask):
            app = module
            break

    structures = {}

    for rule in app.url_map.iter_rules():
        view_func = app.view_functions[rule.endpoint]
        path = str(Path(inspect.getfile(view_func)).resolve())

        if path.endswith('/site-packages/flask/app.py'):
            continue

        comments = inspect.getcomments(view_func)
        code = inspect.getsource(view_func)

        if comments is not None:
            code = comments + code

        md5 = hashlib.md5(code.encode('utf-8')).hexdigest()

        if path not in structures:
            structures[path] = []

        structures[path].append({
            'url': rule.rule,
            'md5': md5,
            'code': code
        })

    structures = _sort_structures(structures)
    return structures


def _sort_structures(structures):
    new_structures = {}
    for path, item_list in structures.items():
        new_structures[path] = sorted(item_list, key=lambda x: x['url'])

    return new_structures
