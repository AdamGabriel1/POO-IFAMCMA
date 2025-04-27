from Moto import *
from Farol import *

moto1=Moto("Yamaha","Fazer")
farolDaFrente=Farol("Xenon",40)
farolDeTras=Farol("Xenon",40)

#agregando
moto1.instalaFarol(farolDaFrente)
moto1.instalaFarol(farolDeTras)

#associando
moto1.farois[0].acender()
moto1.farois[0].apagar()
moto1.farois[1].acender()
moto1.farois[1].apagar()
