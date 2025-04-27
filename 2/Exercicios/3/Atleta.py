class Atleta:
    def __init__(self, aposentado, peso):
        self.aposentado=aposentado
        self.peso=peso

    def aposentar(self):
        self.aposentado=True

    def aquecer(self):
        print(f"{__name__} está aquecendo")
