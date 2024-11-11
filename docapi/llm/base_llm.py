from abc import abstractmethod


class BaseLLM:

    @abstractmethod
    def __call__(self, system, user):
        raise NotImplementedError
