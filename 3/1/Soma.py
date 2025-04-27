from Interface.OperacaoMatematica import OperacaoMatematica

class Soma(OperacaoMatematica):
    def calcula(self, a: int, b: int):
        soma=a+b
        print(f"A soma de A + B é: {soma}")