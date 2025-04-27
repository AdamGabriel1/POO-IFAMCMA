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
