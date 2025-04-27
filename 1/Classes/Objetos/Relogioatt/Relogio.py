class Relogio:
    def __init__(self,seg,min,hora,dia,mes,ano):
        self.seg=seg
        self.min=min
        self.hora=hora
        self.dia=dia
        self.mes=mes
        self.ano=ano
        self.ano_bi=366
        self.ano_no=365
        self.meses=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

    # Funções de Informações
    def data(self):
        print("\n|===============================|")
        print("|             Data              |")
        print(f"|Dia: {self.dia}\t\t\t|")
        print(f"|Mês: {self.mes}\t\t\t|")
        print(f"|Ano: {self.ano}\t\t\t|")
        print("|===============================|\n")

    def horario(self):
        print("\n|===============================|")
        print("|            Horario            |")
        print(f"|Segundos: {self.seg}\t\t\t|")
        print(f"|Minutos: {self.min}\t\t\t|")
        print(f"|Hora: {self.hora}\t\t\t|")
        print("|===============================|\n")

    def fmeses(self):
        print("\n|===============================|")
        print("|             Meses             |")
        for i in range(12):
            print(f"|{i+1}. {self.meses[i]}\t\t\t|")
        print("|===============================|\n")

    # Funções de Conversões
    def seg_min(self):
        seg2=input("Diga de quantos segundos você quer transformar para minutos: ")
        r=(int(seg2)/60)
        print(f"De {seg2} segundos foram possiveis calcular {r} minutos")

    def min_seg(self):
        min2=input("Diga de quantos minutos você quer transformar para segundos: ")
        r=(int(min2)*60)
        print(f"De {min2} minutos foram possiveis calcular {r} segundos")

    def min_hora(self):
        min2=input("Diga de quantos minutos você quer transformar para horas: ")
        r=(int(min2)/60)
        print(f"De {min2} minutos foram possiveis calcular {r} horas")

    def hora_min(self):
        hora2=input("Diga de quantas horas você quer transformar para minutos: ")
        r=(int(hora2)*60)
        print(f"De {hora2} horas foram possiveis calcular {r} minutos")

    def seg_hora(self):
        seg2=input("Diga de quantos segundos você quer transformar para horas: ")
        r=(int(seg2)/3600)
        print(f"De {seg2} segundos foram possiveis calcular {r} horas")

    def hora_seg(self):
        hora2=input("Diga de quantos horas você quer transformar para segundos: ")
        r=(int(hora2)*3600)
        print(f"De {hora2} horas foram possiveis calcular {r} segundos")

    def dia_mes(self):
        dia2=input("Diga de quantos dias você quer transformar para meses: ")
        r=(int(dia2)/30)
        print(f"De {dia2} dias foram possiveis calcular {r} meses")

    def mes_dia(self):
        mes2=input("Diga de quantos meses você quer transformar para dias: ")
        r=(int(mes2)*30)
        print(f"De {mes2} meses foram possiveis calcular {r} dias")

    def mes_ano(self):
        mes2=input("Diga de quantos meses você quer transformar para anos: ")
        r=(int(mes2)/12)
        print(f"De {mes2} meses foram possiveis calcular {r} anos")

    def ano_mes(self):
        ano2=input("Diga de quantos anos você quer transformar para meses: ")
        r=(int(ano2)*12)
        print(f"De {ano2} anos foram possiveis calcular {r} meses")

    def ano_dia(self):
        ano2=input("Diga de quantos anos você quer transformar para dias: ")
        r=((int(ano2)/12)/30)
        print(f"De {ano2} anos foram possiveis calcular {r} dias")

    def dia_ano(self):
        dia2=input("Diga de quantos dias você quer transformar para anos: ")
        r=((int(dia2)*12)*30)
        print(f"De {dia2} dias foram possiveis calcular {r} anos")

    def ano_dec(self):
        ano2=input("Diga de quantos anos você quer transformar para décadas: ")
        r=(int(ano2)/10)
        print(f"De {ano2} anos foram possiveis calcular {r} décadas")

    def dec_ano(self):
        dec2=input("Diga de quantas décadas você quer transformar para anos: ")
        r=(int(dec2)*10)
        print(f"De {dec2} décadas foram possiveis calcular {r} anos")

    def dec_sec(self):
        dec2=input("Diga de quantas décadas você quer transformar para séculos: ")
        r=(int(dec2)/10)
        print(f"De {dec2} décadas foram possiveis calcular {r} séculos")

    def sec_dec(self):
        sec2=input("Diga de quantos séculos você quer transformar para décadas: ")
        r=(int(sec2)*10)
        print(f"De {sec2} séculos foram possiveis calcular {r} décadas")

    def sec_ano(self):
        sec2=input("Diga de quantos séculos você quer transformar para anos: ")
        r=(int(sec2)*100)
        print(f"De {sec2} séculos foram possiveis calcular {r} anos")

    def ano_sec(self):
        ano2=input("Diga de quantos anos você quer transformar para séculos: ")
        r=(int(ano2)*100)
        print(f"De {ano2} anos foram possiveis calcular {r} séculos")

    # Funções de Verificações
    def vr_bissexto(self):
        ano2=int(input("Diga qual o ano que você quer saber se é Bissexto: "))
        if (ano2 % 4 == 0 and ano2 % 100 != 0) or (ano2 % 400 == 0):
            print(f"O ano {ano2} é bissexto.")
        else:
            print(f"O ano {ano2} é normal.")

    def vr_data_hora(self):
        hora2=int(input("Digite as horas: "))
        min2=int(input("Digite os minutos: "))
        seg2=int(input("Digite os segundos: "))
        if (0 <= hora2 < 24) and (0 <= min2 < 60) and (0 <= seg2 < 60):
            print("Data e hora corretas.")
        else:
            print("Data e hora incorretas.")

    def informacoes(self):
        while True:
            print("|===============================|")
            print("|          Informações          |")
            print("|1. Data                        |")
            print("|2. Horario                     |")
            print("|3. Meses                       |")
            print("|0. Sair                        |")
            print("|===============================|")
            con=input("Digite o número da Informação que você quer saber: ")
            if con=="0":
                self.all_f()
                break

            elif con=="1":
                self.data()

            elif con=="2":
                self.horario()

            elif con=="3":
                self.fmeses()

            else:
                print("Número errado tente novamente.")
                self.informacoes()

    def conversoes(self):
        while True:
            print("|==============================|")
            print("|          Conversões          |")
            print("|1. Seg para Min               |")
            print("|2. Min para Seg               |")
            print("|3. Min para Hora              |")
            print("|4. Hora para Min              |")
            print("|5. Seg para Hora              |")
            print("|6. Hora para Seg              |")
            print("|7. Dia para Mês               |")
            print("|8. Mês para Dia               |")
            print("|9. Mês para Ano               |")
            print("|10. Ano para Mês              |")
            print("|11. Ano para Dia              |")
            print("|12. Dia para Ano              |")
            print("|13. Ano para Década           |")
            print("|14. Década para Ano           |")
            print("|15. Década para Século        |")
            print("|16. Século para Década        |")
            print("|17. Século para Ano           |")
            print("|18. Ano para Século           |")
            print("|0. Sair                       |")
            print("|==============================|")
            con=input("Digite o número da Conversão que você quer fazer: ")
            if con=="0":
                self.all_f()
                break

            elif con=="1":
                self.seg_min()

            elif con=="2":
                self.min_seg()

            elif con=="3":
                self.min_hora()

            elif con=="4":
                self.hora_min()

            elif con=="5":
                self.seg_hora()

            elif con=="6":
                self.hora_seg()

            elif con=="7":
                self.dia_mes()

            elif con=="8":
                self.mes_dia()

            elif con=="9":
                self.mes_ano()

            elif con=="10":
                self.ano_mes()

            elif con=="11":
                self.ano_dia()

            elif con=="12":
                self.dia_ano()

            elif con=="13":
                self.ano_dec()

            elif con=="14":
                self.dec_ano()

            elif con=="15":
                self.dec_sec()

            elif con=="16":
                self.sec_dec()

            elif con=="17":
                self.sec_ano()

            elif con=="18":
                self.ano_sec()

            else:
                print("Número errado tente novamente.")
                self.conversoes()

    def verificacoes(self):
        while True:
            print("|======================================|")
            print("|             Verificações             |")
            print("|1. Se é ano Bissexto ou Normal        |")
            print("|2. Se a data e hora estão certas      |")
            print("|0. Sair                               |")
            print("|======================================|")
            con=input("Digite o número da Verificação que você quer fazer: ")
            if con=="0":
                self.all_f()
                break

            elif con=="1":
                self.vr_bissexto()

            elif con=="2":
                self.vr_data_hora()

            else:
                print("Número errado tente novamente.")
                self.verificacoes()

    def all_f(self):
        while True:
            print("|================================|")
            print("|        Todas as Funções        |")
            print("|1. Informações                  |")
            print("|2. Conversões                   |")
            print("|3. Verificações                 |")
            print("|0. Sair                         |")
            print("|================================|")
            con=input("Digite o número da Função que você quer usar: ")
            if con=="0":
                print("Fim do Programa.")
                break

            elif con=="1":
                self.informacoes()

            elif con=="2":
                self.conversoes()

            elif con=="3":
                self.verificacoes()

            else:
                print("Número errado tente novamente.")
                self.all_f()

