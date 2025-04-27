class Aviao:
    def __init__(self, companhia_aerea, modelo, ano, cor, tipo_motor, tipo_transmissao, vm, preco, disponibilidade, quilometragem):
        self.companhia_aerea = companhia_aerea
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.tipo_motor = tipo_motor
        self.tipo_transmissao = tipo_transmissao
        self.vm = vm
        self.preco = preco
        self.disponibilidade = disponibilidade
        self.quilometragem = quilometragem

        # Outros atributos
        self.motor = False
        self.velocidade = 0
        self.altitude = 0
        self.distancia = 0
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

    def decolar(self):
        if self.motor:
            self.velocidade = 200
            self.altitude = 10000
            print(f"Avião {self.modelo} decolando.")
        else:
            print("É necessário ligar o motor primeiro.")

    def pousar(self):
        if self.velocidade == 0 and self.altitude == 0:
            print("O avião já está no solo.")
        else:
            self.velocidade = 0
            self.altitude = 0
            print(f"Avião {self.modelo} pousando.")

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

    def voar(self, distancia):
        if self.motor:
            self.distancia += distancia
            self.tempo_voo += distancia / self.vm
            self.horas_motor += self.tempo_voo
            print(f"Avião {self.modelo} voando por {distancia} km.")
        else:
            print("É necessário ligar o motor primeiro.")

    def calcular_consumo_combustivel(self):
        if self.motor:
            consumo_total = self.tempo_voo * self.tipo_motor
            print(f"Consumo total de combustível: {consumo_total} litros.")
        else:
            print("É necessário ligar o motor primeiro.")

    def verificar_manutencao(self):
        if self.horas_motor >= 1000 and not self.manutencao_registrada:
            print("O avião precisa de manutenção.")
        else:
            print("O avião está em boas condições.")

    def registrar_manutencao(self, tempo):
        self.manutencao_registrada = True
        self.tempo_manutencao += tempo
        print(f"Manutenção registrada: {tempo} horas de manutenção realizadas.")

    def verificar_disponibilidade_passageiros(self, quantidade):
        if self.disponibilidade:
            lugares_disponiveis = 300 - self.passageiros
            if quantidade <= lugares_disponiveis:
                return True
            else:
                print("Capacidade máxima de passageiros excedida.")
                return False
        else:
            print("O avião não está disponível para embarque.")
            return False

    def verificar_disponibilidade_carga(self, peso):
        if self.disponibilidade:
            capacidade_disponivel = 10000 - self.carga
            if peso <= capacidade_disponivel:
                return True
            else:
                print("Capacidade máxima de carga excedida.")
                return False
        else:
            print("O avião não está disponível para carga.")
            return False

    def calcular_distancia_restante(self, combustivel):
        if self.motor:
            distancia_restante = combustivel * self.vm
            print(f"Distância restante: {distancia_restante} km.")
        else:
            print("É necessário ligar o motor primeiro.")

    def atualizar_quilometragem(self, distancia):
        self.quilometragem += distancia
        print(f"Quilometragem atualizada para {self.quilometragem} km.")

    def info(self):
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
