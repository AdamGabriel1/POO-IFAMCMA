from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    def __init__(self, posX:int, posY: int):
        self.posX = posX
        self.posY = posY
        
    @abstractmethod
    def getArea(self):
        pass
    
    @abstractmethod
    def getPerimetro(self):
        pass
    
    def getPosString(self):
        saida = "posicao (" + str(self.posX) + ", " + str(self.posY) + ")"
        return saida