from configparser import ParsingError
from contextlib import ContextDecorator
import math
from xml.dom import minidom
import re
import sys 
import numpy as np 


def retornarFechas():
  print('retornador Fechas')
  ruta = 'BackEnd0//database.xml'
  mydoc = minidom.parse(ruta) 
  datos = mydoc.getElementsByTagName('datos')      
  for x in datos:
    for fechas in x.getElementsByTagName('fecha'):
      lafecha = (fechas.childNodes[0].data).lower()
      print(lafecha)
      # self.lista_de_Fechas.append(x)



retornarFechas()