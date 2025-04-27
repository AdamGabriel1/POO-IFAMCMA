class Conexao:
    def __init__(self, tipoPorta: str, idProtocolo: int, taxaTransmissao: int):
        self.tipoPorta=tipoPorta
        self.idProtocolo=idProtocolo
        self.taxaTransmissao=taxaTransmissao

    def getProtocoloString(self):
        if self.idProtocolo==1:
            return "Rotoscope"
        
        elif self.idProtocolo==2:
            return "Acustico"
        
        elif self.idProtocolo==3:
            return "Radio"
        
        else:
            return "Outros"

    def getTaxaMBps(self):
        saida = self.taxaTransmissao/1024
        return saida

    def getDescricao(self):
        saida = f"Conexao: tipoPorta={self.tipoPorta}, potocolo={self.getProtocoloString()}, taxaTransmissao={self.getTaxaMBps()}MBps"
        return saida