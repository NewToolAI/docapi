import os

from docapi.llm.openai_llm import OpenAILLM
from docapi.llm.azure_openai_llm import AzureOpenAILLM


def build_llm(**kwargs):
    if len(kwargs) > 0:
        api_key = kwargs.get('openai_api_key')
        base_url = kwargs.get('openai_base_url')
        model = kwargs.get('openai_model', 'gpt-4o-mini')
        return OpenAILLM(api_key=api_key, base_url=base_url, model=model)

    elif os.getenv('OPENAI_API_KEY') or os.getenv('OPENAI_API_BASE') or os.getenv('OPENAI_API_MODEL'):
        api_key = os.getenv('OPENAI_API_KEY')
        base_url = os.getenv('OPENAI_API_BASE')
        model = os.getenv('OPENAI_API_MODEL', 'gpt-4o-mini')
        return OpenAILLM(api_key=api_key, base_url=base_url, model=model)

    elif len(kwargs) > 0:
        api_key = kwargs.get('azure_api_key')
        endpoint = kwargs.get('azure_endpoint')
        api_version = kwargs.get('azure_api_version')
        model = kwargs.get('azure_model', 'gpt-4o-mini')
        return AzureOpenAILLM(api_key=api_key, endpoint=endpoint, api_version=api_version, model=model)

    elif os.getenv('AZURE_OPENAI_API_KEY') or os.getenv('AZURE_OPENAI_ENDPOINT') or os.getenv('OPENAI_API_VERSION'):
        api_key = os.getenv('AZURE_OPENAI_API_KEY')
        endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
        api_version = os.getenv('OPENAI_API_VERSION')
        model = os.getenv('AZURE_OPENAI_MODEL', 'gpt-4o-mini')
        return AzureOpenAILLM(api_key=api_key, endpoint=endpoint, api_version=api_version, model=model)

    else:
        raise ValueError('No LLM provider found')
