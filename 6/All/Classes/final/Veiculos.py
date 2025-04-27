class Veiculo(ABC):
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.motor = False
        self.velocidade = 0
        self.distancia = 0
        self.tempo = 0

    def mudar_marcha(self):
        print("Mudando marcha.")

    def calcular_velocidade_media(self):
        if self.tempo > 0:
            velocidade_media = self.distancia / self.tempo
            print(f"Velocidade média: {velocidade_media} km/h")
        else:
            print("Tempo não pode ser zero.")

    def pintar(self, nova_cor):
        self.cor = nova_cor
        print(f"Veículo pintado de {self.cor}.")

    def att_preco(self, novo_preco):
        self.preco = novo_preco
        print(f"Preço atualizado para {self.preco}.")

class Farol:
    def __init__(self, tipo, potencia):
        self.__tipo = tipo
        self.__potencia = potencia

    @property
    def tipo(self):
        return self.__tipo  # getters

    @property
    def potencia(self):
        return self.__potencia  # getters

    def acender(self):
        print("Acendendo farol...")

    def apagar(self):
        print("Apagando farol")

class VeiculoComFarol(Veiculo):
    def __init__(self, modelo, cor, farol: Farol):
        super().__init__(modelo, cor)
        self.farol = farol
        self.farois = []

    def acender_farol(self):
        self.farol.acender()

    def apagar_farol(self):
        self.farol.apagar()

    def instalaFarol(self, farol):
        self.farois.append(farol)
        print(f"Farol do tipo {farol.tipo} instalado.")

    def info(self):
        super().info()
        print(f"Farol: {self.farol.tipo} (Potência: {self.farol.potencia}W)")
        
class Aviao(Veiculo):
    def __init__(self, companhia_aerea, modelo, ano, cor, tipo_motor, tipo_transmissao, vm, preco, disponibilidade, quilometragem):
        super().__init__(modelo, cor)
        self.companhia_aerea = companhia_aerea
        self.ano = ano
        self.tipo_motor = tipo_motor
        self.tipo_transmissao = tipo_transmissao
        self.vm = vm
        self.preco = preco
        self.disponibilidade = disponibilidade
        self.quilometragem = quilometragem

        self.altitude = 0
        self.tempo_voo = 0
        self.horas_motor = 0
        self.passageiros = 0
        self.carga = 0
        self.manutencao_registrada = False
        self.tempo_manutencao = 0

    def ligar_motor(self):
        if not self.motor:
            self.motor = True
            print(f"Motor do avião {self.modelo} ligado.")
        else:
            print(f"O motor do avião {self.modelo} já está ligado.")

    def desligar_motor(self):
        if self.motor:
            self.motor = False
            self.velocidade = 0
            self.altitude = 0
            print("Motor desligado.")
        else:
            print("O motor já está desligado.")

    def acelerar(self):
        if self.motor:
            self.velocidade += 50
            print("Acelerando o avião.")
        else:
            print("É necessário ligar o motor primeiro.")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 50
            print("Freando o avião.")
        else:
            print("O avião já está parado.")

    def decolar(self):
        if self.motor and self.velocidade >= 200:
            self.altitude += 10000
            print(f"Avião {self.modelo} decolou.")
        else:
            print("É necessário ligar o motor e acelerar mais para decolar.")

    def voar(self, distancia):
        if self.motor and self.altitude > 0:
            self.distancia += distancia
            self.tempo_voo += distancia / self.velocidade
            print(f"Avião {self.modelo} voou {distancia} km.")
        else:
            print("O avião precisa estar em altitude para voar.")

    def atualizar_quilometragem(self, km):
        self.quilometragem += km
        print(f"Quilometragem atualizada para {self.quilometragem} km.")

    def verificar_manutencao(self):
        if self.quilometragem > 10000:
            self.manutencao_registrada = True
            self.tempo_manutencao += 10
            print("Manutenção realizada.")
        else:
            print("Manutenção não necessária.")

    def info(self):
        print(f"Companhia Aérea: {self.companhia_aerea}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade: {self.velocidade} km/h")
        print(f"Altitude: {self.altitude} metros")
        print(f"Distância percorrida: {self.distancia} km")
        print(f"Tempo de voo: {self.tempo_voo} horas")
        print(f"Horas de motor: {self.horas_motor} horas")
        print(f"Quilometragem: {self.quilometragem} km")
        print(f"Passageiros a bordo: {self.passageiros}")
        print(f"Carga a bordo: {self.carga} kg")
        if self.manutencao_registrada:
            print(f"Tempo total de manutenção: {self.tempo_manutencao} horas")
            
class Carro(VeiculoComFarol):
    def __init__(self, marca, modelo, ano, cor, tipo_motor, tipo_transmissao, vm, preco, disponibilidade, quilometragem):
        super().__init__(modelo, cor)
        self.marca = marca
        self.ano = ano
        self.tipo_motor = tipo_motor
        self.tipo_transmissao = tipo_transmissao
        self.vm = vm
        self.preco = preco
        self.disponibilidade = disponibilidade
        self.quilometragem = quilometragem

    def ligar_motor(self):
        if not self.motor:
            self.motor = True
            print(f"Motor do carro {self.modelo} ligado.")
        else:
            print(f"O motor do carro {self.modelo} já está ligado.")

    def desligar_motor(self):
        if self.motor:
            self.motor = False
            self.velocidade = 0
            print("Motor desligado.")
        else:
            print("O motor já está desligado.")

    def acelerar(self):
        if self.motor:
            self.velocidade += 10
            print("Acelerando o carro.")
        else:
            print("É necessário ligar o motor primeiro.")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print("Freando o carro.")
        else:
            print("O carro já está parado.")

    def info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade: {self.velocidade} km/h")
        print(f"Quilometragem: {self.quilometragem} km")
        print(f"Disponibilidade: {'Sim' if self.disponibilidade else 'Não'}")
        
class Moto(VeiculoComFarol):
    def __init__(self, marca, modelo, cor):
        super().__init__(modelo, cor)
        self.marca = marca

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"A moto {self.marca} {self.modelo} acelerou para {self.velocidade} km/h.")

class Motoatt(Veiculo):
    def __init__(self, modelo, cor):
        super().__init__(modelo, cor)

    def ligar_motor(self):
        if not self.motor:
            self.motor = True
            print(f"Motor da moto {self.modelo} ligado.")
        else:
            print(f"O motor da moto {self.modelo} já está ligado.")

    def desligar_motor(self):
        if self.motor:
            self.motor = False
            self.velocidade = 0
            print("Motor desligado.")
        else:
            print("O motor já está desligado.")

    def acelerar(self):
        if self.motor:
            self.velocidade += 5
            print("Acelerando a moto.")
        else:
            print("É necessário ligar o motor primeiro.")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 5
            print("Freando a moto.")
        else:
            print("A moto já está parada.")

    def info(self):
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Velocidade: {self.velocidade} km/h")