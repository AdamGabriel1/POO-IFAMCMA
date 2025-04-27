class IniciadoJedi:
    def __init__(self,nome: str,especie: str,anoNascimento: int):
        self.nome=nome
        self.especie=especie
        self.anoNascimento=anoNascimento

    def getDescricao(self):
        return f"{self.nome} (especie={self.especie}, nascimento={self.getAnoNascimento()})"

    def getAnoNascimento(self):
        if self.anoNascimento<0:
            saida = f"{self.anoNascimento} DBY"
        
        else:
            saida = f"{self.anoNascimento} ABY"
        
        return saida

class TreinadorJedi:
    def __init__(self,titulacao: str, nome: str):
        self.titulacao=titulacao
        self.nome=nome

    def getDescricao(self):
        return f"{self.titulacao} {self.nome}"
    
class SessaoJedi:
    def __init__(self,nome: str, treinador: TreinadorJedi):
        self.nome=nome
        self.treinador=treinador
        self.iniciados=[]

    def addIniciado(self,iniciado: str):
            self.iniciados.append(iniciado)

    def getIniciado(self,nome: str):
        for i in self.iniciados:
            if nome==i:
                return i.nome

        return None

    def getMediaAnoNascimento(self):
        media=0
        i=0
        for iniciados in self.iniciados:
            media=iniciados.anoNascimento+media
            i=i+1
        media=media/i
        return media

    def getDescricao(self):
        saida=f"--> SESSÃO {self.nome} (Treinador: {self.treinador.getDescricao()})"
        for iniciados in self.iniciados:
            saida=f"{saida}\n - Iniciado: {iniciados.getDescricao()}"

        return saida
    
treinador=TreinadorJedi("Grão Mestre","Fae Coven")
iniciado1=IniciadoJedi("Katooni","Tholothian",23)
iniciado2=IniciadoJedi("Byph","Ithorian",21)
iniciado3=IniciadoJedi("Gungi","Wookiee",23)
iniciado4=IniciadoJedi("Petro","Human",22)
sessaojedi=SessaoJedi("Instruções de Uso da Força",treinador)

sessaojedi.addIniciado(iniciado1)
sessaojedi.addIniciado(iniciado2)
sessaojedi.addIniciado(iniciado3)
sessaojedi.addIniciado(iniciado4)

print(sessaojedi.getIniciado(iniciado1))
print(sessaojedi.getIniciado(iniciado2))
print(sessaojedi.getIniciado(iniciado3))
print(sessaojedi.getIniciado(iniciado4))
print(sessaojedi.getIniciado("sla"))

print(sessaojedi.getMediaAnoNascimento())

print(sessaojedi.getDescricao())
