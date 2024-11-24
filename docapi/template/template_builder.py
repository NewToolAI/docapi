from pathlib import Path


TEMPLATE_ZH = (Path(__file__).parent / 'flask_zh.md').read_text(encoding='utf-8')

TEMPLATE_EN = (Path(__file__).parent / 'flask_en.md').read_text(encoding='utf-8')


def build_template(lang):
    if lang == 'zh':
        return TEMPLATE_ZH
    else:
        return TEMPLATE_EN
