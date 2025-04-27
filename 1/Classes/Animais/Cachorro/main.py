from Cachorro import Cachorro

Doberman=Cachorro("Dob","Doberman",15,"Preto e Branco",20,16,"Macho","Nome")

print(f"Nome: {Doberman.nome}")
print(f"Raça: {Doberman.raca}")
print(f"Idade: {Doberman.idade}")
print(f"Cor: {Doberman.cor}")
print(f"Altura: {Doberman.altura}cm")
print(f"Peso: {Doberman.peso}kg")
print(f"Gênero: {Doberman.genero}")
print(f"Nome do Dono: {Doberman.dono}")

Doberman.latir()
Doberman.andar()
Doberman.comer()
Doberman.brincar()
Doberman.fazer_truques()
Doberman.receber_carinho()
Doberman.definir_dono("Novo Nome")
print(f"Nome do Dono: {Doberman.dono}")