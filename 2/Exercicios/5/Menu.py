from CartaodeCredito import *
from CartaodeDebito import *
from Pix import *
from Boleto import *

class Menu:
    def __init__(self) -> None:
        pass

    def menu(self):
        while True:
            print("="*50)
            print("Opções de Pagamento:")
            print("1. Cartão de Crédito")
            print("2. Cartão de Débito")
            print("3. Pix")
            print("4. Boleto")
            print("0. Sair")
            print("="*50)
            i=input("Insira a sua escolha: ")
            match i:
                case "1":
                    c1=CartaodeCredito("José","Mastercard","Cartão de Crédito",1000.0,True,10,100)
                    c1.info()

                case "2":
                    c2=CartaodeDebito("Maria","Mastercard Maestro","Cartão de Crédito",2000.0,True,10,200)
                    c2.info()

                case "3":
                    c3=Pix("Nicolas","Pix",5000.0,False)
                    c3.info()

                case "4":
                    c4=Boleto("Marcos","Boleto",3000.0,False)
                    c4.info()

                case "0":
                    break

                case _:
                    print("Tente novamente.")