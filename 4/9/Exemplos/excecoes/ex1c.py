while True:
    try:
        x = int(input("Digite um número: "))
        y = int(input("Digite outro número: "))
        resultado = x / y
        print(f"O resultado é: {resultado}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
print("... continua o programa")
