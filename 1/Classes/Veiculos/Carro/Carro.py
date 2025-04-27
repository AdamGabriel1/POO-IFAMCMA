class Carro:
    def __init__(self,marca,modelo,ano,cor,tipo_motor,tipo_transmissao,vm,preco,disponibilidade,quilometragem):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.cor=cor
        self.tipo_motor=tipo_motor
        self.tipo_transmissao=tipo_transmissao
        self.vm=vm
        self.preco=preco
        self.disponibilidade=disponibilidade
        self.quilometragem=quilometragem

        # Outros
        self.motor = False
        self.acelerador = False
        self.freio = False
        self.marcha = 0
        self.velocidade = 0
        self.tempo = 0
        self.distancia = 0

    def ligar_motor(self):
        if not self.motor:
            self.motor = True
            print(f"Motor do carro {self.modelo} ligado.")
        else:
            print(f"O motor do carro {self.modelo} já está ligado.")

    def desligar_motor(self):
        if self.motor:
            self.motor = False
            self.acelerador = False
            self.freio = False
            self.marcha = 0
            self.velocidade = 0
            self.tempo = 0
            self.distancia = 0
            print("Motor desligado.")
        else:
            print("O motor já está desligado.")

    def acelerar(self):
        if self.motor:
            self.acelerador = True
            print("Acelerando.")
        else:
            print("É necessário ligar o motor primeiro.")

    def frear(self):
        if self.acelerador:
            self.acelerador = False
            self.freio = True
            print("Freando.")
        else:
            print("Você precisa acelerar para frear.")

    def mudar_marcha(self):
        if self.motor:
            if self.velocidade >= 30 and self.velocidade < 50:
                self.marcha = 2
            elif self.velocidade >= 50 and self.velocidade < 70:
                self.marcha = 3
            elif self.velocidade >= 70:
                self.marcha = 4
            else:
                self.marcha = 1
            print(f"Marcha alterada para {self.marcha}.")
        else:
            print("É necessário ligar o motor primeiro.")

    def calcular_velocidade_media(self):
        if self.tempo != 0 and self.distancia != 0:
            velocidade_media = self.distancia / self.tempo
            print(f"Velocidade média: {velocidade_media} km/h.")
        elif self.tempo == 0:
            print("Não é possível calcular a velocidade média pois o tempo é zero.")
        elif self.distancia == 0:
            print("Não é possível calcular a velocidade média pois a distância é zero.")
        else:
            print("Não é possível calcular a velocidade média pois a distância e o tempo são zero.")

    def pintar(self,nova_cor):
        self.cor=nova_cor
        print(f"A nova cor do carro {self.marca} {self.modelo} é: {self.cor}.")

    def att_preco(self,novo_preco):
        self.preco=novo_preco
        print(f"O novo preço do carro {self.marca} {self.modelo} é: {self.preco}.")

    def info(self):
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")
        print(f"Marcha: {self.marcha}")
        print(f"Velocidade: {self.velocidade}")
        print(f"Tempo: {self.tempo}")
        print(f"Distância: {self.distancia}")