from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self,nome,salario):
        self.nome=nome
        self.salario=salario

    def getNome(self):
        return self.nome

    def setNome(self,nome):
        self.nome=nome

    def getSalario(self):
        return self.salario

    def setSalario(self,salario):
        self.salario=salario    

    def aumentaSalario(self):
        pass

class Gerente(Funcionario):
    def __init__(self,nome,salario):
        super().__init__(nome,salario)

    def aumentaSalario(self):
        self.salario=(self.salario*1.10)

class Programador(Funcionario):
    def __init__(self,nome,salario):
        super().__init__(nome,salario)
        
    def aumentaSalario(self):
        self.salario=(self.salario*1.20)

func1=Gerente("joao",1000.0)
func1.setSalario(2000)
func1.aumentaSalario()
print(func1.getNome())
print(func1.getSalario())

func2=Programador("diego",1500)
func2.setSalario(2500)
func2.aumentaSalario()
print(func2.getNome())
print(func2.getSalario())