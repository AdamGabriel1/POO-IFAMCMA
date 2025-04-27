class Atividades:
    def a1(self):
        print("1. Calcule a média de valores da lista de números abaixo:\nlista_numeros = [10, 50, 30, 20, 50, 60, 75, 90]\n")
        lista_numeros=[10, 50, 30, 20, 50, 60, 75, 90]
        
        soma=0
        
        for i in lista_numeros:
            soma+=i
            
        media=soma/len(lista_numeros)
        print(media)

    def a2(self):
        print("2. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.\nDepois modifique o programa para que ele mostre os números um ao lado do outro.\n")
        saida=""
        
        for i in range(1, 20):
            saida+=f"{i}\n"
            
        print(saida)
        
        saida=""
        
        for i in range(1, 20):
            saida+=f"{i} "
            
        print(saida)
    
    def a3(self):
        print("3. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.\n")
        saida=""
        for i in range(50):
            if i%2==1:
                saida+=f"{i} "
        print(saida)

    def a4(self):
        print("4. Faça um programa que, dado a lista de números abaixo, determine o menor valor, o maior valor e a soma dos valores.\nlista_numeros = [5, 2, 1, 8, 10, 30, 50, 9, 22, 11, 7]\n")
        lista_numeros = [5, 2, 1, 8, 10, 30, 50, 9, 22, 11, 7]

        menor_valor = lista_numeros[0]
        maior_valor = lista_numeros[0]
        soma_valores = 0

        for numero in lista_numeros:
            soma_valores += numero

            if numero < menor_valor:
                menor_valor = numero
            
            if numero > maior_valor:
                maior_valor = numero

        print(f"Menor valor: {menor_valor}")
        print(f"Maior valor: {maior_valor}")
        print(f"Soma dos valores: {soma_valores}")
    
    def a5(self):
        print("5. Neste exercício, você possui duas listas de Python. Cada lista representa os gastos do mês de dois amigos, João e Pedro. Com base nas listas, imprima qual amigo gastou mais.\ngastos_joao = [300, 500, 200, 800]\ngastos_pedro = [200, 400, 500, 700]\n")
        gastos_joao = [300, 500, 200, 800]
        gastos_pedro = [200, 400, 500, 700]
        
        soma_joao=0
        soma_pedro=0
        
        for i in gastos_joao:
            soma_joao+=i
            
        for i in gastos_pedro:
            soma_pedro+=i
            
        if soma_joao>soma_pedro:
            print("João gastou mais que Pedro")
        else:
            print("Pedro gastou mais que João")
        
    def a6(self):
        print("6. Partindo de uma lista de palavras qualquer, como:\npalavras = ['python', 'asimov', 'código', 'web', 'programação']\nCrie um código que seja capaz de encontrar e exibir a maior e a menor palavra da lista (em número de caracteres).\n")
        palavras = ["python", "asimov", "código", "web", "programação"]

        maior_palavra = palavras[0]
        menor_palavra = palavras[0]

        for palavra in palavras:
            if len(palavra) > len(maior_palavra):
                maior_palavra = palavra
            
            if len(palavra) < len(menor_palavra):
                menor_palavra = palavra

        print(f"Maior palavra: {maior_palavra}")
        print(f"Menor palavra: {menor_palavra}")
    
    def a7(self):
        print("7. Você fez uma pequena pesquisa de preferência entre três produtos A, B e C. Na entrevista, cada entrevistado precisava escolher seu produto preferido. Os votos obtidos nessa pesquisa estão representados na lista abaixo:\nvotos = ['A', 'B', 'A', 'C', 'C', 'A', 'C', 'C', 'B', 'A']\nAgora, seu objetivo é calcular qual produto foi o mais votado. A partir da lista de votos, crie um dicionário onde a chave é cada produto, e o valor é o número de votos que o produto recebeu.\n")
        votos = ["A", "B", "A", "C", "C", "A", "C", "C", "B", "A"]

        contagem_votos = {}

        for voto in votos:
            if voto in contagem_votos:
                contagem_votos[voto] += 1
            else:
                contagem_votos[voto] = 1

        print(contagem_votos)

        produto_mais_votado = max(contagem_votos, key=contagem_votos.get)
        print(f"Produto mais votado: {produto_mais_votado} ({contagem_votos[produto_mais_votado]} votos)")
    
    def a8(self):
        print("8. Calcule a soma de todos os números pares entre 2 e 100 (inclusive)\n")
        soma=0
        for i in range(100):
            if i%2==0:
                soma=+i
        print(soma)
    
    def a9(self):
        print("9. Calcule a soma de todos os quadrados entre 1 e 100 (inclusive)\nObs: para elevar um número ao quadrado utilize o “**2” logo após o número.\nExemplo: 2**2 = 4\n")
        soma=0
        for i in range(100):
            q=i**2
            soma+=q
        print(soma)
        
    def a10(self):
        print("""
10. O que estes laços imprimem?
a. for i in range(1, 10):
    print(i)
b. for i in range(1, 10, 2):
    print(i)
c. for i in range(10, 1, ‐1):
    print(i)
d. for i in range(10):
    print(i)
e. for i in range(1, 10):
    if i % 2 == 0:
        print(i)
""")
        print("""a. 
1
2
3
4
5
6
7
8
9
""")
        print("""b.
1
3
5
7
9
""")
        print(f"c. Erro: SyntaxError: invalid character '‐' (U+2010)")
            
        print("""d.
0
1
2
3
4
5
6
7
8
9
""")
        print("""d.
2
4
6
8
""")

    def a11(self):
        print("""11. Quantas iterações os seguintes laços executam?
a. for i in range(1, 11) . . .
b. for i in range(10) . . .
c. for i in range(10, 0, −1) . . .
d. for i in range(−10, 11) . . .
e. for i in range(10, 0) . . .
f. for i in range(−10, 11, 2) . . .
g. for i in range(−10, 11, 3) . . .""")

        print("""
Interações:
a: 10
b: 10
c: 10
d: 21
e: 0
f: 11
g: 7""")
    
    def a12(self):
        print("""
12. O que o seguinte segmento de programa imprime? Encontre a resposta, rastreando
o código, não usando o computador.
a. n = 1
for i in range(2, 5) :
n = n + i
print(n)
""")
        print("""A saída é: 
3
6
10""")
    
    def a13(self):
        faltas = [["Brasil", "Italia", [10, 9]], 
                ["Brasil", "Espanha", [5, 7]], 
                ["Italia", "Espanha", [7, 8]]]

        total_faltas = {}

        for jogo in faltas:
            time1, time2, (faltas_time1, faltas_time2) = jogo
            
            if time1 in total_faltas:
                total_faltas[time1] += faltas_time1
            else:
                total_faltas[time1] = faltas_time1
            
            if time2 in total_faltas:
                total_faltas[time2] += faltas_time2
            else:
                total_faltas[time2] = faltas_time2

        total_campeonato = sum(total_faltas.values())
        print(f"Total de faltas do campeonato: {total_campeonato}")

        time_mais_faltas = max(total_faltas, key=total_faltas.get)
        print(f"Time que fez mais faltas: {time_mais_faltas} com {total_faltas[time_mais_faltas]} faltas")

        time_menos_faltas = min(total_faltas, key=total_faltas.get)
        print(f"Time que fez menos faltas: {time_menos_faltas} com {total_faltas[time_menos_faltas]} faltas")
        
    def __init__(self):
        funcoes=[self.a1,self.a2,self.a3,self.a4,self.a5,self.a6,self.a7,self.a8,self.a9,self.a10,self.a11,self.a12,self.a13]
        n=1
        for i in funcoes:
            print(f"Atividade {n}:")
            i()
            print("\n")
            n+=1