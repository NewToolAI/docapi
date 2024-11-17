from zhipuai import ZhipuAI
from docapi.llm.base_llm import BaseLLM


class ZhipuLLM(BaseLLM):
    
    def __init__(self, api_key=None, model='glm-4-flash'):
        self._model = model
        self._client = ZhipuAI(api_key=api_key)
        print(f'Using model: {self._model}\n')

    def __call__(self, system, user):
        resp = self._client.chat.completions.create(
            model=self._model,
            temperature=0,
            max_tokens=2048,
            messages=[
                {'role': 'system', 'content': system},
                {'role': 'user', 'content': user},
            ],
        )
        return resp.choices[0].message.content
