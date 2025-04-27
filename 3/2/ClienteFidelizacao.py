from Cliente import *

class ClienteFidelizacao(Cliente):
    def __init__(self,nome: str,endereco: str,bonus: float,validade: str):
        super().__init__(nome,endereco)
        self.bonus=bonus
        self.validade=validade

    def info(self):
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Bonus: {self.bonus}")
        print(f"Validade: {self.validade}")