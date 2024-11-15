from openai import OpenAI

from docapi.llm.base_llm import BaseLLM


class OpenAILLM(BaseLLM):

    def __init__(self, api_key=None, base_url=None, model='gpt-4o-mini'):
        self._model = model

        kwargs = {}
        if api_key:
            kwargs['api_key'] = api_key
        if base_url:
            kwargs['base_url'] = base_url

        self.client = OpenAI(**kwargs)
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
