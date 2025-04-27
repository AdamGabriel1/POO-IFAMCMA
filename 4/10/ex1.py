from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def emitir_som(self):
        pass
class Cachorro(Animal):
    def emitir_som(self):
        print("Au au!")
class Gato(Animal):
    def emitir_som(self):
        print("Miau!")
        
animal1 = Cachorro()
animal1.emitir_som()
animal2 = Gato()
animal2.emitir_som()