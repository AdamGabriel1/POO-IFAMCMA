import json

class Celular:
    def __init__(self):
        # Carregar dados dos celulares a partir de um arquivo JSON
        with open("celulares.json") as file:
            self.celulares = json.load(file)

    def get_celular(self, modelo):
        return self.celulares.get(modelo)

    def listar_celulares(self):
        for modelo, celular in self.celulares.items():
            print(celular["DADOS GERAIS"]["Nome"])

    def especificacoes(self, modelo):
        celular = self.get_celular(modelo)
        if celular:
            print(f"\nEspecificações do Celular {modelo}: ")
            for chave, valor in celular.items():
                print(f"{chave.capitalize()}: {valor}")
            print("\n")
        else:
            print("Celular não encontrado.")

