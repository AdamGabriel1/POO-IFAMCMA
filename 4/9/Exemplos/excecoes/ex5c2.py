capitais = {'Brasil': 'Brasília', 'França': 'Paris', 'EUA': 'Washington', 'Japão': 'Tóquio'}
entrada = input("Entre com um país: ")
try:
    print(capitais[entrada])
except KeyError:
    print("Erro: Chave não encontrada no dicionário!")
print("... continua o programa")