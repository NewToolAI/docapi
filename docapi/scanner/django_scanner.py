import os
import sys
import re
from pathlib import Path
import hashlib
import inspect


from docapi.scanner.base_scanner import BaseScanner


class DjangoScanner(BaseScanner):
    
    def scan(self, manager_path):
        import django
        from django.urls import get_resolver
        
        project_path = Path(manager_path).parent.resolve()

        sys.path.insert(0, str(project_path))
        os.environ['DJANGO_SETTINGS_MODULE'] = self._get_settings(manager_path)
        django.setup()
        sys.path.pop(0)

        resolver = get_resolver()
        structures = {}
        self._extract_routes(resolver.url_patterns, structures, prefix='/')
        structures = self._sort_structures(structures)

        return structures

    def _get_settings(self, manager_path):
        manager_path = Path(manager_path)

        for line in manager_path.read_text(encoding='utf-8').splitlines():
            if re.match(r'^os\.environ.*DJANGO_SETTINGS_MODULE', line.strip()):
                settings = line.split('DJANGO_SETTINGS_MODULE')[-1].strip(",')\"\t\n ")
                return settings

        raise RuntimeError('Cannot find DJANGO_SETTINGS_MODULE')

    def _extract_routes(self, patterns, structures, prefix):
        from django.urls import URLPattern, URLResolver

        for pattern in patterns:
            if isinstance(pattern, URLPattern):
                url = prefix + str(pattern.pattern)

                if url.startswith('/admin'):
                    continue

                view_func = pattern.callback

                try:
                    comments = inspect.getcomments(view_func) or ''
                except (TypeError, OSError):
                    comments = ''

                try:
                    code = inspect.getsource(view_func)
                except (TypeError, OSError):
                    code = ''

                code = f'# API Path: {url.rstrip("/")}\n\n' + comments + code

                md5 = hashlib.md5(code.encode()).hexdigest()
                path = str(Path(inspect.getfile(view_func)).resolve())

                if path not in structures:
                    structures[path] = []

                structures[path].append({
                    'url': url.rstrip('/'),
                    'md5': md5,
                    'code': code
                 })
            elif isinstance(pattern, URLResolver):
                new_prefix = prefix + str(pattern.pattern)
                self._extract_routes(pattern.url_patterns, structures, prefix=new_prefix)
            else:
                pass

    def _sort_structures(self, structures):
        new_structures = {}
        for path, item_list in structures.items():
            new_structures[path] = sorted(item_list, key=lambda x: x['url'])

        return new_structures
