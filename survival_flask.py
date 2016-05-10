# -*- coding: utf-8 -*-
"""
FLASK SURVIVAL
DAY 0

@author: caioades
"""

from flask import Flask, render_template, request, redirect, url_for

from classes import Usuario, Veiculo



DU = {} #dicionario dos usuários : {usuario : senha}

app = Flask(__name__)

@app.route("/", methods=['GET','POST']) #decorator '@' - no caso, uma objeto da classe Flask, com o método .route() 
def LogIn(): #mainpage - foto com login e senha 
    
    if request.method == 'POST':
        
        login = request.form['Login']
        senha = request.form['Senha']
        
        if login in DU:
            if DU[login] == senha:
                return #prosseguir 
            else: 
                s = 'Usuário ou senha inexistente!' #Mensagem de erro
                return render_template('main.html', dic = DU, erro = s)
        else:
            e = 'Usuário ou senha inexistente!' #Mensagem de erro
            return render_template('main.html', dic = DU, erro = e)
        
    return render_template('main.html', dic = DU, erro = '')
    

@app.route("/register", methods=['GET','POST'])
def Reg():
    
    
    if request.method == 'POST':
        
        nome_completo = request.form['Nome Completo']
        endereco = request.form['Endereço']
        cep = request.form['CEP']
        cpf = request.form['CPF']
        email = request.form['Email']
        nickname = request.form['Usuário']
        if nickname in DU.keys:
            e = 'Esse nome de usuário já existe! Por favor, digite outro' 
            return render_template('register.html', dic = DU, erro = e)
        senha = request.form['Senha']
        if senha in DU.values:
            f = 'Esta senha já existe! Por favor, digite outra'
            return render_template('register.html', dic = DU, erro = f)
        
        usuario = Usuario(email, nome_completo, endereco, cep, cpf, nickname, senha)
        DU[usuario] = [usuario.email, usuario.nome_completo, usuario.endereco, usuario.cep,usuario.cpf, usuario.nickname, usuario.senha]
        
    return render_template('register.html', dic = DU, erro = '')



#app.run()


