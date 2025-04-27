class GerenciadorDeDados(ABC):
    def __init__(self):
        self.itens = []
        self.horarios = list(range(1, 25))
        self.datas = list(range(1, 31))
        self.dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        self.meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
                      "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    @abstractmethod
    def add_item(self, item):
        pass

    @abstractmethod
    def rm_item(self, item):
        pass

    @abstractmethod
    def mostrar_itens(self):
        pass

    @abstractmethod
    def visu_mes(self, mes):
        pass

    @abstractmethod
    def visu_ano(self):
        pass

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

    def determinar_dia_da_semana(self, ano, mes, dia):
        if mes < 3:
            mes += 12
            ano -= 1
        k = ano % 100
        j = ano // 100
        dia_da_semana = (dia + 13*(mes+1)//5 + k + k//4 + j//4 + 5*j) % 7
        return (dia_da_semana + 6) % 7

    def dias_num_mes(self, mes, ano):
        dias_por_mes = {
            "Janeiro": 31, "Fevereiro": 28, "Março": 31, "Abril": 30, "Maio": 31, "Junho": 30,
            "Julho": 31, "Agosto": 31, "Setembro": 30, "Outubro": 31, "Novembro": 30, "Dezembro": 31
        }
        if mes == "Fevereiro" and self.eh_bissexto(ano):
            return 29
        return dias_por_mes[mes]

    def eh_bissexto(self, ano):
        return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

    def proximo_dia(self, ano, mes, dia):
        mes_idx = self.meses.index(mes) + 1
        dia += 1

        if dia > self.dias_num_mes(mes, ano):
            dia = 1
            mes_idx += 1
            if mes_idx > 12:
                mes_idx = 1
                ano += 1

        return ano, mes_idx, dia

class Calendario(GerenciadorDeDados):
    def __init__(self, ano, feriados=None, eventos=None, p_dia_da_semana="Segunda"):
        super().__init__()
        self.ano = ano
        self.p_dia_da_semana = p_dia_da_semana
        
        self.bimestres_num_ano = list(range(1, 7))
        self.trimestres_num_ano = list(range(1, 5))
        self.semestres_num_ano = list(range(1, 3))
        self.meses_de_um_bimestre = list(range(1, 3))
        self.meses_de_um_trimestre = list(range(1, 4))
        self.meses_de_um_semestre = list(range(1, 7))
        
        self.feriados = feriados or {}
        self.eventos = eventos or {}

    def add_item(self, item):
        pass

    def rm_item(self, item):
        pass

    def mostrar_itens(self):
        pass

    def add_evento(self, data, evento):
        self.eventos.setdefault(data, []).append(evento)

    def rm_evento(self, data, evento):
        eventos = self.eventos.get(data)
        if eventos and evento in eventos:
            eventos.remove(evento)
            if not eventos:
                del self.eventos[data]
        else:
            print("Evento não encontrado.")

    def visu_eventos(self, data):
        eventos = self.eventos.get(data, [])
        if eventos:
            print(f"Eventos em {data}:")
            for evento in eventos:
                print(evento)
        else:
            print("Nenhum evento encontrado para esta data.")

    def verif_feriado(self, data):
        feriado = self.feriados.get(data)
        if feriado:
            print(f"{data} é feriado: {feriado}")
        else:
            print(f"{data} não é feriado.")

    def visu_mes(self, mes):
        if mes in self.meses:
            print(f"Calendário para o mês de {mes}:")
            dias_no_mes = self.dias_num_mes(mes, self.ano)
            dia_inicio = self.determinar_dia_da_semana(self.ano, self.meses.index(mes) + 1, 1)
            print(" " * (3 * dia_inicio), end="")
            for dia in range(1, dias_no_mes + 1):
                print(f"{dia:2}", end=" ")
                if (dia + dia_inicio) % 7 == 0:
                    print()
            print()

    def visu_ano(self):
        print(f"Calendário para o ano de {self.ano}:")
        for mes in self.meses:
            self.visu_mes(mes)
            
    def determinar_ultimo_dia_mes_anterior(self, mes, ano):
        mes_anterior = self.meses[(self.meses.index(mes) - 1) % 12]
        return self.dias_num_mes(mes_anterior, ano)
            
    def mostrar_meses_por_periodo(self, periodo):
        if periodo == "bimestre":
            periodos = self.bimestres_num_ano
            meses_por_periodo = self.meses_de_um_bimestre
        elif periodo == "trimestre":
            periodos = self.trimestres_num_ano
            meses_por_periodo = self.meses_de_um_trimestre
        elif periodo == "semestre":
            periodos = self.semestres_num_ano
            meses_por_periodo = self.meses_de_um_semestre
        else:
            print("Período inválido. Escolha entre 'bimestre', 'trimestre' ou 'semestre'.")
            return

        for periodo_num in periodos:
            print(f"{periodo.capitalize()} {periodo_num}:")
            for mes_num in meses_por_periodo:
                mes = self.meses[(periodo_num - 1) * len(meses_por_periodo) + mes_num - 1]
                print(mes)
            print()
            
    def mostrar_calendario_xml(self):
        xml = "<Calendario>\n"
        dias_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

        for mes in self.meses:
            xml += f"  <Mes>\n    <Nome>{mes}</Nome>\n"
            xml += "    <Semanas>\n"

            dia_inicio = self.determinar_dia_da_semana(self.ano, self.meses.index(mes) + 1, 1)

            if dia_inicio != 0:
                dia_anterior = self.determinar_ultimo_dia_mes_anterior(mes, self.ano)
                dias_mes_anterior = dia_anterior - dia_inicio + 1
                for i in range(dia_inicio):
                    xml += f"\t| {dias_semana[i]} {dias_mes_anterior + i} "

            dia_atual = 1
            while dia_atual <= self.dias_num_mes(mes, self.ano):
                xml += f"\t| {dias_semana[(dia_inicio + dia_atual - 1) % 7]} {dia_atual} "
                if (dia_inicio + dia_atual) % 7 == 0:
                    xml += "|\n"
                dia_atual += 1

            if (dia_inicio + dia_atual - 1) % 7 != 0:
                dias_mes_posterior = 7 - (dia_inicio + dia_atual - 1) % 7
                for i in range(dias_mes_posterior):
                    xml += f"\t| {dias_semana[(dia_inicio + dia_atual + i - 1) % 7]} {i + 1} "

            xml += "\n    <Semanas>\n  </Mes>\n"

        xml += "</Calendario>"
        with open('calendario_xml.txt', 'w') as arquivo:
            arquivo.write(xml)
        print("Abra o arquivo 'calendario_xml.txt' para ver o Calendario em XML.")
        print(xml)

class Cronograma(GerenciadorDeDados):
    def __init__(self):
        super().__init__()

    def add_item(self, item):
        self.itens.append(item)
        print(f"{item} adicionado à lista.")

    def rm_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            print(f"{item} removido da lista.")
        else:
            print(f"{item} não encontrado na lista.")

    def mostrar_itens(self):
        print("Itens na lista:")
        for item in self.itens:
            print(item)

    def visu_mes(self, mes):
        pass

    def visu_ano(self):
        pass

    def opcs(self):
        opcoes = {
            "0": "Sair",
            "1": "Adicionar item à lista",
            "2": "Remover item da lista",
            "3": "Mostrar itens da lista",
            "4": "Adicionar horário",
            "5": "Remover horário",
            "6": "Mostrar dias da semana",
            "7": "Mostrar meses",
            "8": "Adicionar data",
            "9": "Remover data"
        }

        while True:
            print("|===============================|")
            for key, value in opcoes.items():
                print(f"|{key}. {value}\t\t|")
            print("|===============================|")

            escolha = input("Escolha a opção desejada: ")

            match escolha:
                case "0":
                    print("Saindo do menu.")
                    break
                case "1":
                    item = input("Insira o item que deseja adicionar à lista: ")
                    self.add_item(item)
                case "2":
                    item = input("Insira o item que deseja remover da lista: ")
                    self.rm_item(item)
                case "3":
                    self.mostrar_itens()
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