from Pessoa import Pessoa

class Musico(Pessoa):
    def __init__(self,nome: str,cpf: str,AnoNascimento: int,instrumentista: bool,cantor: bool,compositor: bool):
        super().__init__(nome,cpf,AnoNascimento)
        self.__instrumentista=instrumentista
        self.__cantor=cantor
        self.__compositor=compositor

    def setInstrumentista(self,valor: bool):
        self.__instrumentista=valor

    def setCantor(self,valor: bool):
        self.__cantor=valor

    def setCompositor(self,valor: bool):
        self.__compositor=valor

    def getInstrumentista(self):
        return self.__instrumentista

    def getCantor(self):
        return self.__cantor

    def getCompositor(self):
        return self.__compositor