from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

    @abstractmethod
    def descricao(self):
        pass

    @abstractmethod
    def disponibilidade(self):
        pass

class Livro(Item):
    def __init__(self, titulo, ano, autor, num_paginas):
        super().__init__(titulo, ano)
        self.autor = autor
        self.num_paginas = num_paginas
        self.emprestado = False

    def descricao(self):
        return f"Livro: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Páginas: {self.num_paginas}"

    def disponibilidade(self):
        return "Disponível" if not self.emprestado else "Emprestado"

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            return f"Livro '{self.titulo}' emprestado com sucesso."
        else:
            return f"Livro '{self.titulo}' já está emprestado."

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            return f"Livro '{self.titulo}' devolvido com sucesso."
        else:
            return f"Livro '{self.titulo}' não estava emprestado."

class Revista(Item):
    def __init__(self, titulo, ano, volume):
        super().__init__(titulo, ano)
        self.volume = volume

    def descricao(self):
        return f"Revista: {self.titulo}, Volume: {self.volume}, Ano: {self.ano}"

    def disponibilidade(self):
        return "Disponível na biblioteca"

class DVD(Item):
    def __init__(self, titulo, ano, duracao):
        super().__init__(titulo, ano)
        self.duracao = duracao
        self.emprestado = False

    def descricao(self):
        return f"DVD: {self.titulo}, Duração: {self.duracao} minutos, Ano: {self.ano}"

    def disponibilidade(self):
        return "Disponível" if not self.emprestado else "Emprestado"

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            return f"DVD '{self.titulo}' emprestado com sucesso."
        else:
            return f"DVD '{self.titulo}' já está emprestado."

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            return f"DVD '{self.titulo}' devolvido com sucesso."
        else:
            return f"DVD '{self.titulo}' não estava emprestado."

# Exemplo de uso:
livro = Livro("O Senhor dos Anéis", 1954, "J.R.R. Tolkien", 1178)
revista = Revista("National Geographic", 2023, 7)
dvd = DVD("Matrix", 1999, 136)

print(livro.descricao())
print(livro.disponibilidade())
print(livro.emprestar())
print(livro.disponibilidade())

print(revista.descricao())
print(revista.disponibilidade())

print(dvd.descricao())
print(dvd.disponibilidade())
print(dvd.emprestar())
print(dvd.disponibilidade())
