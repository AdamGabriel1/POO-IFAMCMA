from abc import ABC,abstractmethod

class InfoCliente(ABC):
    @abstractmethod
    def info(self):
        raise NotImplementedError