capitais = {'Brasil': 'Brasília', 'França': 'Paris', 'EUA': 'Washington', 'Japão': 'Tóquio'}
while True:
    try:
        entrada = input("Entre com um país: ")
        print(capitais[entrada])
    except:
        print("País não encontrado")
        pais = entrada
        capital = input("Entre com a capital de " + pais)
        capitais[pais] = capital