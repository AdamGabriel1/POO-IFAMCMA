from abc import abstractmethod, ABC

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade
    
    def apresentar(self):
        raise NotImplementedError
    
class Professor(Pessoa):
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e sou um professor.")
        
class Aluno(Pessoa):
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e sou um aluno.")
        
professor=Professor("Yuri", 15)
aluno=Aluno("Adam", 15)

professor.apresentar()
aluno.apresentar()
