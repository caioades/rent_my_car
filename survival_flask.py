# -*- coding: utf-8 -*-
"""
FLASK SURVIVAL
DAY 0

@author: caioades
"""


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



from flask import Flask, render_template, request, redirect, url_for


import firecall


app = Flask(__name__)

Veiculos = {}
@app.route("/", methods=['GET','POST']) #decorator '@' - no caso, uma objeto da classe Flask, com o método .route() 
def LogIn(): #mainpage - foto com login e senha 
    
    #importar DG do firebase (GET)
    my_firebase = firecall.Firebase("https://rent-my-car.firebaseio.com/")
    DG = my_firebase.get_sync(point="/Dicionário Geral")
    
    if request.method == 'POST':
        
        login = request.form['Login']
        senha = request.form['Senha']
        
        if login in DG:
            if DG[login] == senha:
                return #prosseguir 
            else: 
                s = 'Usuário ou senha inexistente!' #Mensagem de erro
                return render_template('main.html', dic = DG, erro = s)
        else:
            e = 'Usuário ou senha inexistente!' #Mensagem de erro
            return render_template('main.html', dic = DG, erro = e)
        
    return render_template('main.html', dic = DG, erro = '')
    

@app.route("/register", methods=['GET','POST'])
def Reg():
    
    my_firebase = firecall.Firebase("https://rent-my-car.firebaseio.com/")
    DB = eval(my_firebase.get_sync(point="/Dicionário Geral"))
    print(DB)
    if request.method == 'POST':
        
        nome_completo = request.form['Nome Completo']
        email = request.form['Email']
        endereco = request.form['Endereço']
        cpf = request.form['CPF']
        nickname = request.form['Usuário']
        senha = request.form['Senha']
        cep = request.form['CEP']
        
        
        #Veiculos[nickname] = Usuario(email, nome_completo, endereco, cep, cpf, nickname, senha)
        usuario = Usuario(email, nome_completo, endereco, cep, cpf, nickname, senha)
        usuario.salvar()
        
        '''if nickname in DG.keys:
            e = 'Esse nome de usuário já existe! Por favor, digite outro' 
            return render_template('register.html', dic = DG, erro = e)
        senha = request.form['Senha']
        if senha in DG.values:
            f = 'Esta senha já existe! Por favor, digite outra'
            return render_template('register.html', dic = DG, erro = f)
        
        # = Usuario(email, nome_completo, endereco, cep, cpf, nickname, senha)
        
        #DG[usuario] = [usuario.email, usuario.nome_completo, usuario.endereco, usuario.cep,usuario.cpf, usuario.nickname, usuario.senha]
        my_firebase = firecall.Firebase("https://rent-my-car.firebaseio.com")
        my_firebase.put_sync(point="/Dicionário Geral", data=DG)'''
        
    return render_template('register.html', dic = DB, erro = '')


@app.route('/Homepage')
def home():
    return render_template("Homepage.html", erro = '')

@app.route('/alugar') #endereço para alugar um carro (I)
def alugar():
    return render_template("alugar.html", erro ='')

@app.route('/alugar/modelo') # (II) escolha do modelo de carro
def modelo():
    
    modelo = request.args['Modelo']
    
    return render_template("modelo.html", erro = '')
    
@app.route('/alugar/tabela') # (III) escolher um dos carros dentre os da tabela 
def tabela(): 
    return render_template("tabela.html", erro='')
    
@app.route('/alugar/anúncio') # (IV) página do anúncio com opções de barganhar ou alugar
def anuncio():
    return render_template("anuncio.html", erro='')
    
@app.route('/alugar/barganha') #(V) opção de dar um lance de barganha 
def barganha():
    preco = request.forms['Faça um Lance']
    return render_template("barganha.html", erro='')

@app.route('/anunciar')
def anunciar():
    fabricante = request.args['Fabricante']
    modelo = request.args['Modelo']
    ano = request.args['Ano']
    #aluguel diario/mensal/semanal
    
    
    return render_template ('anunciar.html', erro='')
    
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)


