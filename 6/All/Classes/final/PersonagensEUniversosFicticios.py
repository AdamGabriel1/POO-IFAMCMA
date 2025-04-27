class Mestre:
    def __init__(self,nome: str, anoNascimento: int, afiliacao: str, posto: str):
        self.nome=nome
        self.anoNascimento=anoNascimento
        self.afiliacao=afiliacao
        self.posto=posto

    def getIdade(self, anoReferencia: int):
        idade = anoReferencia - self.anoNascimento
        return idade

    def possuiForca(self):
        if self.posto=="Jedi" or self.posto=="Sith":
            return True
        
        else:
            return False
        
    def getAnoNascimentoString(self):
        if self.anoNascimento<0:
            saida = str(self.anoNascimento) + "ABY"
        
        else:
            saida = str(self.anoNascimento) + "DBY"
        
        return saida
        
    def getDescricao(self):
        saida = f"Mestre: nome={self.nome}, anoNascimento={self.getAnoNascimentoString()}, afiliacao={self.afiliacao}, posto={self.posto}, possuiForca={self.possuiForca()}"
        return saida

class Sensor:
    def __init__(self, cor: str, resolucao: float, framesPorSegundo: int):
        self.cor=cor
        self.resolucao=resolucao
        self.framesPorSegundo=framesPorSegundo

    def getMPixelsPorSegundo(self):
        saida = self.resolucao * float(self.framesPorSegundo)
        return saida

    def getDescricao(self):
        saida = f"Sensor: {self.cor}, resolucao={self.resolucao}Mp, framesPorSegundo={self.framesPorSegundo}fps, mPixelsPorSegundo={self.getMPixelsPorSegundo()}Mpps"
        return saida

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

class Astromech:
    def __init__(self, modelo: str, mestre: Mestre, sensor: Sensor, conexao: Conexao):
        self.modelo=modelo
        self.mestre=mestre
        self.sensor=sensor
        self.conexao=conexao

    def getDescricao(self):
        saida = f"Astromech modelo {self.modelo}. \n{self.mestre.getDescricao()}. \n{self.sensor.getDescricao()}. \n{self.conexao.getDescricao()}"
        return saida

class IniciadoJedi:
    def __init__(self,nome: str,especie: str,anoNascimento: int):
        self.nome=nome
        self.especie=especie
        self.anoNascimento=anoNascimento

    def getDescricao(self):
        return f"{self.nome} (especie={self.especie}, nascimento={self.getAnoNascimento()})"

    def getAnoNascimento(self):
        if self.anoNascimento<0:
            saida = f"{self.anoNascimento} DBY"
        
        else:
            saida = f"{self.anoNascimento} ABY"
        
        return saida

class TreinadorJedi:
    def __init__(self,titulacao: str, nome: str):
        self.titulacao=titulacao
        self.nome=nome

    def getDescricao(self):
        return f"{self.titulacao} {self.nome}"
    
class SessaoJedi:
    def __init__(self,nome: str, treinador: TreinadorJedi):
        self.nome=nome
        self.treinador=treinador
        self.iniciados=[]

    def addIniciado(self,iniciado: str):
        self.iniciados.append(iniciado)

    def getIniciado(self,nome: str):
        for i in self.iniciados:
            if nome==i:
                return i.nome

        return None

    def getMediaAnoNascimento(self):
        media=0
        i=0
        for iniciados in self.iniciados:
            media=iniciados.anoNascimento+media
            i=i+1
        media=media/i
        return media

    def getDescricao(self):
        saida=f"--> SESSÃO {self.nome} (Treinador: {self.treinador.getDescricao()})"
        for iniciados in self.iniciados:
            saida=f"{saida}\n - Iniciado: {iniciados.getDescricao()}"

        return saida