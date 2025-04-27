from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self,nome,fpagamento,valor,eparcelado,qparcelas=None,vparcelas=None):
        self.nome=nome
        self.fpagamento=fpagamento
        self.valor=valor
        self.eparcelado=eparcelado

        if eparcelado==True:
            self.qparcelas=qparcelas
            self.vparcelas=vparcelas
        else:
            self.qparcelas=1
            self.vparcelas=valor

    @abstractmethod
    def info(self):
        pass
