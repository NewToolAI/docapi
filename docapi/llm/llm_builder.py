import os


def build_llm():

    if os.getenv('OPENAI_API_KEY') or os.getenv('OPENAI_API_BASE'):
        from docapi.llm.openai_llm import OpenAILLM

        api_key = os.getenv('OPENAI_API_KEY', 'default')
        base_url = os.getenv('OPENAI_API_BASE')
        model = os.getenv('OPENAI_API_MODEL', 'gpt-4o-mini')
        return OpenAILLM(api_key=api_key, base_url=base_url, model=model)

    elif os.getenv('AZURE_OPENAI_API_KEY') and os.getenv('AZURE_OPENAI_ENDPOINT') and os.getenv('OPENAI_API_VERSION'):
        from docapi.llm.azure_openai_llm import AzureOpenAILLM

        api_key = os.getenv('AZURE_OPENAI_API_KEY', 'default')
        endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
        api_version = os.getenv('OPENAI_API_VERSION')
        model = os.getenv('AZURE_OPENAI_MODEL', 'gpt-4o-mini')
        return AzureOpenAILLM(api_key=api_key, endpoint=endpoint, api_version=api_version, model=model)

    elif os.getenv('QIANFAN_ACCESS_KEY') and os.getenv('QIANFAN_SECRET_KEY'):
        from docapi.llm.baidu_llm import BaiduLLM

        access_key = os.getenv('QIANFAN_ACCESS_KEY')
        secret_key = os.getenv('QIANFAN_SECRET_KEY')
        model = os.getenv('QIANFAN_MODEL', 'ERNIE-3.5-8K')
        return BaiduLLM(access_key=access_key, secret_key=secret_key, model=model)

    elif os.getenv('ZHIPUAI_API_KEY'):
        from docapi.llm.zhipu_llm import ZhipuLLM

        api_key = os.getenv('ZHIPUAI_API_KEY')
        model = os.getenv('ZHIPUAI_MODEL', 'glm-4-flash')
        return ZhipuLLM(api_key=api_key, model=model)

    else:
        raise ValueError('No LLM provider found')
