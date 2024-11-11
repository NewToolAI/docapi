from openai import OpenAI

from llm.base_llm import BaseLLM


class OpenAILLM(BaseLLM):
    def __init__(self, api_key, base_url=None):
        if base_url:
            self.client = OpenAI(base_url=base_url, api_key=api_key)
        else:
            self.client = OpenAI(api_key=api_key)

    def __call__(self, model, system, input):
        response = self.client.chat.completions.create(
            model=model,
            temperature=0,
            max_tokens=4096,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": input},
            ]
        )
        return response.choices[0].message.content
