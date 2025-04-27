class Pilha:
    def __init__(self):
        self.items = []
    def empilhar(self, item):
        self.items.append(item)
    def desempilhar(self):
        assert len(self.items) > 0, "Não é possível desempilhar de uma pilha"
        return self.items.pop()
p = Pilha()
p.empilhar(1)
p.empilhar(5)
print(p.items)
print(p.desempilhar())
print(p.desempilhar())
print(p.items)
p.empilhar(3)
p.empilhar(2)
print(p.items)