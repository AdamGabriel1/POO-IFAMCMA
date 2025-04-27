class Barraquinha:
    def __init__(self,nome,endereco,telefone,email,longitude,latitude,cardapio,funcionamento,delivery,taxa_delivery):
        self.nome=nome
        self.endereco=endereco
        self.telefone=telefone
        self.email=email
        self.longitude=longitude
        self.latitude=latitude
        self.cardapio=cardapio
        self.funcionamento=funcionamento
        self.delivery=delivery
        self.taxa_delivery=taxa_delivery
    
    def adicionar_item_ao_cardapio():
        return 0

    def remover_item_ao_cardapio():
        return 0

    def alterar_preco_de_item_ao_cardapio():
        return 0
    
    def info(self):
        print(f"Nome: {self.nome}\nEndereço: {self.endereco}\nTelefone: {self.telefone}\nEmail: {self.email}\nLongitude: {self.longitude}\nLatitude: {self.latitude}\nCardapio:\n{self.cardapio}\nFuncionamento: {self.funcionamento}\nDelivery: {self.delivery}\nTaxa de Delivery: {self.taxa_delivery}")
        