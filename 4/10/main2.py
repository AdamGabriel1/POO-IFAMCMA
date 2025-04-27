from abc import abstractmethod, ABC

class SerVivo(ABC):
    @abstractmethod
    def respirar(self):
        raise NotImplementedError
    
class Macaco(SerVivo):
    def respirar(self):
        print("Respirando como um macaco")

class Humano(SerVivo):
    def respirar(self):
        print("Respirando como um humano")

macaco=Macaco()
macaco.respirar()

humano=Humano()
humano.respirar()