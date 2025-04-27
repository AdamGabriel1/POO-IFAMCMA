from abc import ABC, abstractmethod

class Entidade(ABC):
    def __init__(self, nome: str, endereco: str, telefone: str = None, email: str = None):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    @abstractmethod
    def info(self):
        pass

class Pessoa(Entidade):
    def __init__(self, nome: str, cpf: str, ano_nascimento: int, endereco: str, telefone: str = None, email: str = None):
        super().__init__(nome, endereco, telefone, email)
        self.__cpf = cpf
        self.__ano_nascimento = ano_nascimento

    def setNome(self, valor: str):
        self.nome = valor

    def setCPF(self, valor: str):
        self.__cpf = valor

    def setAnoNascimento(self, valor: int):
        self.__ano_nascimento = valor

    @property
    def getNome(self):
        return self.nome
    
    @property
    def getCPF(self):
        return self.__cpf
    
    @property
    def getAnoNascimento(self):
        return self.__ano_nascimento

    def info(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.__cpf}")
        print(f"Ano de Nascimento: {self.__ano_nascimento}")
        print(f"Endereço: {self.endereco}")
        if self.telefone: print(f"Telefone: {self.telefone}")
        if self.email: print(f"Email: {self.email}")

class Engenheiro(Pessoa):
    def __init__(self, nome: str, cpf: str, ano_nascimento: int, endereco: str, numero_crea: str, telefone: str = None, email: str = None):
        super().__init__(nome, cpf, ano_nascimento, endereco, telefone, email)
        self.__numero_crea = numero_crea

    def setNumeroCREA(self, valor: str):
        self.__numero_crea = valor

    @property
    def getNumeroCREA(self):
        return self.__numero_crea

    def info(self):
        super().info()
        print(f"CREA: {self.__numero_crea}")

class Musico(Pessoa):
    def __init__(self, nome: str, cpf: str, ano_nascimento: int, endereco: str, instrumentista: bool, cantor: bool, compositor: bool, telefone: str = None, email: str = None):
        super().__init__(nome, cpf, ano_nascimento, endereco, telefone, email)
        self.__instrumentista = instrumentista
        self.__cantor = cantor
        self.__compositor = compositor

    def setInstrumentista(self, valor: bool):
        self.__instrumentista = valor

    def setCantor(self, valor: bool):
        self.__cantor = valor

    def setCompositor(self, valor: bool):
        self.__compositor = valor

    def getInstrumentista(self):
        return self.__instrumentista

    def getCantor(self):
        return self.__cantor

    def getCompositor(self):
        return self.__compositor

    def info(self):
        super().info()
        print(f"Instrumentista: {'Sim' if self.__instrumentista else 'Não'}")
        print(f"Cantor: {'Sim' if self.__cantor else 'Não'}")
        print(f"Compositor: {'Sim' if self.__compositor else 'Não'}")

class Baterista(Musico):
    def __init__(self, nome: str, cpf: str, ano_nascimento: int, endereco: str, telefone: str = None, email: str = None):
        super().__init__(nome, cpf, ano_nascimento, endereco, True, False, False, telefone, email)
        self.saxofonistas = []
    
    def add_saxofonista(self, saxofonista):
        self.saxofonistas.append(saxofonista)
    
    def toca_com(self):
        for sax in self.saxofonistas:
            print(f"{sax.getNome} toca com Baterista")

class Saxofonista(Musico):
    def __init__(self, nome: str, cpf: str, ano_nascimento: int, endereco: str, telefone: str = None, email: str = None):
        super().__init__(nome, cpf, ano_nascimento, endereco, True, False, False, telefone, email)
    
    def toca_com(self, outro_musico):
        print(f"{outro_musico.getNome} toca com Saxofonista")

class Orquestra(Entidade):
    def __init__(self, nome: str, endereco: str):
        super().__init__(nome, endereco)
        self.musicos = []
    
    def add_musico(self, musico):
        self.musicos.append(musico)
    
    def info(self):
        print(f"Orquestra: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print("Músicos:")
        for m in self.musicos:
            print(f"- {m.getNome}")

class Atleta(Pessoa):
    def __init__(self, nome: str, cpf: str, ano_nascimento: int, endereco: str, aposentado: bool, peso: float, telefone: str = None, email: str = None):
        super().__init__(nome, cpf, ano_nascimento, endereco, telefone, email)
        self.aposentado = aposentado
        self.peso = peso

    def aposentar(self):
        self.aposentado = True

    def aquecer(self):
        print(f"{self.getNome} está aquecendo")

class Ciclista(Atleta):
    def __init__(self, nome: str, cpf: str, ano_nascimento: int, endereco: str, aposentado: bool, peso: float, telefone: str = None, email: str = None):
        super().__init__(nome, cpf, ano_nascimento, endereco, aposentado, peso, telefone, email)

    def pedalar(self):
        print(f"{self.getNome} está pedalando")

class Corredor(Atleta):
    def __init__(self, nome: str, cpf: str, ano_nascimento: int, endereco: str, aposentado: bool, peso: float, telefone: str = None, email: str = None):
        super().__init__(nome, cpf, ano_nascimento, endereco, aposentado, peso, telefone, email)

    def correr(self):
        print(f"{self.getNome} está correndo")

class Nadador(Atleta):
    def __init__(self, nome: str, cpf: str, ano_nascimento: int, endereco: str, aposentado: bool, peso: float, telefone: str = None, email: str = None):
        super().__init__(nome, cpf, ano_nascimento, endereco, aposentado, peso, telefone, email)

    def nadar(self):
        print(f"{self.getNome} está nadando")

class TriAtleta(Ciclista, Corredor, Nadador):
    def __init__(self, nome: str, cpf: str, ano_nascimento: int, endereco: str, aposentado: bool, peso: float, telefone: str = None, email: str = None):
        super().__init__(nome=nome, cpf=cpf, ano_nascimento=ano_nascimento, endereco=endereco, aposentado=aposentado, peso=peso, telefone=telefone, email=email)

class InfoCliente(ABC):
    @abstractmethod
    def info(self):
        raise NotImplementedError
        
class InfoClientePessoaFisica(InfoCliente):
    def __init__(self,cpf: str):
        self.cpf=cpf

    def info(self):
        print(f"CPF: {self.cpf}")
        
class InfoClientePessoaJuridica(InfoCliente):
    def __init__(self,cnpj: str):
        self.cnpj=cnpj

    def info(self):
        print(f"CNPJ: {self.cnpj}")

class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, ano_nascimento: int, endereco: str, data_nasc: str, telefone: str = None, email: str = None):
        super().__init__(nome, cpf, ano_nascimento, endereco, telefone, email)
        self.data_nasc = data_nasc

    def mudar_endereco(self, novo_endereco: str):
        self.endereco = novo_endereco

    def fazer_emprestimo(self, valor: float):
        print(f"Empréstimo de R${valor} para {self.nome}")

    def info(self):
        super().info()
        print(f"Data de Nascimento: {self.data_nasc}")

class ClienteFidelizacao(Cliente):
    def __init__(self, nome: str, cpf: str, ano_nascimento: int, endereco: str, data_nasc: str, bonus: float, validade: str, telefone: str = None, email: str = None):
        super().__init__(nome, cpf, ano_nascimento, endereco, data_nasc, telefone, email)
        self.bonus = bonus
        self.validade = validade

    def info(self):
        super().info()
        print(f"Bônus: {self.bonus}")
        print(f"Validade: {self.validade}")

class Barraquinha(Entidade):
    def __init__(self, nome: str, endereco: str, telefone: str, email: str, longitude: float, latitude: float, cardapio: list, funcionamento: str, delivery: bool, taxa_delivery: float):
        super().__init__(nome, endereco, telefone, email)
        self.longitude = longitude
        self.latitude = latitude
        self.cardapio = cardapio
        self.funcionamento = funcionamento
        self.delivery = delivery
        self.taxa_delivery = taxa_delivery

    def adicionar_item_ao_cardapio(self, item):
        self.cardapio.append(item)
        print(f"Item '{item['nome']}' adicionado ao cardápio.")

    def remover_item_do_cardapio(self, item_nome):
        for item in self.cardapio:
            if item['nome'] == item_nome:
                self.cardapio.remove(item)
                print(f"Item '{item_nome}' removido.")
                return
        print("Item não encontrado.")

    def alterar_preco_item(self, item_nome, novo_preco):
        for item in self.cardapio:
            if item['nome'] == item_nome:
                item['preco'] = novo_preco
                print(f"Preço de '{item_nome}' atualizado para R${novo_preco}.")
                return
        print("Item não encontrado.")

    def info(self):
        super().info()
        print(f"Localização: {self.longitude}, {self.latitude}")
        print(f"Horário: {self.funcionamento}")
        print(f"Delivery: {'Sim' if self.delivery else 'Não'} (Taxa: R${self.taxa_delivery})")
        print("Cardápio:")
        for item in self.cardapio:
            print(f"- {item['nome']}: R${item['preco']}")

class Produto:
    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

class Loja(Entidade):
    def __init__(self, nome: str, endereco: str, horario_abertura: str, horario_fechamento: str, telefone: str = None, email: str = None):
        super().__init__(nome, endereco, telefone, email)
        self.horario_abertura = horario_abertura
        self.horario_fechamento = horario_fechamento
        self.produtos = []

    def esta_aberta(self, hora_atual: int):
        if self.horario_abertura <= hora_atual < self.horario_fechamento:
            print(f"{self.nome} está aberta.")
        else:
            print(f"{self.nome} está fechada.")

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)
        print(f"Produto '{produto.nome}' adicionado.")

    def remover_produto(self, nome_produto: str):
        for p in self.produtos:
            if p.nome == nome_produto:
                self.produtos.remove(p)
                print(f"Produto '{nome_produto}' removido.")
                return
        print("Produto não encontrado.")

    def info(self):
        super().info()
        print(f"Funcionamento: {self.horario_abertura}h às {self.horario_fechamento}h")
        print("Produtos:")
        for p in self.produtos:
            print(f"- {p.nome}: R${p.preco} (Estoque: {p.estoque})")

# Exemplo de uso:
cliente_pf = Cliente("João", "Rua A", InfoClientePessoaFisica("123.456.789-00", "01/01/1990"))
cliente_pj = Cliente("Empresa X", "Av. B", InfoClientePessoaJuridica("12.345.678/0001-99"))

# Criar um músico e adicionar à orquestra
baterista = Baterista("João", "123.456.789-00", 1990, "Rua A")
saxofonista = Saxofonista("Maria", "987.654.321-00", 1985, "Av. B")
orquestra = Orquestra("Filarmônica", "Teatro Municipal")
orquestra.add_musico(baterista)
orquestra.add_musico(saxofonista)
orquestra.info()

# Criar um cliente fidelizado
cliente = ClienteFidelizacao(
    "Carlos", "111.222.333-44", 1980, "Rua X",
    "15/05/1980", 150.0, "31/12/2024"
)
cliente.fazer_emprestimo(5000)
cliente.info()
