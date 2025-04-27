from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self,nome,salario):
        self.nome=nome
        self.salario=salario

    def getNome(self):
        return self.nome

    def setNome(self,nome):
        self.nome=nome

    def getSalario(self):
        return self.salario

    def setSalario(self,salario):
        self.salario=salario    

    @abstractmethod
    def aumentaSalario(self):
        pass

class Gerente(Funcionario):
    def __init__(self,nome,salario):
        super().__init__(nome,salario)

    def aumentaSalario(self):
        self.salario=(self.salario*1.10)

class Programador(Funcionario):
    def __init__(self,nome,salario):
        super().__init__(nome,salario)
        
    def aumentaSalario(self):
        self.salario=(self.salario*1.20)

class Menu:
    def __init__(self) -> None:
        pass
        
    def menu(self):
        while True:
            print("="*50)
            print("Escolha o que você deseja fazer")
            print("1. Imprimir dados")
            print("2. Aumentar salário")
            print("0. Sair")
            print("="*50)
            i=input("Insira a sua escolha: ")
            match i:
                case "1":
                    print("="*50)
                    print("qual Funcionario você deseja imprimir os dados")
                    print("1. Gerente")
                    print("2. Programador")
                    print("0. Sair")
                    print("="*50)
                    c=input("Insira a sua escolha: ")
                    match c:
                        case "1":
                            print("Dados do Gerente:")
                            print(func1.getNome())
                            print(func1.getSalario())

                        case "2":
                            print("Dados do Programador:")
                            print(func2.getNome())
                            print(func2.getSalario())

                        case "0":
                            break

                        case _:
                            print("Tente novamente.")

                case "2":
                    print("="*50)
                    print("Escolha de qual Funcionario você deseja aumentar o salario")
                    print("1. Gerente")
                    print("2. Programador")
                    print("0. Sair")
                    print("="*50)
                    c=input("Insira a sua escolha: ")
                    match c:
                        case "1":
                            func1.aumentaSalario()
                            print(func1.getSalario())

                        case "2":
                            func2.aumentaSalario()
                            print(func2.getSalario())

                        case "0":
                            break

                        case _:
                            print("Tente novamente.")

                case "0":
                    break

                case _:
                    print("Tente novamente.")

func1=Gerente("João Matheus",1000.0)
func2=Programador("Adam",1000)

menu1=Menu()
menu1.menu()