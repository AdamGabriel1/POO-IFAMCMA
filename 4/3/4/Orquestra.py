class Orquestra:
    def __init__(self):
        self.musico = []
    
    def add_musico(self,musico):
        self.musico.append(musico)
    
    def toca_em(self):
        for classe in self.musico:
            print(f"{classe} toca em Orquestra")

