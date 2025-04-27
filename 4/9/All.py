while True: 
    print("|===========================|")
    print("|        Exercicio 9        |")
    print("|1. Exemplos Exceções       |")
    print("|2. Exemplos Assert         |")
    print("|3. Tarefa                  |")
    print("|0. Sair                    |")
    print("|===========================|")
    opcao=input("Insira a opção que você quer: ")
    match opcao:
        case "0": break
        case "1":
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
       
        case "2":
            while True: 
                print("|===========================|")
                print("|     Exemplos Assert       |")
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
                        print("Exemplo 1:")
                        def divide(x, y):
                            assert y != 0, "Divisão por zero não é permitida"
                            return x / y
                        print(divide(50, 5))
                        print(divide(10, 0))
                        print(divide(10, 2))

                    case "2":
                        print("Exemplo 2: ")
                        def encontrar_maior(lista):
                            if len(lista) == 0:
                                return -1
                            return max(lista)
                        print(encontrar_maior([1, 2, 3, 4]))
                        print(encontrar_maior([21, 421, 4, 432, 253, 523]))
                        print("... continua o codigo")

                    case "3":
                        print("Exemplo 3: ")
                        def calcular_imc(peso, altura):
                            assert peso > 0 and altura > 0, "Peso e altura devem ser maiores que zero"
                            return peso / altura**2
                        resultado = calcular_imc(-70, 1.75)
                        resultado = calcular_imc(73, 1.90)
                        print(resultado)
                        print("... continua o programa")

                    case "4":
                        print("Exemplo 4: ")
                        class Pilha:
                            def __init__(self):
                                self.items = []
                            def empilhar(self, item):
                                self.items.append(item)
                            def desempilhar(self):
                                assert len(self.items) > 0, "Não é possível desempilhar de uma pilha"
                                return self.items.pop()
                        p = Pilha()
                        p.empilhar(1)
                        p.empilhar(5)
                        print(p.items)
                        print(p.desempilhar())
                        print(p.desempilhar())
                        print(p.items)
                        p.empilhar(3)
                        p.empilhar(2)
                        print(p.items)

                    case "5":
                        print("Exemplo 5: ")
                        import requests
                        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
                        requisicao_dic = requisicao.json()
                        cotacao = requisicao_dic["USDBRL"]["bid"]
                        print(type(cotacao), cotacao)
                        preco_produto = 100 # DOLAR
                        cotacao = float(cotacao)
                        assert type(cotacao) == float, "Cotacao não é do tipo FLOAT"
                        faturamento = preco_produto * cotacao
                        print('o preco do produto de ', preco_produto, 'em dolares, é igual a ', faturamento)

                        preco_produto_2 = 1265 # DOLAR
                        faturamento_2 = preco_produto_2 * cotacao
                        print('o preco do produto de ', preco_produto_2, 'em dolares, é igual a ', faturamento_2)

                    case "6":
                        print("Exemplo 6: ")
                        def soma(a, b):
                            assert isinstance(a, int) and isinstance(b, int), "A e B devem ser inteiros"
                            return a + b
                        print(soma(2, 3))
                        print(soma('a', 3))
                        print(soma('a', 'b'))
                        print(soma(50, 10))
                        print("akjsdlkjsadlkja")
                        
                    case _: print("Opção errada, tente novamente.")
                    
        case "3":
            def divisao(a, b):
                assert b != 0, "b deve ser diferente de zero"
                return a / b

            def soma(a, b):
                return a + b
                
            def calcular_imc(peso, altura):
                assert altura > 0, "Altura deve ser maior que zero."
                assert peso > 0, "Peso deve ser maior que zero."
                return peso / (altura ** 2)
                
            def encontrar_maior(lista):
                assert len(lista) > 0, "A lista não pode estar vazia."
                return max(lista)

            for i in range(2):
                print("\nDivisão:")
                a=int(input("Insira um número: "))
                b=int(input("Insira um número: "))
                print(f"A divisão de A por B é: {divisao(a, b)}")

                print("\nSoma:")
                a=int(input("Insira um número: "))
                b=int(input("Insira um número: "))
                print(f"A soma de A e B é: {soma(a, b)}")

                print("\nIMC:")
                peso=float(input("Insira o seu peso: "))
                altura=float(input("Insira a sua altura: "))
                print(f"O seu IMC é: {calcular_imc(peso, altura)}")

                print("\nLista:")
                lista=list(input("Insira uma lista, exemplo '1, 2, 3, 4, 5': "))
                print(f"O maior valor da lista é: {encontrar_maior(lista)}")

            def dividir_numeros(a, b):
                try:
                    return a / b
                except ZeroDivisionError:
                    return "Erro: Divisão por zero."
                except TypeError:
                    return "Erro: Entrada inválida"

            def dividir_numeros_2(a, b):
                try:
                    resultado = a / b
                except ZeroDivisionError:
                    return "Erro: Divisão por zero."
                except TypeError:
                    return "Erro: Entrada inválida"
                else:
                    return resultado
                    
            def dividir_numeros_3(a, b):
                try:
                    return a / b
                except ZeroDivisionError:
                    return "Erro: Divisão por zero."
                except TypeError:
                    return "Erro: Entrada inválida"
                finally:
                    print("Operação de divisão concluída.")
                    
            def ler_arquivo(nome_arquivo):
                try:
                    with open(nome_arquivo, "r") as file:
                        return file.read()
                except FileNotFoundError:
                    return "Erro: Arquivo não encontrado."
                    
            def buscar_chave(dicionario, chave):
                try:
                    return dicionario[chave]
                except KeyError:
                    return "Erro: Chave não encontrada."
                    
            def importar_biblioteca(nome_biblioteca):
                try:
                    __import__(nome_biblioteca)
                    return f"Biblioteca '{nome_biblioteca}' importada com sucesso."
                except ImportError:
                    return f"Erro: Biblioteca {nome_biblioteca} não encontrada."

            print("\nDivisão Try, Except 1:")
            print(dividir_numeros(10, 0))
            print(dividir_numeros(10, 'a'))

            print("\nDivisão Try, Except 2:")
            print(dividir_numeros_2(20, 2))
            print(dividir_numeros_2(50, 5))

            print("\nDivisão Try, Except 3:")
            print(dividir_numeros_3(50, 2))
            print(dividir_numeros_3(100, 2))

            print("\nLer Arquivo")
            print(ler_arquivo("arquivo.txt"))

            print("\nDicionario")
            dicionario = {"a": 1, "b": 2}
            print(buscar_chave(dicionario, "a"))
            print(buscar_chave(dicionario, "c"))

            print("\nBiblioteca")
            print(importar_biblioteca("os"))
            print(importar_biblioteca("biblioteca"))
            
        case _: print("Opção errada, tente novamente.")
