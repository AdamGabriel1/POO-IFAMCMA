from Soma import *
from Subtracao import *
from Multiplicacao import *
from Divisao import *

class Menu:
    def __init__(self) -> None:
        pass

    def menu(self):
        while True:
            print("="*50)
            print("Operações Matemáticas:")
            print("1. Soma")
            print("2. Subtração")
            print("3. Multiplicação")
            print("4. Divisão")
            print("0. Sair")
            print("="*50)
            i=input("Insira a sua escolha: ")
            match i:
                case "1":
                    som1=Soma()
                    som1.calcula(10,50)

                case "2":
                    sub1=Subtracao()
                    sub1.calcula(50,30)

                case "3":
                    mult1=Multiplicacao()
                    mult1.calcula(10,10)

                case "4":
                    div1=Divisao()
                    div1.calcula(10,5)

                case "0":
                    break

                case _:
                    print("Tente novamente.")