def calcular_imc(peso, altura):
    assert peso > 0 and altura > 0, "Peso e altura devem ser maiores que zero"
    return peso / altura**2
resultado = calcular_imc(-70, 1.75)
resultado = calcular_imc(73, 1.90)
print(resultado)
print("... continua o programa")
