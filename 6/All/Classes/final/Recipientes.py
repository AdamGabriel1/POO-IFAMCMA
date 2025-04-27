class Recipiente(ABC):
    def __init__(self, raio_topo, raio_base, altura, material, estilo):
        self.raio_topo = raio_topo
        self.raio_base = raio_base
        self.altura = altura
        self.material = material
        self.estilo = estilo

    @abstractmethod
    def Calcular_volume(self):
        pass

    def Encher(self):
        print(f"{self.__class__.__name__} está cheio.")

    def Esvaziar(self):
        print(f"{self.__class__.__name__} está vazio.")

class Caneca(Recipiente):
    def __init__(self, raio_topo, raio_base, altura, material, estilo, formato_da_alca):
        super().__init__(raio_topo, raio_base, altura, material, estilo)
        self.formato_da_alca = formato_da_alca

    def Calcular_volume(self):
        volume = (1/3) * pi * self.altura * (self.raio_topo**2 + self.raio_base**2 + self.raio_topo * self.raio_base)
        print(f"Volume da Caneca: {volume} unidades cúbicas")

class Copo(Recipiente):
    def Calcular_volume(self):
        volume = (1/3) * pi * self.altura * (self.raio_topo**2 + self.raio_base**2 + self.raio_topo * self.raio_base)
        print(f"Volume do Copo: {volume} unidades cúbicas")

class Taca(Recipiente):
    def __init__(self, raio_topo, raio_base, altura, material, estilo, tipo_de_bebida):
        super().__init__(raio_topo, raio_base, altura, material, estilo)
        self.tipo_de_bebida = tipo_de_bebida

    def Calcular_volume(self):
        volume = (1/3) * pi * self.altura * (self.raio_topo**2 + self.raio_base**2 + self.raio_topo * self.raio_base)
        print(f"Volume da Taça: {volume} unidades cúbicas")

class Jarra(Recipiente):
    def __init__(self, raio_topo, raio_base, altura, material, estilo, capacidade):
        super().__init__(raio_topo, raio_base, altura, material, estilo)
        self.capacidade = capacidade

    def Calcular_volume(self):
        volume = (1/3) * pi * self.altura * (self.raio_topo**2 + self.raio_base**2 + self.raio_topo * self.raio_base)
        print(f"Volume da Jarra: {volume} unidades cúbicas")
