from abc import abstractmethod


class BaseLLM:

    @abstractmethod
    def __call__(self, model, system, input):
        raise NotImplementedError
