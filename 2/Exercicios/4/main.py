from ContaCorrente import *
from ContaImposto import *
from Poupanca import *

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