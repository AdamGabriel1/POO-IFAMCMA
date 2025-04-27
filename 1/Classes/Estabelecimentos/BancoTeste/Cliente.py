class Cliente:
	def __init__(self,nome,cpf,data_de_nasc,endereco):
		self.nome=nome
		self.cpf=cpf
		self.data_de_nasc=data_de_nasc
		self.endereco=endereco
	
	def mudar_endereco(self,novo_endereco):
		self.endereco=novo_endereco
		
	def fazer_emprestimo(self,valor):
		print("Solicitacao de emprestimo no nome de "+self.nome+" de R$ "+valor)
		
