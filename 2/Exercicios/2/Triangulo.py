from Forma import *

class Triangulo(Forma):
    def __init__(self, area, perimetro):
        Forma.__init__(self, area, perimetro)

    def calculaArea(self, base, altura):
        self.area=(base*altura)/2
        return self.area

    def calculaPerimetro(self, a, b, c):
        self.perimetro=a+b+c
        return self.perimetro
