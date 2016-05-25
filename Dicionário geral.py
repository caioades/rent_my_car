# -*- coding: utf-8 -*-
"""
Created on Mon May 16 16:59:01 2016

@author: caioades
"""

import firecall

my_firebase = firecall.Firebase("https://rent-my-car.firebaseio.com")

DG = {"usuario" : ["email","nome completo","endereço","CEP","CPF","nickname","senha"],"usuario2" : ["email","nome completo","endereço","CEP","CPF","nickname","senha"],"usuario3" : ["email","nome completo","endereço","CEP","CPF","nickname","senha"]}

my_firebase.put_sync(point="/Dicionário Geral", data=DG)

DC_anunciados = {"usuario" : [{"veiculo":["fabricante","modelo","ano","cor"]},{"veiculo":["fabricante","modelo","ano","cor"]}]}

my_firebase.put_sync(point="/Dicionário de Carros Alugados", data=DC_anunciados)

DC_alugados = {"usuario" : [{"veiculo":["fabricante","modelo","ano","cor","proprietário",True, "período", "preço"]},{"veiculo":["fabricante","modelo","ano","cor","propriterário",False,"período", "preço"]}]} #bool = blindagem(sim/não)

my_firebase.put_sync(point="/Dicionário de Carros Alugados", data=DC_alugados)

D_lances = {"usuario" : [{"veiculo":["lance1","lance2","lance3"]}]}

my_firebase.put_sync(point="/Registro de Renegociações", data=D_lances)

print(DC_anunciados["usuario"][0]["veiculo"][1])
for e in DG:
    if e == "usuario":
        print("aleluia")
    else:
        print(e)