class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

class Loja:
    def __init__(self, nome, endereco, telefone, email, horario_abertura, horario_fechamento):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.horario_abertura = horario_abertura
        self.horario_fechamento = horario_fechamento
        self.produtos = []

    def esta_aberta(self):
        hora_atual = 10
        if self.horario_abertura <= hora_atual < self.horario_fechamento:
            print(f"A loja {self.nome} está aberta agora.")
        else:
            print(f"A loja {self.nome} está fechada agora.")

    def info(self):
        print(f"\nInformações da Loja:\nNome: {self.nome}\nEndereço: {self.endereco}\nTelefone: {self.telefone}\nEmail: {self.email}")

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto '{produto.nome}' adicionado à loja.")

    def remover_produto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                self.produtos.remove(produto)
                print(f"Produto '{nome_produto}' removido da loja.")
                return
        print(f"Produto '{nome_produto}' não encontrado na loja.")

    def verificar_estoque(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                print(f"Estoque de '{nome_produto}': {produto.estoque}")
                return
        print(f"Produto '{nome_produto}' não encontrado na loja.")

    def atualizar_estoque(self, nome_produto, novo_estoque):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                produto.estoque = novo_estoque
                print(f"Estoque de '{nome_produto}' atualizado para {novo_estoque}.")
                return
        print(f"Produto '{nome_produto}' não encontrado na loja.")

    def listar_produtos(self):
        print("Produtos disponíveis na loja:")
        for produto in self.produtos:
            print(f"Nome: {produto.nome}, Preço: {produto.preco}, Estoque: {produto.estoque}")

    def buscar_produto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                print(f"Informações de '{nome_produto}': Preço: {produto.preco}, Estoque: {produto.estoque}")
                return
        print(f"Produto '{nome_produto}' não encontrado na loja.")
