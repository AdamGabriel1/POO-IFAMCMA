from abc import ABC, abstractmethod

class OperacaoMatematica(ABC):
    @abstractmethod
    def calcula(self,a: int, b: int):
        raise NotImplementedError