# Exercício 1
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

# Exercício 2
class Forma:
    def __init__(self, area, perimetro):
        self.area=area
        self.primetro=perimetro

class Retangulo(Forma):
    def __init__(self, area, perimetro):
        Forma.__init__(self, area, perimetro)

    def calculaArea(self, base, altura):
        self.area=base*altura
        return self.area

    def calculaPerimetro(self, base, altura):
        self.perimetro=2*(base*altura)
        return self.perimetro

class Triangulo(Forma):
    def __init__(self, area, perimetro):
        Forma.__init__(self, area, perimetro)

    def calculaArea(self, base, altura):
        self.area=(base*altura)/2
        return self.area

    def calculaPerimetro(self, a, b, c):
        self.perimetro=a+b+c
        return self.perimetro

# Exercício 3
class Atleta:
    def __init__(self, aposentado, peso):
        self.aposentado=aposentado
        self.peso=peso

    def aposentar(self):
        self.aposentado=True

    def aquecer(self):
        print(f"{__name__} está aquecendo")

class Ciclista(Atleta):
    def __init__(self, aposentado, peso):
        Atleta.__init__(self, aposentado, peso)

    def pedalar(self):
        print(f"{__name__} está pedalando")

class Corredor(Atleta):
    def __init__(self, aposentado, peso):
        Atleta.__init__(self, aposentado, peso)

    def correr(self):
        print(f"{__name__} está correndo")

class Nadador(Atleta):
    def __init__(self, aposentado, peso):
        Atleta.__init__(self, aposentado, peso)

    def nadar(self):
        print(f"{__name__} está nadando")

class TriAtleta(Ciclista, Corredor, Nadador):
    def __init__(self, aposentado, peso):
        Atleta.__init__(self, aposentado, peso)

# Exercício 4
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
