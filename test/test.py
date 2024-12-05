import os
from fire import Fire


MODELS = [
    # 'openai:gpt-4o-mini',
    # 'xai:grok-beta',
    # 'aliyun:qwen-turbo',
    # 'baidu:ERNIE-4.0-Turbo-8K',
    'zhipu:glm-4-flash'
]


def test_flask(env_path, model):
    print('Test Flask.\n')

    result = os.system(f'docapi generate flask_project/server.py flask_project/docs --model {model} --env {env_path}')
    if result != 0:
        exit(1)

    result = os.system(f'docapi update flask_project/server.py flask_project/docs --model {model} ' 
                       f'--lang zh --template ../docapi/template/flask_zh.md --env {env_path}')
    if result != 0:
        exit(1) 
    

def test_code(env_path, model):
    print('Test Code.\n')

    from dotenv import load_dotenv
    from docapi import DocAPI
    
    load_dotenv(dotenv_path=env_path)

    docapi = DocAPI.build(lang="zh", model=model)
    docapi.generate("django_project/manage.py", "django_project/docs", )
    docapi.update("django_project/manage.py", "django_project/docs")


def test(env):
    for model in MODELS:
        test_flask(env, model)

    test_code(env, MODELS[-1])
    
    os.system(f'docapi serve flask_project/docs')


if __name__ == '__main__':
    Fire(test)
