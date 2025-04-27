class Farol:
    def __init__(self,tipo,potencia):
        self.__tipo=tipo
        self.__potencia=potencia

    @property
    def tipo(self):
        return self.__tipo#getters
    
    @property
    def potencia(self):
        return self.__potencia#getters
    
    def acender(self):
        print("Acendendo farol...")

    def apagar(self):
        print("Apagando farol")