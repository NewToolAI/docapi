import os

from docapi.llm.openai_llm import OpenAILLM
from docapi.llm.azure_openai_llm import AzureOpenAILLM


def build_llm(**kwargs):
    if kwargs.get('openai_api_key') and kwargs.get('openai_base_url') and kwargs.get('openai_model'):
        api_key = kwargs.get('openai_api_key')
        base_url = kwargs.get('openai_base_url')
        model = kwargs.get('openai_model')
        return OpenAILLM(api_key=api_key, base_url=base_url, model=model)

    elif kwargs.get('openai_api_key'):
        api_key = kwargs.get('openai_api_key')
        return OpenAILLM(api_key=api_key)

    elif os.getenv('OPENAI_API_KEY') and os.getenv('OPENAI_API_BASE'):
        return OpenAILLM()

    elif os.getenv('OPENAI_API_KEY'):
        api_key = os.getenv('OPENAI_API_KEY')
        return OpenAILLM()

    if kwargs.get('azure_api_key') and kwargs.get('azure_endpoint') and kwargs.get('azure_api_version') and kwargs.get('azure_model'):
        api_key = kwargs.get('azure_api_key')
        endpoint = kwargs.get('azure_endpoint')
        api_version = kwargs.get('azure_api_version')
        model = kwargs.get('azure_model')
        return AzureOpenAILLM(api_key=api_key, endpoint=endpoint, api_version=api_version, model=model)

    elif os.getenv('AZURE_OPENAI_API_KEY') and os.getenv('AZURE_OPENAI_ENDPOINT') and os.getenv('OPENAI_API_VERSION'):
        return AzureOpenAILLM()

    else:
        raise ValueError('No LLM provider found')
