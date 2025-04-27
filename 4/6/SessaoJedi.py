from TreinadorJedi import TreinadorJedi
from IniciadosJedi import IniciadoJedi

class SessaoJedi:
    def __init__(self,nome: str, treinador: TreinadorJedi):
        self.nome=nome
        self.treinador=treinador
        self.iniciados=[]

    def addIniciado(self,iniciado):
        self.iniciados.append(iniciado)

    def getIniciado(self):
        for iniciados in self.iniciados:
            print(iniciados.getDescricao())

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