from Ciclista import *
from Corredor import *
from Nadador import *

class TriAtleta(Ciclista, Corredor, Nadador):
    def __init__(self, aposentado, peso):
        Atleta.__init__(self, aposentado, peso)
