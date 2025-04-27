class CalendarioXML:
    def __init__(self, ano, p_dia_da_semana):
        self.ano = ano
        self.p_dia_da_semana = p_dia_da_semana
        self.meses = [
            "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
            "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
        ]

    def eh_bissexto(self):
        return self.ano % 4 == 0 and (self.ano % 100 != 0 or self.ano % 400 == 0)

    def dias_no_mes(self, mes):
        dias_por_mes = {
            "Janeiro": 31, "Fevereiro": 28, "Março": 31, "Abril": 30, "Maio": 31, "Junho": 30,
            "Julho": 31, "Agosto": 31, "Setembro": 30, "Outubro": 31, "Novembro": 30, "Dezembro": 31
        }
        if self.eh_bissexto() and mes == "Fevereiro":
            return 29
        else:
            return dias_por_mes[mes]

    def mostrar_calendario_xml(self):
        xml = "<Calendario>\n"
        dias_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

        dia_inicio = self.p_dia_da_semana
        for mes in self.meses:
            xml += f"  <Mes>\n    <Nome>{mes}</Nome>\n"
            xml += "    <Semanas>\n"

            # Adiciona os dias finais do mês anterior no início do mês atual
            dia_anterior = self.dias_no_mes(self.meses[(self.meses.index(mes) - 1) % 12])
            dias_mes_anterior = (dia_anterior - dia_inicio + 1) if dia_inicio != 0 else 0

            for i in range(dia_inicio):
                xml += f"\t| {dias_semana[i]} {dias_mes_anterior + i} "

            dia_atual = 1
            while dia_atual <= self.dias_no_mes(mes):
                xml += f"\t| {dias_semana[(dia_inicio + dia_atual - 1) % 7]} {dia_atual} "
                if (dia_inicio + dia_atual) % 7 == 0:  # Final de semana
                    xml += "|\n"
                dia_atual += 1

            # Se o mês terminar antes do final da semana, armazena os dias que serão adicionados no próximo mês
            if (dia_inicio + dia_atual - 1) % 7 != 0:
                dias_mes_anterior = self.dias_no_mes(mes) - (dia_inicio + dia_atual - 1) % 7

            xml += "    </Semanas>\n  </Mes>\n"
            dia_inicio = (dia_inicio + dia_atual - 1) % 7

        xml += "</Calendario>"
        print(xml)


# Exemplo de uso:
calendario = CalendarioXML(2024, 1)  # Começando em uma segunda-feira
calendario.mostrar_calendario_xml()
