from Mestre import Mestre
from Sensor import Sensor
from Conexao import Conexao
from Astromech import Astromech

novoMestre=Mestre("Luke Skywalker",100,"Alianca para Restauracao da Republica","Jedi")
print(novoMestre.getIdade(5))
print(novoMestre.possuiForca())
print(novoMestre.getAnoNascimentoString())
print(novoMestre.getDescricao())

novoSensor=Sensor("Azul",512.0,240)
print(novoSensor.getMPixelsPorSegundo())
print(novoSensor.getDescricao())

novaConexao=Conexao("SCOMP Link",1,4096000)
print(novaConexao.getProtocoloString())
print(novaConexao.getTaxaMBps())
print(novaConexao.getDescricao())

astromech1=Astromech("R2-D2",novoMestre,novoSensor,novaConexao)
print(astromech1.getDescricao())