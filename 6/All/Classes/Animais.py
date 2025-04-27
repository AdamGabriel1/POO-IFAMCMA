class Animal(ABC):
    def __init__(self,cor,altura,peso):
        self.cor=cor
        self.altura=altura
        self.peso=peso

class Ave:
    def __init__(self,tipo_ave,voa,peso):
        self.tipo_ave=tipo_ave
        self.voa=voa
        self.peso=peso

    def voar(self):
        if self.voa=="Sim":
            print(f"A (o) {self.tipo_ave} de {self.peso} está voando.")
        else:
            print(f"A (o) {self.tipo_ave} {self.peso} não pode voar.")

class Cachorro:
    def __init__(self,nome,raca,idade,cor,altura,peso,genero,dono):
        self.nome=nome
        self.raca=raca
        self.idade=idade
        self.cor=cor
        self.altura=altura
        self.peso=peso
        self.genero=genero
        self.dono=dono

    def latir(self):
        print("Auuuuuuuu!!!!")

    def andar(self):
        print("Se não for mais de 5km de corrida eu não vou.")

    def comer(self):
        print("Se não for Pedigree eu não como.")

    def brincar(self):
        print("")

    def fazer_truques(self):
        print("Aqui não é esses negocio de dar a patinha não eu jogo Basquete, me respeita.")

    def receber_carinho(self):
        print("Melhor cachorro do Brasil...")

    def definir_dono(self,novo_dono):
        self.dono=novo_dono