class Usuario():
	
	def __init__ (self, email, nome_completo, endereco, cep, cpf, nickname, senha):
		self.email = email
		self.nome_completo = nome_completo
		self.endereco = endereco
		self.cep = cep
		self.cpf = cpf
		self.nickname = nickname
		self.senha = senha
		self.lista_carros = []
	
	def anunciar_carro(self, fabricante, modelo, ano, cor, blindagem):
		self.carro = veiculo(fabricante, modelo, ano, cor, blindagem)
		self.lista_carros.append(self.carro)
		
class Veiculo():
	
	def __init__(self, fabricante, modelo, ano, cor, blindagem):
		self.fabricante = fabricante
		self.modelo = modelo
		self.ano = ano
		self.cor = cor
		self.blindagem = blindagem