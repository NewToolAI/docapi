import os

from llm.openai_llm import OpenAILLM


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
        api_key = os.getenv('OPENAI_API_KEY')
        base_url = os.getenv('OPENAI_API_BASE')
        return OpenAILLM(api_key=api_key, base_url=base_url)

    elif os.getenv('OPENAI_API_KEY'):
        api_key = os.getenv('OPENAI_API_KEY')
        return OpenAILLM(api_key=api_key)

    else:
        raise ValueError('No LLM provider found')
