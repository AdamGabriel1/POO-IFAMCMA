from Moto import Moto

moto1 = Moto("Suzuki", "Vermelha")
moto2 = Moto("Honda", "Azul")

moto1.ligar_motor()
moto1.acelerar()
moto1.velocidade = 40
moto1.mudar_marcha()

print("\nInformações da Moto 1:")
moto1.info()

moto1.distancia = 100
moto1.tempo = 2
moto1.calcular_velocidade_media()

moto1.frear()
moto1.desligar_motor()

print("\nInformações da Moto 1 após desligar:")
moto1.info()

print("\n")
moto2.ligar_motor()
moto2.acelerar()
moto2.velocidade = 70
moto2.mudar_marcha()

print("\nInformações da Moto 2:")
moto2.info()

moto2.distancia = 400
moto2.tempo = 5
moto2.calcular_velocidade_media()

moto2.frear()
moto2.desligar_motor()

print("\nInformações da Moto 2 após desligar:")
moto2.info()
