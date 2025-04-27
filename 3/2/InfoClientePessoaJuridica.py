from Interface.InfoCliente import InfoCliente

class InfoClientePessoaJuridica(InfoCliente):
    def __init__(self,cnpj: str):
        self.cnpj=cnpj

    def info(self):
        print(f"CNPJ: {self.cnpj}")