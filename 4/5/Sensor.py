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