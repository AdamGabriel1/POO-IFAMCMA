from Interface.OperacaoMatematica import OperacaoMatematica

class Multiplicacao(OperacaoMatematica):
    def calcula(self, a: int, b: int):
        multiplicacao=a*b
        print(f"A multiplicação de A * B é: {multiplicacao}")