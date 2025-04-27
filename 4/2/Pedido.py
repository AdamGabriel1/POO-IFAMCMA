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
