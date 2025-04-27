try:
    f = open('arquivo_inexistente.txt', 'r')
except FileNotFoundError:
    print("Erro: Arquivo não encontrado!")
print("... continua o programa")