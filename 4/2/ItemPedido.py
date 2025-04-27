from Produto import Produto

class ItemPedido(Produto):
    def __init__(self, codigo: int, valor: float, descricao: str, quantidade: int):
        super().__init__(codigo, valor, descricao)
        self.__quantidade = quantidade

    def quantidade(self) -> int:
        return self.__quantidade

    def valor_total(self) -> float:
        return self.valor * self.__quantidade
