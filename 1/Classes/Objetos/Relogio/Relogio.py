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

    def data(self):
        print(f"Dia: {self.dia}\nMês: {self.mes}\nAno: {self.ano}")

    def horario(self):
        print(f"Segundos: {self.seg}\nMinutos: {self.min}\nHora: {self.hora}")

    def seg_min(self):
        seg2=input("Diga de quantos segundos você quer transformar para minutos: ")
        r=(int(seg2)*60)
        print(f"De {seg2} segundos foram possiveis calcular {r} minutos")

    def min_seg(self):
        min2=input("Diga de quantos minutos você quer transformar para segundos: ")
        r=(int(min2)/60)
        print(f"De {min2} minutos foram possiveis calcular {r} segundos")

    def seg_hora(self):
        seg2=input("Diga de quantos segundos você quer transformar para horas: ")
        r=(int(seg2)*3600)
        print(f"De {seg2} segundos foram possiveis calcular {r} horas")
    
    def hora_seg(self):
        hora2=input("Diga de quantos horas você quer transformar para segundos: ")
        r=(int(hora2)/3600)
        print(f"De {hora2} horas foram possiveis calcular {r} segundos")
        self.hora/3600

    def ano_bissesto(self):
        self.mes=input("Diga o nome do Mês que você quer saber os dias: ")
        if self.mes=="Janeiro":
            self.diasdomes=31
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")
            
        elif self.mes=="Fevereiro":
            self.diasdomes=29
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")

        elif self.mes=="Março":
            self.diasdomes=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")

        elif self.mes=="Abril":
            self.diasdomes=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")

        elif self.mes=="Maio":
            self.diasdomes=31
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")
            
        elif self.mes=="Junho":
            self.diasdomes=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")

        elif self.mes=="Julho":
            self.diasdomes=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")
            
        elif self.mes=="Agosto":
            self.diasdomes=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")
            
        elif self.mes=="Setembro":
            self.diasdomes=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")
            
        elif self.mes=="Outubro":
            self.diasdomes=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")

        elif self.mes=="Novembro":
            self.diasdomes=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")
            
        elif self.mes=="Dezembro":
            self.diasdomes=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")

        else:
            print("Mês errado tente novamente.")
            self.ano_bissesto()

    def ano_normal(self):
        self.mes=input("Diga o nome do Mês que você quer saber os dias: ")
        if self.mes=="Janeiro":
            self.diasdomes=31
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")
            
        elif self.mes=="Fevereiro":
            self.diasdomes=28
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")

        elif self.mes=="Março":
            self.diasdomes=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")

        elif self.mes=="Abril":
            self.diasdomes=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")

        elif self.mes=="Maio":
            self.diasdomes=31
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")
            
        elif self.mes=="Junho":
            self.diasdomes=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")

        elif self.mes=="Julho":
            self.diasdomes=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")
            
        elif self.mes=="Agosto":
            self.diasdomes=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")
            
        elif self.mes=="Setembro":
            self.diasdomes=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")
            
        elif self.mes=="Outubro":
            self.diasdomess=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")

        elif self.mes=="Novembro":
            self.diasdomes=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")
            
        elif self.mes=="Dezembro":
            self.diasdomes=30
            print(f"O Mês: {self.mes} tem {self.diasdomes} dias.")

        else:
            print("Mês errado tente novamente.")
            self.ano_normal()

    def dia_mes(self):
        ab=input("O ano é um ano Bissesto: ")
        if ab=="Sim":
            self.ano_bissesto()
        else:
            self.ano_normal()

    def q_ano(self):
        dia_a=input("Diga quantos dias tem esse ano: ")
        if dia_a==366:
            print(f"Ele é um ano Bissesto pois tem: {dia_a}")
        else:
            print(f"Ele é um ano Normal pois tem: {dia_a}")

    def mes_dia(self):
        ab=input("O ano é um ano Bissesto: ")
        if ab=="Sim":
            self.ano_bissesto()
        else:
            self.ano_normal()

    def ano_dia(self):
        dia_a=input("Diga de quantos anos você quer calcular para dias: ")
        ano_c=input("Você quer calcular com base em anos Bissestos ou anos normais: ")
        if ano_c=="Bissesto":
            r=dia_a*366
            print(f"O resultado é que são {r} anos Bissestos.")
        else:
            r=dia_a*365
            print(f"O resultado é que são {r} anos normais.")

    def dia_ano(self):
        dia_a=input("Diga de quantos dias você quer calcular para ano: ")
        ano_c=input("Você quer calcular com base em anos Bissestos ou anos normais: ")
        if ano_c=="Bissesto":
            r=dia_a/366
            print(f"O resultado é que são {r} dias em anos Bissestos.")
        else:
            r=dia_a/365
            print(f"O resultado é que são {r} dias em anos normais.")

    def verificar_metodo(self):
        while True:
            self.tabela()
            f=input("Fale a Função que voce quer usar: ")
            print(f"A Função que você escolheu foi: {f}")
            if f=="0":
                print("Fim do Programa.")
                break

            elif f=="1":
                self.data()
            
            elif f=="2":
                self.horario()
        
            elif f=="3":
                self.seg_min()
        
            elif f=="4":
                self.min_seg()
        
            elif f =="5":
                self.seg_hora()
        
            elif f=="6":
                self.hora_seg()
            
            elif f=="7":
                self.dia_mes()
            
            elif f=="8":
                self.q_ano()
        
            elif f=="9":
                self.mes_dia()
        
            elif f=="10":
                self.ano_dia()
        
            elif f=="11":
                self.dia_ano()
        
            else:
                print("Função errada tente novamente:")
                self.verificar_metodo()

    def tabela(self):
        print("|=============================|")
        print("|           Funções           |")
        print("|1. Data                      |")
        print("|2. Horario                   |")
        print("|3. Seg para Min              |")
        print("|4. Min para Seg              |")
        print("|5. Seg para hora             |")
        print("|6. Hora para Seg             |")
        print("|7. Dia para Mês              |")
        print("|8. Quantos dias tem esse ano |")
        print("|9. Mês para dia              |")
        print("|10. Ano para dia             |")
        print("|11. Dia para ano             |")
        print("|0. Sair                      |")
        print("|=============================|")

