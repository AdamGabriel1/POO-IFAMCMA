class Carro:
    def __init__(self,ano: int,modelo: str,placa: str,cor: str):
        self.ano=ano
        self.modelo=modelo
        self.placa=placa
        self.cor=cor

    def acelerar(self):
        print("O carro está acelerando a 2000 km/h")

    def frear(self):
        print("O carro está à 50 km/h")

    def businar(self):
        print("Barulho de busina")