from Pedido import Pedido
from ItemPedido import ItemPedido

pedido1 = Pedido()

itempedido1 = ItemPedido(codigo=1, valor=100, descricao="Produto 1", quantidade=2)
itempedido2 = ItemPedido(codigo=2, valor=200, descricao="Produto 2", quantidade=1)

pedido1.add_item(itempedido1)
pedido1.add_item(itempedido2)

total = pedido1.obter_total()
print(f"Total do pedido: R${total:.2f}")
