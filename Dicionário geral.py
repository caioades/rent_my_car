# -*- coding: utf-8 -*-
"""
Created on Mon May 16 16:59:01 2016

@author: caioades
"""

import firecall

my_firebase = firecall.Firebase("https://rent-my-car.firebaseio.com")

DG = {"usuario" : "infos" }

my_firebase.put_sync(point="/Dicionário Geral", data=DG)

DC = {"usuario" : {"veiculo":["fabricante","modelo","ano","cor"]}}

my_firebase.put_sync(point="/Dicionário de Carros", data=DC)

