# -*- coding: utf-8 -*-
"""
FLASK SURVIVAL
DAY 0

@author: caioades
"""

from flask import Flask, render_template, request, redirect, url_for

from classes import Usuario, Veiculo


app = Flask(__name__)

@app.route("/", methods=['GET','POST']) #decorator '@' - no caso, uma objeto da classe Flask, com o método .route() 
def LogIn(): #mainpage - foto com login e senha 
    
    if request.method == 'POST':
        
        login = request.form['Login']
        senha = request.form['Senha']
        
        if login in Usuario.DU:
            if Usuario.DU[login] == senha:
                return #prosseguir 
            else: 
                s = 'Usuário ou senha inexistente!' #Mensagem de erro
                return render_template('main.html', dic = Usuario.DU, erro = s)
        else:
            e = 'Usuário ou senha inexistente!' #Mensagem de erro
            return render_template('main.html', dic = Usuario.DU, erro = e)
        
    return render_template('main.html', dic = Usuario.DU, erro = '')
    

@app.route("/register", methods=['GET','POST'])
def Reg():
    
    
    if request.method == 'POST':
        
        nome_completo = request.form['Nome Completo']
        endereco = request.form['Endereço']
        cep = request.form['CEP']
        cpf = request.form['CPF']
        email = request.form['Email']
        nickname = request.form['Usuário']
        if nickname in Usuario.DU.keys:
            e = 'Esse nome de usuário já existe! Por favor, digite outro' 
            return render_template('register.html', dic = Usuario.DU, erro = e)
        senha = request.form['Senha']
        if senha in Usuario.DU.values:
            f = 'Esta senha já existe! Por favor, digite outra'
            return render_template('register.html', dic = Usuario.DU, erro = f)
        
        usuario = Usuario(email, nome_completo, endereco, cep, cpf, nickname, senha)
        Usuario.DU[usuario] = [usuario.email, usuario.nome_completo, usuario.endereco, usuario.cep,usuario.cpf, usuario.nickname, usuario.senha]
        
    return render_template('register.html', dic = Usuario.DU, erro = '')


@app.route('/home')
def home():
    return render_template("home.html", dic = Usuario.DU, erro = '')

@app.route('/alugar') #endereço para alugar um carro (I)

@app.route('/alugar/modelo') # (II) escolha do modelo de carro

@app.route('/alugar/tabela') # (III) escolher um dos carros dentre os da tabela 

@app.route('/alugar/anúncio') # (IV) página do anúncio com opções de barganhar ou alugar

@app.route('/alugar/barganha') #(V) opção de dar um lance de barganha 


@app.route('/anunciar')
def anunciar():
    return render_template ('anunciar.html')
    
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)


