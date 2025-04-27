"""
class Classe_Abstrata:
    def faca_algum_coisa(self):
        pass
    
class B(Classe_Abstrata):
    pass

x=Classe_Abstrata()
"""
"""
from abc import ABC, abstractmethod

class Exemplo_Classe_abstrata(ABC):
    def __init__(self, value):
        self.value=value
        super().__init__()

    @abstractmethod
    def faca_alguma_coisa(self):
        pass

class Adicione35(Exemplo_Classe_abstrata):
    def faca_alguma_coisa(self):
        return self.value+35
    
class Multiplique35(Exemplo_Classe_abstrata):
    def faca_alguma_coisa(self):
        return self.value*35

x=Adicione35(10)
y=Multiplique35(10)
print(x.faca_alguma_coisa())
print(y.faca_alguma_coisa())
"""
from abc import ABC, abstractmethod

class Exemplo_Classe_abstrata(ABC):
    @abstractmethod
    def faca_alguma_coisa(self):
        print("Alguma implementação")

class Outra_subclasse(Exemplo_Classe_abstrata):
    def faca_alguma_coisa(self):
        super().faca_alguma_coisa()
        print("Algo a mais da outra subclasse")

x=Outra_subclasse()
x.faca_alguma_coisa()