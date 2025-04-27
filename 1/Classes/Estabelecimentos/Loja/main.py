from Loja import Produto, Loja

l1 = Loja("Loja de Maués", "Bairro: A, Rua: A, Número: A", "123456789", "loja@email.com", 6, 18)
l1.info()

produto1 = Produto("Camiseta", 20, 100)
produto2 = Produto("Calça Jeans", 50, 50)
l1.adicionar_produto(produto1)
l1.adicionar_produto(produto2)

l1.esta_aberta()

l1.atualizar_estoque("Camiseta", 80)

l1.listar_produtos()

l1.buscar_produto("Calça Jeans")
