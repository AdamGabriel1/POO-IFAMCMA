class Calendario:
    def __init__(self, ano, feriados, eventos, p_dia_da_semana):
        self.ano = ano
        self.meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        self.dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
        self.p_dia_da_semana = p_dia_da_semana

        # Outros
        self.bimestres_num_ano = list(range(1, 7))
        self.trimestres_num_ano = list(range(1, 5))
        self.semestres_num_ano = list(range(1, 3))
        self.meses_de_um_bimestre = list(range(1, 3))
        self.meses_de_um_trimestre = list(range(1, 4))
        self.meses_de_um_semestre = list(range(1, 7))

        self.feriados = feriados if feriados else {}
        self.eventos = eventos if eventos else {}

    def add_evento(self, data, evento):
        if data in self.eventos:
            self.eventos[data].append(evento)
        else:
            self.eventos[data] = [evento]

    def rm_evento(self, data, evento):
        if data in self.eventos and evento in self.eventos[data]:
            self.eventos[data].remove(evento)
            if not self.eventos[data]:
                del self.eventos[data]
        else:
            print("Evento não encontrado.")

    def visu_eventos(self, data):
        if data in self.eventos:
            print(f"Eventos em {data}:")
            for evento in self.eventos[data]:
                print(evento)
        else:
            print("Nenhum evento encontrado para esta data.")

    def visu_mes(self, mes):
        if mes in self.meses:
            print(f"Calendário para o mês de {mes}:")
            self.dias_no_mes = 31 if mes in ["Janeiro", "Março", "Maio", "Julho", "Agosto", "Outubro", "Dezembro"] else 30
            if mes == "Fevereiro":
                self.dias_no_mes = 29 if self.eh_bissexto(self.ano) else 28

            dia_inicio = self.determinar_dia_da_semana(self.ano, self.meses.index(mes) + 1, 1)
            print(" " * (3 * dia_inicio), end="")
            for dia in range(1, self.dias_no_mes + 1):
                print(f"{dia:2}", end=" ")
                if (dia + dia_inicio) % 7 == 0:
                    print()
            print()

    def visu_ano(self):
        print(f"Calendário para o ano de {self.ano}:")
        for mes in self.meses:
            self.visu_mes(mes)

    def verif_feriado(self, data):
        if data in self.feriados:
            print(f"{data} é feriado: {self.feriados[data]}")
        else:
            print(f"{data} não é feriado.")

    def proximo_dia(self, ano, mes, dia):
        mes_idx = self.meses.index(mes) + 1
        dia += 1

        if dia > self.dias_num_mes(self.meses[mes_idx - 1], ano):
            mes_idx += 1
            dia = 1
            if mes_idx > 12:
                mes_idx = 1
                ano += 1

        return ano, mes_idx, dia

    def determinar_dia_da_semana(self, ano, mes, dia):
        if mes < 3:
            mes += 12
            ano -= 1
        k = ano % 100
        j = ano // 100
        dia_da_semana = (dia + 13*(mes+1)//5 + k + k//4 + j//4 + 5*j) % 7
        return (dia_da_semana + 6) % 7

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

    def dias_num_mes(self, mes, ano):
        dias_por_mes = {
            "Janeiro": 31, "Fevereiro": 28, "Março": 31, "Abril": 30, "Maio": 31, "Junho": 30,
            "Julho": 31, "Agosto": 31, "Setembro": 30, "Outubro": 31, "Novembro": 30, "Dezembro": 31
        }
        if self.eh_bissexto(ano) and mes == "Fevereiro":
            return 29
        else:
            return dias_por_mes[mes]

    def eh_bissexto(self, ano):
        return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)
