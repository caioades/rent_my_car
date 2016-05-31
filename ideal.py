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

app.secret_key='\xd0\xe2\xef\xbdq~\x99\xe9\xe7Z\x13i\x87Vlx0q5n\x14\x10D\xb7'


@app.route("/", methods=['GET','POST']) #decorator '@' - no caso, uma objeto da classe Flask, com o método .route() 
def LogIn(): #mainpage - pagina login e senha 
    
    #importar DG do firebase (GET)
    my_firebase = firecall.Firebase("https://rent-my-car.firebaseio.com/")
    DG = eval(my_firebase.get_sync(point="/Dicionário Geral"))
    usuario=''
    
    if request.method == 'POST':
        
        usuario = request.form['usuario']
        print("OLHA O USUARIO!!!!!!!!!!!!", usuario)
        
        senha = request.form['senha']
        
        return redirect(url_for('home', usuario=usuario))
        
        
        if usuario in DG:
            if DG[usuario][6] == senha:
                return redirect(url_for('Homepage',usuario=usuario))
            else: 
                s = 'Usuário ou senha inexistente!' #Mensagem de erro
                return redirect(url_for('LogIn', dic = DG,usuario=usuario, erro = s))
        else:
            e = 'Usuário ou senha inexistente!' #Mensagem de erro
            return redirect(url_for('LogIn', dic = DG,usuario=usuario, erro = e))
    
    return render_template('main.html', dic = DG, usuario=usuario, erro = '')
    

@app.route("/register/", methods=['GET','POST'])
def Reg():
    
    my_firebase = firecall.Firebase("https://rent-my-car.firebaseio.com/")
    DG = my_firebase.get_sync(point="/Dicionário Geral")
    if DG == b'null':
        DG = {}
    else:
        DG = eval(DG)
    			
    if request.method == 'POST':
        
        nome_completo = request.form['nome']
        email = request.form['email']
        endereco = request.form['endereco']
        cpf = request.form['cpf']
        nickname = request.form['usuario']
        print(nickname)
        for k in DG:
            if k == nickname:
                e = 'Esse nome de usuário já existe! Por favor, digite outro' 
                return render_template('register.html', dic = DG, erro = e)
        senha = request.form['senha']
        for f in DG: 
            if DG[f][6] == senha:
                s = 'Esta senha já existe! Por favor, digite outra'
                return render_template('register.html', dic = DG, erro = s)
        cep = request.form['cep']
        
        DG[nickname]=[email, nome_completo, endereco, cep, cpf, nickname, senha] #devo criar objeto da classe Usuario para salvar, ou crio quando importo esses dados? 
        my_firebase.put_sync(point="/Dicionário Geral", data=DG)
        
        return redirect(url_for('LogIn'))
        
    return render_template('register.html', dic = DG, erro = '')


@app.route('/Homepage',methods=['GET','POST'])
def home():
    usuario = request.form['usuario']
    print("OLHA O USUARIO!!!!!!!!!!!!", usuario)
   
        
    DC_anunciados = my_firebase.get_sync(point="/Dicionário de Carros")
    if DC_anunciados == b'null':
        DC_anunciados = {}
    else:
        DC_anunciados = eval(DC_anunciados)
    
    
    lances = my_firebase.get_sync(point="/Registro de Renegociações")
    if lances == b'null':
        lances = {}
    else:
        lances = eval(lances)
    

    #listagem de veiculos do usuário:
    #,usuarios=DG, anunciados=DC_anunciados, alugados=DC_alugados, lances=lances,
    
    return render_template("Homepage.html", anunciados=DC_anunciados, lances=lances, erro = '')
    
    
@app.route('/Homepage/perfil')
def perfil(): 
    import firecall 
    usuario = request.args['usuario']       
    
    my_firebase = firecall.Firebase("https://rent-my-car.firebaseio.com/")
    DG = my_firebase.get_sync(point="/Dicionário Geral")
    if DG == b'null':
        print(DG)
        DG = {}
    else:
        DG = eval(DG)
    print("DG:",DG)
        
    DC_alugados = my_firebase.get_sync(point="/Dicionário de Carros Alugados")
    if DC_alugados == b'null':
        DC_alugados = {}
    else:
        DC_alugados = eval(DC_alugados)
    print("alugados:",DC_alugados)
    
    lances = my_firebase.get_sync(point="/Registro de Renegociações")
    if lances == b'null':
        lances = {}
    else:
        lances = eval(lances)
    print("lances:", lances)
    
    return render_template("perfil.html",usuarios=DG,alugados=DC_alugados,usuario=usuario, erro='')
    

@app.route('/alugar',methods=['GET','POST']) #endereço para alugar um carro (I)
def alugar():
    return render_template("alugar.html", erro ='')

@app.route('/alugar/modelo',methods=['GET','POST']) # (II) escolha do modelo de carro
def modelo():
    
    modelo = request.args['Modelo']
    
    return render_template("modelo.html", erro = '')
    
@app.route('/alugar/tabela',methods=['GET','POST']) # (III) escolher um dos carros dentre os da tabela 
def tabela(): 
    return render_template("tabela.html", erro='')
    
@app.route('/alugar/anúncio',methods=['GET','POST']) # (IV) página do anúncio com opções de barganhar ou alugar
def anuncio():
    return render_template("anuncio.html", erro='')
    
@app.route('/alugar/renegociar',methods=['GET','POST']) #(V) opção de dar um lance de barganha 
def barganha():
    preco = request.forms['Faça um Lance']
    return render_template("renegociar.html", erro='')

@app.route('/anunciar',methods=['GET','POST'])
def anunciar():
    '''fabricante = request.args['Fabricante']
    modelo = request.args['Modelo']
    ano = request.args['Ano']
    cor = request.args['Cor']
    
    #veiculo = Veiculo(fabricante, modelo, ano, cor, blindagem)

    , dic = DG,    
    
    #aluguel diario/mensal/semanal'''
    
    
    return render_template ('anunciar.html',  erro='')
    
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)


