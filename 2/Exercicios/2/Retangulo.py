from Forma import *

class Retangulo(Forma):
    def __init__(self, area, perimetro):
        Forma.__init__(self, area, perimetro)

    def calculaArea(self, base, altura):
        self.area=base*altura
        return self.area

    def calculaPerimetro(self, base, altura):
        self.perimetro=2*(base*altura)
        return self.perimetro
