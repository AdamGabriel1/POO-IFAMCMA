class Pessoa:
    def __init__(self,nome: str,cpf: str,AnoNascimento: int):
        self.__nome=nome
        self.__cpf=cpf
        self.__AnoNascimento=AnoNascimento

    def setNome(self,valor: str):
        self.__nome=valor

    def setCPF(self,valor: str):
        self.__cpf=valor

    def setAnoNascimento(self,valor: int):
        self.__AnoNascimento=valor
    
    @property
    def getNome(self):
        return self.__nome
    
    @property
    def getCPF(self):
        return self.__cpf
    
    @property
    def getAnoNascimento(self):
        return self.__AnoNascimento
