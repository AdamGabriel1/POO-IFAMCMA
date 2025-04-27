while True: 
    print("|===========================|")
    print("|     Exemplos Exceções     |")
    print("|1. Exemplo 1               |")
    print("|2. Exemplo 2               |")
    print("|3. Exemplo 3               |")
    print("|4. Exemplo 4               |")
    print("|5. Exemplo 5               |")
    print("|0. Sair                    |")
    print("|===========================|")
    opcao=input("Insira a opção que você quer: ")
    match opcao:
        case "0": break
        case "1":
            print("Exemplo 1: ")
            while True:
                x = int(input("Digite um número: "))
                y = int(input("Digite outro número: "))
                resultado = x / y
            print(f"O resultado é: {resultado}")
            print("... continua o programa")

            print("Exemplo 2: ")
            try:
                x = int(input("Digite um número: "))
                y = int(input("Digite outro número: "))
                resultado = x / y
                print(f"O resultado é: {resultado}")
            except ZeroDivisionError:
                print("Erro: Não é possível dividir por zero!")
            except ValueError:
                print("Erro: Entrada inválida! Por favor, digite um número.")
            print("... continua o programa")

            print("Exemplo 3: ")
            while True:
                try:
                    x = int(input("Digite um número: "))
                    y = int(input("Digite outro número: "))
                    resultado = x / y
                    print(f"O resultado é: {resultado}")
                except Exception as e:
                    print(f"Ocorreu um erro: {e}")
            print("... continua o programa")
            
        case "2":
            print("Exemplo 1: ")
            try:
                x = int(input("Digite um número: "))
                y = int(input("Digite outro número: "))
                resultado = x / y
            except ZeroDivisionError:
                print("Erro: Não é possível dividir por zero!")
            except ValueError:
                print("Erro: Entrada inválida! Por favor, digite um número.")
            else:
                print(f"O resultado é: {resultado}")
            print("... continua o programa")

            print("Exemplo 2: ")
            try:
                x = int(input("Digite um número: "))
                y = int(input("Digite outro número: "))
                resultado = x / y
            except ZeroDivisionError:
                print("Erro: Não é possível dividir por zero!")
            except ValueError:
                print("Erro: Entrada inválida! Por favor, digite um número.")
            else:
                print(f"O resultado é: {resultado}")
            print("... continua o programa")
            
            print("Exemplo 3: ")
            try:
                x = int(input("Digite um número: "))
                y = int(input("Digite outro número: "))
                resultado = x / y
            except ZeroDivisionError:
                print("Erro: Não é possível dividir por zero!")
            except ValueError:
                print("Erro: Entrada inválida! Por favor, digite um número.")
            finally:
                print(f"O resultado é: {resultado}")
            print("Execução finalizada.")
        
        case "3":
            try:
                x = int(input("Digite um número: "))
                y = int(input("Digite outro número: "))
                resultado = x / y
            except ZeroDivisionError:
                print("Erro: Não é possível dividir por zero!")
            except ValueError:
                print("Erro: Entrada inválida! Por favor, digite um número.")
            finally:
                print(f"O resultado é: {resultado}")
            print("Execução finalizada.")
            
        case "4":
            class ErrorNovoException(Exception):
                def __init__(self, mensagem):
                    self.mensagem = mensagem
                    super().__init__(self.mensagem)
                def dividir(a, b):
                    if b == 3:
                        raise ErrorNovoException("Não é possível dividir por 3!")
                    return a / b
            try:
                resultado = dividir(10, 2)
            except ErrorNovoException as e:
                print(f"Erro: {e.mensagem}")
            else:
                print("resultado:", resultado)
            print("... continua o programa")

        case "5":
            print("Exemplo 1: ")
            try:
                f = open('arquivo_inexistente.txt', 'r')
            except FileNotFoundError:
                print("Erro: Arquivo não encontrado!")
            print("... continua o programa")
            
            print("Exemplo 2: ")
            try:
                numero = int(input("Digite um número: "))
            except ValueError:
                print("Erro: Você não digitou um número válido!")
            print("... continua o programa")
            
            print("Exemplo 3.1: ")
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
                    
            print("Exemplo 3.2: ")
            capitais = {'Brasil': 'Brasília', 'França': 'Paris', 'EUA': 'Washington', 'Japão': 'Tóquio'}
            entrada = input("Entre com um país: ")
            try:
                print(capitais[entrada])
            except KeyError:
                print("Erro: Chave não encontrada no dicionário!")
            print("... continua o programa")
            
            print("Exemplo 4: ")
            try:
                resultado = 'abc' + 123
            except TypeError:
                print("Erro: Não é possível somar uma string e um número!")
            print("... continua o programa")

            print("Exemplo 5: ")
            try:
                import biblioteca_inexistente
            except ModuleNotFoundError:
                print("Erro: Biblioteca não encontrada!")
            print("... continua o programa")

        case _: print("Opção errada, tente novamente.")
