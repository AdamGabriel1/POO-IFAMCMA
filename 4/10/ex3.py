from ex2 import *

class Circulo(FormaGeometrica):
    def __init__(self, posX:int, posY: int, raio: float):
        super().__init__(posX, posY)
        self.raio = raio
        
    def getArea(self):
        super().getArea()
        return math.pi * self.raio**2
    
    def getPerimetro(self):
        super().getPerimetro()
        return 2 * math.pi * self.raio
    
    def toString(self):
        print(f"Círculo na posição {super().getPosString()} com raio de {self.raio}cm")

obj_um = Circulo(10, 10, 5.0)
print(obj_um.getArea())
print(obj_um.getPerimetro())
obj_um.toString()