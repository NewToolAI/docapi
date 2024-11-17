import os
import qianfan
from docapi.llm.base_llm import BaseLLM


class BaiduLLM(BaseLLM):

    def __init__(self, access_key=None, secret_key=None, model='ERNIE-3.5-8K'):
        self._model = model

        if access_key and secret_key:
            os.environ['QIANFAN_ACCESS_KEY'] = access_key
            os.environ['QIANFAN_SECRET_KEY'] = secret_key

        self.chat_comp = qianfan.ChatCompletion()
        print(f'Using model: {self._model}\n')

    def __call__(self, system, user):
        response = self.chat_comp.do(
            model=self._model,
            temperature=1e-6,
            max_output_tokens=2048,
            messages=[
                {"role": "user", "content": system + '\n\n' + user},
            ]
        )
        return response['body']['result']
