from abc import abstractmethod


class BaseScanner:

    @abstractmethod
    def scan(self, app_path):
        raise NotImplementedError
