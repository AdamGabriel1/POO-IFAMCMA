class Rua:
    def __init__(self, nome: str):
        self.nome=nome

class Numero:
    def __init__(self, numero: int):
        self.numero=numero

class Bairro:
    def __init__(self, nome: str):
        self.nome=nome

class Cidade:
    def __init__(self, nome: str):
        self.nome=nome

class Estado:
    def __init__(self, nome: str):
        self.nome=nome

class País:
    def __init__(self, nome: str):
        self.nome=nome

class CEP:
    def __init__(self, numero: int):
        self.numero=numero

class Endereco(Bairro, Rua, Numero, Cidade, Estado, País, CEP):
    def __init__(self, bairro: Bairro, rua: Rua, numero: Numero, cidade: Cidade, estado: Estado, país: País, cep: CEP):
        self.bairro=bairro.nome
        self.rua=rua.nome
        self.numero=numero.numero
        self.cidade=cidade.nome
        self.estado=estado.nome
        self.país=país.nome
        self.cep=cep.numero

    def info(self):
        print(f"""Bairro: {self.bairro}
Rua: \t{self.rua}
Número: {self.numero}
Cidade: {self.cidade}
Estado: {self.estado}
País: \t{self.país}
CEP: \t{self.cep}""")

endereco1=Endereco(Bairro("Bairro"),Rua("Sla"),Numero(123),Cidade("Cidade"),Estado("Estado"),País("País"),CEP(12345000))
endereco1.info()