from Interface.InfoCliente import InfoCliente

class InfoClientePessoaFisica(InfoCliente):
    def __init__(self,cpf: str):
        self.cpf=cpf

    def info(self):
        print(f"CPF: {self.cpf}")