# -*- coding: utf-8 -*-
"""
FLASK SURVIVAL
DAY 0

@author: caioades
"""

from flask import Flask, render_template, request, redirect, url_for


DU = {} #dicionario dos usuários : {usuario : senha}

app = Flask(__name__)

@app.route("/", methods=['GET','POST']) #decorator '@' - no caso, uma objeto da classe Flask, com o método .route() 
def main(): #mainpage - foto com login e senha 
    
    if request.method == 'POST':
        
        login = request.args['Login']
        senha = request.args['Senha']
        
        if login in DU:
            if DU[login] == senha:
                return #prosseguir 
            else: 
                e = 'Usuário ou senha inexistente!' #Mensagem de erro
                return render_template('main.html', dic = DU, erro = e)
        else:
            e = 'Usuário ou senha inexistente!' #Mensagem de erro
            return render_template('main.html', dic = DU, erro = e)
        
    
    
    
    return render_template('main.html', dic = DU, erro = '')
    
@app.route("/register")
def reg(): 
    
    
    DU[login] = senha


app.run()



