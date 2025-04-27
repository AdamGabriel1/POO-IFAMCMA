from Pessoa import Pessoa

class Engenheiro(Pessoa):
    def __init__(self,nome: str,cpf: str,AnoNascimento: int,numeroCREA: str):
        super().__init__(nome,cpf,AnoNascimento)
        self.__numeroCREA=numeroCREA

    def setNumeroCREA(self,valor: str):
        self.__numeroCREA=valor

    @property
    def getNumeroCREA(self):
        return self.__numeroCREA