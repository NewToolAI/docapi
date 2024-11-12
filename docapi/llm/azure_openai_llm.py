from openai import AzureOpenAI

from docapi.llm.base_llm import BaseLLM


class AzureOpenAILLM(BaseLLM):

    def __init__(self, api_key=None, endpoint=None, api_version=None, model='gpt-4o-mini'):
        self._model = model

        if api_key and endpoint and api_version:
            self.client = AzureOpenAI(api_key=api_key, azure_endpoint=endpoint, api_version=api_version)
        else:
            self.client = AzureOpenAI()

        print(f'Using model: {self._model}\n')

    def __call__(self, system, user):
        response = self.client.chat.completions.create(
            model=self._model,
            temperature=0,
            max_tokens=2048,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ]
        )
        return response.choices[0].message.content
