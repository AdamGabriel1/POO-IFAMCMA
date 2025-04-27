class FormaGeometrica(ABC):
    def __init__(self, posX: int, posY: int):
        self.posX = posX
        self.posY = posY
        
    @abstractmethod
    def getArea(self):
        pass
    
    @abstractmethod
    def getPerimetro(self):
        pass
    
    def getPosString(self):
        return f"posição ({self.posX}, {self.posY})"

class Circulo(FormaGeometrica):
    def __init__(self, posX: int, posY: int, raio: float):
        super().__init__(posX, posY)
        self.raio = raio
        
    def getArea(self):
        return math.pi * self.raio ** 2
    
    def getPerimetro(self):
        return 2 * math.pi * self.raio
    
    def toString(self):
        print(f"Círculo na {self.getPosString()} com raio de {self.raio}cm")

class Retangulo(FormaGeometrica):
    def __init__(self, posX: int, posY: int, largura: float, altura: float):
        super().__init__(posX, posY)
        self.largura = largura
        self.altura = altura
        
    def getArea(self):
        return self.largura * self.altura
    
    def getPerimetro(self):
        return 2 * (self.largura + self.altura)
    
    def toString(self):
        print(f"Retângulo na {self.getPosString()} com largura de {self.largura}cm e altura de {self.altura}cm")

class Triangulo(FormaGeometrica):
    def __init__(self, posX: int, posY: int, base: float, altura: float):
        super().__init__(posX, posY)
        self.base = base
        self.altura = altura
        
    def getArea(self):
        return (self.base * self.altura) / 2
    
    def getPerimetro(self, a: float, b: float, c: float):
        return a + b + c
    
    def toString(self):
        print(f"Triângulo na {self.getPosString()} com base de {self.base}cm e altura de {self.altura}cm")