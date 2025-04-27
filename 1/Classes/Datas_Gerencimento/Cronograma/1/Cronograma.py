class Cronograma:
    def __init__(self):
        self.lista = ["Escola"]
        self.horarios = list(range(1, 25))
        self.datas = list(range(1, 31))
        self.dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        self.semanas = list(range(1, 5))
        self.meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"]
        self.bimestres = list(range(1, 5))

    def adicionar_item_lista(self, item):
        self.lista.append(item)
        print(f"{item} adicionado à lista.")

    def remover_item_lista(self, item):
        if item in self.lista:
            self.lista.remove(item)
            print(f"{item} removido da lista.")
        else:
            print(f"{item} não encontrado na lista.")

    def mostrar_lista(self):
        print("Itens na lista:")
        for item in self.lista:
            print(item)

    def adicionar_horario(self, novo_horario):
        if novo_horario not in self.horarios:
            self.horarios.append(novo_horario)
            print(f"Horário {novo_horario} adicionado.")
        else:
            print("Horário já existe na lista.")

    def remover_horario(self, horario):
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

    def adicionar_data(self, nova_data):
        if nova_data not in self.datas:
            self.datas.append(nova_data)
            print(f"Data {nova_data} adicionada.")
        else:
            print("Data já existe na lista.")

    def remover_data(self, data):
        if data in self.datas:
            self.datas.remove(data)
            print(f"Data {data} removida.")
        else:
            print("Data não encontrada.")

