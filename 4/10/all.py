from abc import ABC, abstractmethod
import math

class Animal2(ABC):
    @abstractmethod
    def emitir_som(self):
        pass
class Cachorro2(Animal2):
    def emitir_som(self):
        print("Au au!")
class Gato2(Animal2):
    def emitir_som(self):
        print("Miau!")
        
class FormaGeometrica(ABC):
    def __init__(self, posX:int, posY: int):
        self.posX = posX
        self.posY = posY
        
    @abstractmethod
    def getArea(self):
        pass
    
    @abstractmethod
    def getPerimetro(self):
        pass
    
    def getPosString(self):
        saida = "posicao (" + str(self.posX) + ", " + str(self.posY) + ")"
        return saida
        
class Circulo(FormaGeometrica):
    def __init__(self, posX:int, posY: int, raio: float):
        super().__init__(posX, posY)
        self.raio = raio
        
    def getArea(self):
        super().getArea()
        return math.pi * self.raio**2
    
    def getPerimetro(self):
        super().getPerimetro()
        return 2 * math.pi * self.raio
    
    def toString(self):
        print(f"Círculo na posição {super().getPosString()} com raio de {self.raio}cm")
        
class Retangulo(FormaGeometrica):
    def __init__(self, posX:int, posY: int, largura: float, altura: float):
        super().__init__(posX, posY)
        self.largura = largura
        self.altura = altura
        
    def getArea(self):
        super().getArea()
        return self.largura * self.altura
    
    def getPerimetro(self):
        super().getPerimetro()
        return 2 * (self.largura + self.altura)
    
    def toString(self):
        print(f"Retangulo na posição {super().getPosString()} com largura de {self.largura}")
        
class Pessoa2(ABC):
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade
    
    def apresentar(self):
        raise NotImplementedError
    
class Professor2(Pessoa2):
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e sou um Professor2.")
        
class Aluno2(Pessoa2):
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e sou um Aluno2.")
        
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

while True: 
    print("|===========================|")
    print("|        Exercicio 10       |")
    print("|1. Exemplos                |")
    print("|2. Tarefa 1                |")
    print("|3. Tarefa 2                |")
    print("|0. Sair                    |")
    print("|===========================|")
    opcao=input("Insira a opção que você quer: ")
    match opcao:
        case "0": break
        case "1":
            Animal21 = Cachorro2()
            Animal21.emitir_som()
            Animal22 = Gato2()
            Animal22.emitir_som()
            
            obj_um = Circulo(10, 10, 5.0)
            print(obj_um.getArea())
            print(obj_um.getPerimetro())
            obj_um.toString()
        
            obj_dois = Retangulo(12, 65, 2.0, 7.0)
            print(obj_dois.getArea())
            print(obj_dois.getPerimetro())
            obj_dois.toString()
            
        case "2":
            Professor2=Professor2("Yuri", 15)
            Aluno2=Aluno2("Adam", 15)

            Professor2.apresentar()
            Aluno2.apresentar()
        
        case "3":
            macaco=Macaco()
            macaco.respirar()

            humano=Humano()
            humano.respirar()
            
        case _: print("Opção errada, tente novamente.")
