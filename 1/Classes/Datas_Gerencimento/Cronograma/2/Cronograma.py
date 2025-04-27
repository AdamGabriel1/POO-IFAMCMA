class Cronograma:
    def __init__(self):
        self.lista = ["Escola"]
        self.horarios = list(range(1, 25))
        self.datas = list(range(1, 31))
        self.dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        self.semanas = list(range(1, 5))
        self.meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"]
        self.bimestre = list(range(1, 5))

    def add_item_lista(self, item):
        self.lista.append(item)
        print(f"{item} adicionado à lista.")

    def rm_item_lista(self, item):
        if item in self.lista:
            self.lista.remove(item)
            print(f"{item} removido da lista.")
        else:
            print(f"{item} não encontrado na lista.")

    def mostrar_lista(self):
        print("Itens na lista:")
        for item in self.lista:
            print(item)

    def add_horario(self, novo_horario):
        if novo_horario not in self.horarios:
            self.horarios.append(novo_horario)
            print(f"Horário {novo_horario} adicionado.")
        else:
            print("Horário já existe na lista.")

    def rm_horario(self, horario):
        if horario in self.horarios:
            self.horarios.remove(horario)
            print(f"Horário {horario} removido.")
        else:
            print("Horário não encontrado.")

    def mostrar_dias_semana(self):
        print("Dias da semana:")
        for dia in self.dias_semana:
            print(dia)

    def mostrar_meses(self):
        print("Meses:")
        for mes in self.meses:
            print(mes)

    def add_data(self, nova_data):
        if nova_data not in self.datas:
            self.datas.append(nova_data)
            print(f"Data {nova_data} adicionada.")
        else:
            print("Data já existe na lista.")

    def rm_data(self, data):
        if data in self.datas:
            self.datas.remove(data)
            print(f"Data {data} removida.")
        else:
            print("Data não encontrada.")

    def opcs(self):
        while True:
            print("|===============================|")
            print("|          Cronograma           |")
            print("|1. Adicionar item à lista\t|")
            print("|2. Remover item da lista\t|")
            print("|3. Mostrar itens da lista\t|")
            print("|4. Adicionar horário\t\t|")
            print("|5. Remover horário\t\t|")
            print("|6. Mostrar dias da semana\t|")
            print("|7. Mostrar meses\t\t|")
            print("|8. Adicionar data\t\t|")
            print("|9. Remover data\t\t|")
            print("|0. Sair\t\t\t|")
            print("|===============================|")
            escolha = input("Escolha a opção desejada: ")

            match escolha:
                case "0":
                    print("Saindo do menu.")
                    break

                case "1":
                    item = input("Insira o item que deseja adicionar à lista: ")
                    self.add_item_lista(item)

                case "2":
                    item = input("Insira o item que deseja remover da lista: ")
                    self.rm_item_lista(item)

                case "3":
                    self.mostrar_lista()

                case "4":
                    horario = int(input("Insira o novo horário: "))
                    self.add_horario(horario)

                case "5":
                    horario = int(input("Insira o horário que deseja remover: "))
                    self.rm_horario(horario)

                case "6":
                    self.mostrar_dias_semana()

                case "7":
                    self.mostrar_meses()

                case "8":
                    nova_data = int(input("Insira a nova data: "))
                    self.add_data(nova_data)

                case "9":
                    data = int(input("Insira a data que deseja remover: "))
                    self.rm_data(data)

                case _:
                    print("Opção inválida. Escolha novamente.")

