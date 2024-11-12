import os
from pathlib import Path

import yaml


def build_web_config(doc_dir):
    doc_dir = Path(doc_dir)

    config = {
        'site_name': 'DocAPI',
        'nav': [],
        'theme': 'readthedocs',
        'docs_dir': str(doc_dir.resolve()),
    }

    config['nav'].append({
        'Home': 'index.md'
    })

    for path in doc_dir.glob('*.md'):
        if path.name == 'index.md':
            continue

        config['nav'].append({
            path.stem: path.name
        })

    output = doc_dir /'web.yaml'
    with open(str(output), 'w', encoding='utf-8') as f:
        yaml.dump(config, f)


def serve(doc_dir, ip, port):
    build_web_config(doc_dir)

    config_name = 'web.yaml'
    script = f'cd {Path(doc_dir).resolve()} && mkdocs serve -a {ip}:{port} -f {config_name} --no-directory-urls'
    os.system(script)


if __name__ == '__main__':
    serve('docs', '127.0.0.1', 8000)
