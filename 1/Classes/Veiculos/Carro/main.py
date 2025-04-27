from Carro import Carro

fiat_uno=Carro("Fiat","Uno",1984,"Preto","Fire 1.0 Evo 8V Flex","5 marchas, manual","152 km/h","R$ 9.553",
               "1ª geração 1984-2013",0)
fuscao_preto=Carro("Volkswagem","Fusca Type 1",1938,"Preto","1.2L F4","4 marchas, manual","112 km/h",
                   "R$ 20.000,00 a 150.000,00","1938–2003 (total)",0)

fiat_uno.ligar_motor()
fiat_uno.acelerar()
fiat_uno.velocidade = 40
fiat_uno.mudar_marcha()

print(f"\nInformações do carro {fiat_uno.marca} {fiat_uno.modelo}:")
fiat_uno.info()

fiat_uno.distancia = 100
fiat_uno.tempo = 2
fiat_uno.calcular_velocidade_media()

fiat_uno.frear()
fiat_uno.desligar_motor()

print(f"\nInformações do carro {fiat_uno.marca} {fiat_uno.modelo} após desligar:")
fiat_uno.info()

fiat_uno.pintar("Cinza")

print("\n")
fuscao_preto.ligar_motor()
fuscao_preto.acelerar()
fuscao_preto.velocidade = 70
fuscao_preto.mudar_marcha()

print(f"\nInformações do carro {fuscao_preto.marca} {fuscao_preto.modelo}:")
fuscao_preto.info()

fuscao_preto.distancia = 400
fuscao_preto.tempo = 5
fuscao_preto.calcular_velocidade_media()

fuscao_preto.frear()
fuscao_preto.desligar_motor()

print(f"\nInformações do carro {fuscao_preto.marca} {fuscao_preto.modelo} após desligar:")
fuscao_preto.info()

fuscao_preto.att_preco("R$ 50.000,00 a 150.000,00")
