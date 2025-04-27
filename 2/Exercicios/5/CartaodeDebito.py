from Pagamento import *

class CartaodeDebito(Pagamento):
    def __init__(self,nome,bandeira,fpagamento,valor,eparcelado,qparcelas=None,vparcelas=None):
        super().__init__(nome,fpagamento,valor,eparcelado,qparcelas,vparcelas)
        self.bandeira=bandeira

    def info(self):
        print(f"Nome do Pagador: {self.nome}")
        print(f"Bandeira do Cartão: {self.bandeira}")
        print(f"Forma de Pagamento: {self.fpagamento}")
        print(f"Valor do Pagamento: {self.valor}")
        if self.eparcelado==True:
            print("O Produto é parcelado.")
            print(f"Quantidade de Parcelas: {self.qparcelas}")
            print(f"Valor das Parcelas: {self.vparcelas}")
        else:
            print("O produto não é parcelado.")