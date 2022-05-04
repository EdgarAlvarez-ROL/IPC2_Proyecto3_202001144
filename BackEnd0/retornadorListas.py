from cgi import print_arguments
import json
import re
import os
from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE
from xml.dom import minidom


class Retornador:
    def __init__(self):
        self.listEmpresas = []
        self.lista_de_Fechas =[]
    
    def recibirFechas(self,listafechas, listaEmpresas):
        self.listEmpresas = listaEmpresas
        self.lista_de_Fechas = listafechas
        print(self.lista_de_Fechas)
        print(self.listEmpresas)

        file = 'BackEnd0\\database.xml'
        archivo = open(file, 'w') # abre el archivo datos.txt
        archivo.write('<datos>')
        for fechasA in listafechas:
            archivo.write('<fecha>' + fechasA + '</fecha>')
        
        for empresasA in listaEmpresas:
            archivo.write('<empresa>' + empresasA + '</empresa>')
        archivo.write('</datos>')
        # print(archivo.readline())
        archivo.close()
        
    

    def retornarFechas(self):
        # print('retornador Fechas')
        ruta = 'BackEnd0//database.xml'
        mydoc = minidom.parse(ruta) 
        datos = mydoc.getElementsByTagName('datos')      
        for x in datos:
            for fechas in x.getElementsByTagName('fecha'):
                lafecha = (fechas.childNodes[0].data)
                # print(lafecha)
                self.lista_de_Fechas.append(lafecha)
        
            # for empresas in x.getElementsByTagName('empresa'):
            #     laempresa = (empresas.childNodes[0].data)
            #     self.lista_de_Fechas.append(laempresa)

        return json.dumps((self.lista_de_Fechas))