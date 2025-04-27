from Atleta import *

class Nadador(Atleta):
    def __init__(self, aposentado, peso):
        Atleta.__init__(self, aposentado, peso)

    def nadar(self):
        print(f"{__name__} está nadando")
