from Atleta import *

class Corredor(Atleta):
    def __init__(self, aposentado, peso):
        Atleta.__init__(self, aposentado, peso)

    def correr(self):
        print(f"{__name__} está correndo")
