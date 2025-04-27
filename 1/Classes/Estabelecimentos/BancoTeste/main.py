import Cliente

joao=Cliente.Cliente("Joao da Silva",23632,"06/06/1995","Rua A, Bairro B, Maues-AM")

print(joao.nome)

maria=Cliente.Cliente("Maria Alburquerque", "65456", "11/11/2000", "Rua B, 2, Bairro A, Maues-AM")
print(maria.endereco)

print(joao.endereco)
joao.mudar_endereco("Rua C, 3, Bairro X, Maues-AM")
print(joao.endereco)

maria.fazer_emprestimo('2000')
joao.fazer_emprestimo('30')
