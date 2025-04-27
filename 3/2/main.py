from InfoClientePessoaFisica import *
from InfoClientePessoaJuridica import *
from ClienteFidelizacao import *

icpf=InfoClientePessoaFisica("123456789")
icpj=InfoClientePessoaJuridica("123456789-0000")
cf=ClienteFidelizacao("José","Rua: A, Bairro: A, Cidade: ABCD",1000.0,"10/10/2010")

icpf.info()
print(" ")
icpj.info()
print(" ")
cf.info()