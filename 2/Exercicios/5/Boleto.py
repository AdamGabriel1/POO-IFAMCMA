from Pagamento import *

class Boleto(Pagamento):
    def info(self):
        print(f"Nome do Pagador: {self.nome}")
        print(f"Forma de Pagamento: {self.fpagamento}")
        print(f"Valor do Pagamento: {self.valor}")
        if self.eparcelado==True:
            print("O Produto é parcelado.")
            print(f"Quantidade de Parcelas: {self.qparcelas}")
            print(f"Valor das Parcelas: {self.vparcelas}")
        else:
            print("O produto não é parcelado.")
