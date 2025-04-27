from Interface.OperacaoMatematica import OperacaoMatematica

class Divisao(OperacaoMatematica):
    def calcula(self, a: int, b: int):
        divisao=a/b
        print(f"A divisão de A / B é: {divisao}")