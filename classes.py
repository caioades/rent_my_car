import firecall
my_firebase = firecall.Firebase("https://rent-my-car.firebaseio.com/")

class Usuario():
	
	def __init__ (self, email, nome_completo, endereco, cep, cpf, nickname, senha):
		self.email = email
		self.nome_completo = nome_completo
		self.endereco = endereco
		self.cep = cep
		self.cpf = cpf
		self.nickname = nickname
		self.senha = senha
		self.dicio_carros_anunciados = {}
		self.dicio_carros_alugados = {}
		self.dicio_usuarios = {}
		
	
	def anunciar_carro (self, fabricante, modelo, ano, cor, blindagem):
		self.carro_anunciado = Veiculo(fabricante, modelo, ano, cor, blindagem)
		self.dicio_carros_anunciados[self.nickname] = self.carro_anunciado		
	
	def alugar_carro (self, fabricante, modelo, ano, cor, blindagem):
		self.carro_alugado = Veiculo(fabricante, modelo, ano, cor, blindagem)
		self.dicio_carros_alugados[self.nickname] = self.carro_alugado				

	def salvar (self):
           DU = {}
           DU[self.usuario] = self.email, self.nome_completo,self.endereco,self.cep, self.cpf,self.nickname,self.senha,self.dicio_carros_anunciados,self.dicio_carros_alugados   
           my_firebase = firecall.Firebase("https://rent-my-car.firebaseio.com/")
           my_firebase.put_sync(point="/Dados do usuário/{0}".format(self.nickname), data=DU)
		
		

class Veiculo():
	
	def __init__(self, fabricante, modelo, ano, cor, blindagem):
		self.fabricante = fabricante
		self.modelo = modelo
		self.ano = ano
		self.cor = cor
		self.blindagem = blindagem