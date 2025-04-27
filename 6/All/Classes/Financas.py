class ContaCorrente:
    def __init__(self, numero):
        self.numero=numero
        self.saldo=0.0

    def creditar(self, valor):
        self.saldo=self.saldo+valor

    def debitar(self, valor):
        self.saldo=self.saldo-valor

class Poupanca(ContaCorrente):
    def __init__(self, numero, taxa):
        ContaCorrente.__init__(self, numero)
        self.taxa=taxa

    def renderJuros(self):
        self.saldo=self.saldo+self.taxa*(self.saldo/100)

class ContaImposto(ContaCorrente):
    def __init__(self, numero, percentualImposto):
        ContaCorrente.__init__(self, numero)
        self.percentualImposto=percentualImposto

    def calculaImposto(self):
        self.saldo=self.saldo-(self.saldo*self.percentualImposto)
