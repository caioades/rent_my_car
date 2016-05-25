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
def LogIn(): #mainpage - pagina login e senha 
    
    #importar DG do firebase (GET)
    my_firebase = firecall.Firebase("https://rent-my-car.firebaseio.com/")
    DG = eval(my_firebase.get_sync(point="/Dicionário Geral"))
    
    if request.method == 'POST':
        
        usuario = request.form['Login']
        senha = request.form['Senha']
        
        if usuario in DG:
            if DG[usuario][6] == senha:
                return render_template('main.html', dic = DG, erro = '')
            else: 
                s = 'Usuário ou senha inexistente!' #Mensagem de erro
                return render_template('main.html', dic = DG, erro = s)
        else:
            e = 'Usuário ou senha inexistente!' #Mensagem de erro
            return render_template('main.html', dic = DG, erro = e)
        
    return render_template('main.html', dic = DG, erro = '')
    

@app.route("/register/", methods=['GET','POST'])
def Reg():
    
    my_firebase = firecall.Firebase("https://rent-my-car.firebaseio.com/")
    DG = eval(my_firebase.get_sync(point="/Dicionário Geral"))
    print(DG)
    if request.method == 'POST':
        
        nome_completo = request.form['Nome Completo']
        email = request.form['Email']
        endereco = request.form['Endereço']
        cpf = request.form['CPF']
        nickname = request.form['Usuário']
        for e in DG:
            if e == nickname:
                e = 'Esse nome de usuário já existe! Por favor, digite outro' 
                return render_template('register.html', dic = DG, erro = e)
        senha = request.form['Senha']
        for f in DG: 
            if DG[f][7] == senha:
                s = 'Esta senha já existe! Por favor, digite outra'
                return render_template('register.html', dic = DG, erro = s)
        cep = request.form['CEP']
        
        DG[nickname]=[email, nome_completo, endereco, cep, cpf, nickname, senha] #devo criar objeto da classe Usuario para salvar, ou crio quando importo esses dados? 
        my_firebase.put_sync(point="/Dicionário Geral", data=DG)
        
        
    return render_template('register.html', erro = '')


@app.route('/Homepage/<usuario>')
def home(usuario):
    my_firebase = firecall.Firebase("https://rent-my-car.firebaseio.com/")
    DG = eval(my_firebase.get_sync(point="/Dicionário Geral"))
    DC_alugados = eval(my_firebase.get_sync(point="/Dicionário de Carros Alugados"))
    DC_anunciados = eval(my_firebase.get_sync(point="/Dicionário de Carros Anunciados"))
    lances = eval(my_firebase.get_sync(point="/Dicionário de Renegociações"))
    #listagem de veiculos do usuário:
    

    return render_template("Homepage.html", usuarios=DG, anunciados=DC_anunciados, alugados=DC_alugados, lances=lances, erro = '')

@app.route('/Alugar') #endereço para alugar um carro (I)
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
    
@app.route('/alugar/renegociar') #(V) opção de dar um lance de barganha 
def barganha():
    preco = request.forms['Faça um Lance']
    return render_template("renegociar.html", erro='')

@app.route('/anunciar')
def anunciar():
    fabricante = request.args['Fabricante']
    modelo = request.args['Modelo']
    ano = request.args['Ano']
    cor = request.args['Cor']
    
    veiculo = Veiculo(fabricante, modelo, ano, cor, blindagem)
    
    #aluguel diario/mensal/semanal
    
    
    return render_template ('anunciar.html', dic = DB,  erro='')
    
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)


