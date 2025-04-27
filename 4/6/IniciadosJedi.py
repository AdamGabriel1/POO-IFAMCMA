class IniciadoJedi:
    def __init__(self,nome: str,especie: str,anoNascimento: int):
        self.nome=nome
        self.especie=especie
        self.anoNascimento=anoNascimento

    def getDescricao(self):
        return f"{self.nome} (especie={self.especie}, nascimento={self.getAnoNascimento()})"

    def getAnoNascimento(self):
        if self.anoNascimento<0:
            saida = str(self.anoNascimento) + "DBY"
        
        else:
            saida = str(self.anoNascimento) + "ABY"
        
        return saida