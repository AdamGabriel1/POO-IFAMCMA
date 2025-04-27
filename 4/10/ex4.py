from ex2 import *

class Retangulo(FormaGeometrica):
    def __init__(self, posX:int, posY: int, largura: float, altura: float):
        super().__init__(posX, posY)
        self.largura = largura
        self.altura = altura
        
    def getArea(self):
        super().getArea()
        return self.largura * self.altura
    
    def getPerimetro(self):
        super().getPerimetro()
        return 2 * (self.largura + self.altura)
    
    def toString(self):
        print(f"Retangulo na posição {super().getPosString()} com largura de {self.largura}")
        
obj_dois = Retangulo(12, 65, 2.0, 7.0)
print(obj_dois.getArea())
print(obj_dois.getPerimetro())
obj_dois.toString()