class Produto:
    def __init__(self, codigo: int, valor: float, descricao: str):
        self.codigo = codigo
        self.valor = valor
        self.descricao = descricao
        
class Pedido:
    def __init__(self):
        self.itempedido = []

    def add_item(self, item):
        self.itempedido.append(item)

    def obter_total(self):
        self.valor_total = 0
        for item in self.itempedido:
            self.valor_total += item.valor_total()
        return self.valor_total

class ItemPedido(Produto):
    def __init__(self, codigo: int, valor: float, descricao: str, quantidade: int):
        super().__init__(codigo, valor, descricao)
        self.__quantidade = quantidade

    def quantidade(self) -> int:
        return self.__quantidade

    def valor_total(self) -> float:
        return self.valor * self.__quantidade