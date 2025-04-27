print("Aqui serao testadas as classes...")

from Caneca import Caneca
from Copo import Copo

Copo.Calcular_volume()

copoAmericano=Copo.Copo(0.25,0.2,0.3,"vidro","americano")

print(copoAmericano.altura)
copoAmericano.altura=0.4
print("Novo valor da altura...")
print(copoAmericano.altura)
