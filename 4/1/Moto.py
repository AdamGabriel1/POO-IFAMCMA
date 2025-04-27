class Moto:
    def __init__(self,marca,modelo):
        self.__marca=marca
        self.__modelo=modelo
        self.__farol=None
        self.farois=[]
        self.__qtdRodas=2

    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def farol(self):
        return self.__farol
    
    @farol.setter
    def farol(self,farol):
        self.__farol=farol

    def liga(self):
        print("Ligando moto")

    def desliga(self):
        print("Desligando moto")

    def acelera(self):
        print("Acelerando moto")

    def freia(self):
        print("Freiando moto")

    def instalaFarol(self,farol):
        self.farois.append(farol)