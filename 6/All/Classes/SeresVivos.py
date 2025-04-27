class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade
    
    def apresentar(self):
        raise NotImplementedError
    
class Professor(Pessoa):
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e sou um Professor.")
        
class Aluno(Pessoa):
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e sou um Aluno.")
        
class SerVivo(ABC):
    @abstractmethod
    def respirar(self):
        raise NotImplementedError
    
class Macaco(SerVivo):
    def respirar(self):
        print("Respirando como um macaco")

class Humano(SerVivo):
    def respirar(self):
        print("Respirando como um humano")

class Animal(ABC):
    def __init__(self,cor,altura,peso):
        self.cor=cor
        self.altura=altura
        self.peso=peso

class Ave(SerVivo):
    def __init__(self,tipo_ave,voa,peso):
        self.tipo_ave=tipo_ave
        self.voa=voa
        self.peso=peso

    def voar(self):
        if self.voa=="Sim":
            print(f"A (o) {self.tipo_ave} de {self.peso} está voando.")
        else:
            print(f"A (o) {self.tipo_ave} {self.peso} não pode voar.")

    def respirar(self):
        print("Respirando como uma ave")

class Cachorro(SerVivo):
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

    def respirar(self):
        print("Respirando como um cachorro")