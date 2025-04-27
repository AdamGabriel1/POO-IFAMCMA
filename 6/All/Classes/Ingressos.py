class Ingresso:
    def __init__(self, valor):
        self.valor=valor

    def imprimeValor(self):
        print(self.valor)

class VIP(Ingresso):
    def __init__(self, valor, valor_add):
        Ingresso.__init__(self, valor)
        self.valor_add=valor_add

    def imprimeValor(self):
        print(self.valor+self.valor_add)