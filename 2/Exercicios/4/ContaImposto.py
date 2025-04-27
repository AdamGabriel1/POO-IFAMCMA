from ContaCorrente import *

class ContaImposto(ContaCorrente):
    def __init__(self, numero, percentualImposto):
        super().__init__(numero)
        self.percentualImposto=percentualImposto

    def calculaImposto(self):
        self.saldo=self.saldo-(self.saldo*self.percentualImposto)