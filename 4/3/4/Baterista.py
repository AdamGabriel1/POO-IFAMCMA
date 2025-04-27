class Baterista:
    def __init__(self):
        self.saxofonista = []
    
    def add_saxofonista(self,saxofonista):
        self.saxofonista.append(saxofonista)
    
    def toca_com(self):
        for classe in self.saxofonista:
            print(f"{classe} toca com Baterista")
