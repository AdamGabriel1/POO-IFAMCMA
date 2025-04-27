from Calendario import Calendario

cal = Calendario(2024,None,None,1)

cal.add_evento(1,"Teste1")
cal.add_evento(2,"Teste2")
cal.rm_evento(1, "Teste1")

cal.visu_eventos(2)
cal.visu_mes("Janeiro")
cal.visu_ano()

cal.verif_feriado(2)

cal.proximo_dia(2024, "Fevereiro", 28)

cal.mostrar_meses_por_periodo("bimestre")
cal.mostrar_meses_por_periodo("trimestre")
cal.mostrar_meses_por_periodo("semestre")

cal.mostrar_calendario_xml()