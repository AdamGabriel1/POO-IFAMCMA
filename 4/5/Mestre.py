class Mestre:
    def __init__(self,nome: str, anoNascimento: int, afiliacao: str, posto: str):
        self.nome=nome
        self.anoNascimento=anoNascimento
        self.afiliacao=afiliacao
        self.posto=posto

    def getIdade(self, anoReferencia: int):
        idade = anoReferencia - self.anoNascimento
        return idade

    def possuiForca(self):
        if self.posto=="Jedi" or self.posto=="Sith":
            return True
        
        else:
            return False
        
    def getAnoNascimentoString(self):
        if self.anoNascimento<0:
            saida = str(self.anoNascimento) + "ABY"
        
        else:
            saida = str(self.anoNascimento) + "DBY"
        
        return saida
        
    def getDescricao(self):
        saida = f"Mestre: nome={self.nome}, anoNascimento={self.getAnoNascimentoString()}, afiliacao={self.afiliacao}, posto={self.posto}, possuiForca={self.possuiForca()}"
        return saida
