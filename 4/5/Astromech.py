from Mestre import Mestre
from Sensor import Sensor
from Conexao import Conexao

class Astromech:
    def __init__(self, modelo: str, mestre: Mestre, sensor: Sensor, conexao: Conexao):
        self.modelo=modelo
        self.mestre=mestre
        self.sensor=sensor
        self.conexao=conexao

    def getDescricao(self):
        saida = f"Astromech modelo {self.modelo}. \n{self.mestre.getDescricao()}. \n{self.sensor.getDescricao()}. \n{self.conexao.getDescricao()}"
        return saida