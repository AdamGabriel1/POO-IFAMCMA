from Classes import VIP
from Classes import Retangulo, Triangulo
from Classes import TriAtleta
from Classes import ContaCorrente, Poupanca, ContaImposto

# Exercício 1
vip1=VIP(5,10)
vip1.imprimeValor()

# Exercício 2
r1=Retangulo(0, 0)
print(r1.calculaArea(5, 10))
print(r1.calculaPerimetro(5, 10))

t1=Triangulo(0, 0)
print(t1.calculaArea(2, 5))
print(t1.calculaPerimetro(1, 2, 3))

# Exercício 3
tr1=TriAtleta(False, 40)
tr1.aquecer()
tr1.correr()
tr1.nadar()
tr1.pedalar()

# Exercício 4
c1=ContaCorrente(1)
p1=Poupanca(2, 0.1)
ci1=ContaImposto(3, 0.05)

print(c1.numero)
print(c1.saldo)
c1.creditar(2000.0)
print(c1.saldo)
c1.debitar(500.0)
print(c1.saldo)

print(p1.numero)
print(p1.saldo)
p1.creditar(2000.0)
print(p1.saldo)
p1.debitar(500.0)
print(p1.saldo)
p1.renderJuros()
print(p1.saldo)

print(ci1.numero)
print(ci1.saldo)
ci1.creditar(2000.0)
print(ci1.saldo)
ci1.debitar(500.0)
print(ci1.saldo)
ci1.calculaImposto()
print(ci1.saldo)