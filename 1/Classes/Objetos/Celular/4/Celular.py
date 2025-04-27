class Celular:
    def __init__(self,dados_gerais,dados_tecnicos,bateria,tela,camera,video):
        self.dados_gerais=dados_gerais
        self.dados_tecnicos=dados_tecnicos
        self.bateria=bateria
        self.tela=tela
        self.camera=camera
        self.video=video

    def mostrar_especificacoes(self):
        print(f"\nEspecificações do Celular:")
        print("===================================")
        print("\nDados Gerais:")
        for chave, valor in self.dados_gerais.items():
            print(f"- {chave}: {valor}")
        print("\nDados Técnicos:")
        for chave, valor in self.dados_tecnicos.items():
            print(f"- {chave}: {valor}")
        print("\nBateria:")
        for chave, valor in self.bateria.items():
            print(f"- {chave}: {valor}")
        print("\nTela:")
        for chave, valor in self.tela.items():
            print(f"- {chave}: {valor}")
        print("\nCâmera:")
        for chave, valor in self.camera.items():
            print(f"- {chave}: {valor}")
        print("\nVídeo:")
        for chave, valor in self.video.items():
            print(f"- {chave}: {valor}")
        print("\n")

    def mostrar_opcoes():
        print("|================================|")
        print("|       Todos os Celulares       |")
        print("|1. S24 Ultra                    |")
        print("|2. A14 5G                       |")
        print("|3. Redmi 9A                     |")
        print("|4. Red Magic 9 Pro Plus         |")
        print("|5. Moto E7                      |")
        print("|0. Sair                         |")
        print("|================================|")

