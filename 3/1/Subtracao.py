from Interface.OperacaoMatematica import OperacaoMatematica

class Subtracao(OperacaoMatematica):
    def calcula(self, a: int, b: int):
        subtracao=a-b
        print(f"A subtração de A - B é: {subtracao}")