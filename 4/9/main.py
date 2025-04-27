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
