class Copo:
	def __init__(self,raio_topo,raio_base,altura,material,estilo):
		self.raio_topo=raio_topo
		self.raio_base=raio_base
		self.altura=altura
		self.material=material
		self.estilo=estilo
	
	def Calcular_volume():
		altura=input("Insira a altura do Copo:")
		largura=input("Insira a largura do Copo:")
		comprimento=input("Insira a comprimento do Copo:")
		volume=altura*largura*comprimento
		print(volume)
	
	def Encher():
		return 0
		
	def Esvaziar():
		return 0
