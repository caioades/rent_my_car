# -*- coding: utf-8 -*-
"""
Created on Mon May 16 16:59:01 2016

@author: caioades


NOTA: NAO MEXER NUNCA MAIS!! 
submitar dados por meio de outros programas (caso contrário, serão perdidos todos os dados armazenados previamente no Firebase)
"""

import firecall

my_firebase = firecall.Firebase("https://rent-my-car.firebaseio.com")

DG = {"usuario" : ["email","nome completo","endereço","CEP","CPF","nickname","senha"],"usuario2" : ["email","nome completo","endereço","CEP","CPF","nickname","senha"],"usuario3" : ["email","nome completo","endereço","CEP","CPF","nickname","senha"]}

my_firebase.put_sync(point="/Dicionário Geral", data=DG)



DC_anunciados = {"usuario" : [{"veiculo":["fabricante","modelo","ano","cor","S","preco","periodo"]},{"veiculo":["fabricante","modelo","ano","cor","N","preco","periodo"]}]}

my_firebase.put_sync(point="/Dicionário de Carros Anunciados", data=DC_anunciados)



DC_alugados = {"usuario" : [{"veiculo":["fabricante","modelo","ano","cor","proprietario","S", "periodo", "preco"]},{"veiculo":["fabricante","modelo","ano","cor","proprietario","N","periodo", "preco"]}]} #bool = blindagem(sim/não)

my_firebase.put_sync(point="/Dicionário de Carros Alugados", data=DC_alugados)



D_lances = {"usuario" : [{"veiculo":[{"lance1":"usuario1"},{"lance2":"usuario2"},{"lance3":"usuario3"}]}]}

my_firebase.put_sync(point="/Registro de Renegociações", data=D_lances)


