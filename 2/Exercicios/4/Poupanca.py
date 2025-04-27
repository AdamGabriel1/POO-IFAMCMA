from ContaCorrente import *

class Poupanca(ContaCorrente):
    def __init__(self, numero, taxa):
        super().__init__(numero)
        self.taxa=taxa

    def renderJuros(self):
        self.saldo=self.saldo+self.taxa*(self.saldo/100)
