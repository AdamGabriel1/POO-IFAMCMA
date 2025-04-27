class TreinadorJedi:
    def __init__(self,titulacao: str, nome: str):
        self.titulacao=titulacao
        self.nome=nome

    def getDescricao(self):
        return f"{self.titulacao} {self.nome}"