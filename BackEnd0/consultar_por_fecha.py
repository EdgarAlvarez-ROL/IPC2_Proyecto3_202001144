from configparser import ParsingError
from contextlib import ContextDecorator
import math
from socket import AddressFamily
from xml.dom import minidom
import re
import sys 
import numpy as np 

from unicodedata import normalize

""" A VER SI NO DA PROBLEMAS"""
import xml.etree.cElementTree as ET
""""""

ruta = 'BackEnd0//xmlCopyEntrada.xml'

mydoc = minidom.parse(ruta)            # Creamos un objeto del documento

palabrasPositivas = ''
palabrasNegativas = ''
palabrasNeutras = ''
empresas_y_servicios = ''
lista_de_mensajes = ''
listado_fechas = ''

listEmpresas = ''
namesServicios = ''

arrayFechas = []



def lectorXML(rutanueva, buscarEstaFecha):
    global palabrasPositivas, palabrasNegativas, empresas_y_servicios, lista_de_mensajes, palabrasNeutras, listEmpresas, namesServicios

    mydoc = minidom.parse(ruta)    

    """ SENTIMIENTOS """
    """"""        
    sentimientos_positivos = mydoc.getElementsByTagName('sentimientos_positivos')      
    for x in sentimientos_positivos:
        for palabritas in x.getElementsByTagName('palabra'):
            palabra = (palabritas.childNodes[0].data).lower()

            palabra = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", palabra), 0, re.I)
            # -> NFC
            palabra = normalize( 'NFC', palabra)
            # print(palabra)
            
            # print(palabra)
            palabrasPositivas += str.strip(palabra) + ' '            
    listaPPositivas = ((str.rstrip(palabrasPositivas))).split(' ')
    palabrasPositivas = listaPPositivas
    # for x in palabrasPositivas:
    #     print(x)
    """"""
    ##########################################################################################################
    """"""        
    sentimientos_negativos = mydoc.getElementsByTagName('sentimientos_negativos')      
    for x in sentimientos_negativos:
        for palabritas in x.getElementsByTagName('palabra'):
            palabra = (palabritas.childNodes[0].data).lower()

            palabra = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", palabra), 0, re.I)
            # -> NFC
            palabra = normalize( 'NFC', palabra)
            # print(palabra)

            # print(palabra)
            palabrasNegativas += str.strip(palabra) + ' '            
    listaPNegativas = (str.rstrip(palabrasNegativas)).split(' ')
    palabrasNegativas = listaPNegativas
    # for x in palabrasNegativas:
    #     print(x)
    """"""
    """"""
    ##########################################################################################################
    """ MENSAJES """
    """"""
    lista_mensajes = mydoc.getElementsByTagName('lista_mensajes')      
    for c in lista_mensajes:
        for mensajesx in c.getElementsByTagName('mensaje'):
            mensaje = mensajesx.childNodes[0].data

            mensaje = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", mensaje), 0, re.I)
            # -> NFC
            mensaje = normalize( 'NFC', mensaje)
            # print(mensaje)

            # print(mensaje)
            lista_de_mensajes += (mensaje).lower() + '$$44$$'
    listaMensaje = lista_de_mensajes.split('$$44$$')
    lista_de_mensajes = listaMensaje
    lista_de_mensajes.pop()
    # for x in lista_de_mensajes:
    #     print('******'+ x)
    """"""
    """"""
    analizar_fehcas_en_mensaje(buscarEstaFecha)


def analizar_fehcas_en_mensaje(buscarEstaFecha):
    global arrayFechas

    ruta = 'BackEnd0//database.xml'
    database = minidom.parse(ruta) 
    datos = database.getElementsByTagName('datos')      
    for x in datos:
        for fechas in x.getElementsByTagName('fecha'):
            lafecha = (fechas.childNodes[0].data)
            # print(lafecha)
            arrayFechas.append(lafecha)
    print()
    cua(arrayFechas,buscarEstaFecha)

""" DEF FECHAS"""
def p_fech(fecha):
    global palabrasPositivas, lista_de_mensajes
    contador = 0
    for x in range(len(palabrasPositivas)):
        for mess in lista_de_mensajes:
            match = re.search(r'(\d+/\d+/\d+)',mess)
            fechaita = match.group(1)
            n_palab = mess.count(palabrasPositivas[x])
            # print(n_palab)
            # print(fecha)

            if fechaita == fecha and n_palab >= 1:
                contador += 1
        # print('')   
    
    return contador

def n_fech(fecha):
    global palabrasNegativas, lista_de_mensajes
    contador = 0
    for x in range(len(palabrasNegativas)):
        for mess in lista_de_mensajes:
            match = re.search(r'(\d+/\d+/\d+)',mess)
            fechaita = match.group(1)
            n_palab = mess.count(palabrasNegativas[x])
            # print(n_palab)
            # print(fecha)

            if fechaita == fecha and n_palab == 1:
                contador += 1
        # print('')   
    
    return contador

def neu_fech(fecha):
    global palabrasNeutras, lista_de_mensajes
    contador = 0
    for x in range(len(palabrasNeutras)):
        for mess in lista_de_mensajes:
            match = re.search(r'(\d+/\d+/\d+)',mess)
            fechaita = match.group(1)
            n_palab = mess.count(palabrasNeutras[x])
            # print(n_palab)
            # print(fecha)

            if fechaita == fecha and n_palab == 1:
                contador += 1
        # print('')   
    
    return contador

def mensaje_con_fecha(fecha):
    global lista_de_mensajes
    contador = 0
    for mess in lista_de_mensajes:
        match = re.search(r'(\d+/\d+/\d+)',mess)
        fechaita = match.group(1)
        # print(n_palab)
        # print(fecha)
        if fechaita == fecha:
            contador += 1
    # print('')   
    
    return contador
""""""



def cua(arrayFechas, buscarEstaFecha):  
    global listEmpresas, namesServicios, lista_de_mensajes, palabrasNeutras,palabrasNegativas,palabrasPositivas


    file = 'Backend0//textPDF.txt'
    archivo = open(file, 'w') 

    lista_respuestas = ET.Element("lista_respuestas")
    respuesta = ET.SubElement(lista_respuestas, "respuesta")

    contador = 0
    contMes = 1
    # print(buscarEstaFecha)
    for x in arrayFechas:
        if contador == int(buscarEstaFecha):

            fecha = ET.SubElement(respuesta, "fecha").text = x
            mensajes = ET.SubElement(respuesta, "mensajes")
            nMess = mensaje_con_fecha(x)
            ET.SubElement(mensajes, "total").text = str(nMess)

            np = p_fech(x)
            ET.SubElement(mensajes, "positivos").text = str(np)

            nn = n_fech(x)
            ET.SubElement(mensajes, "negativos").text = str(nn)

            nneu = neu_fech(x)
            ET.SubElement(mensajes, "neutros").text = str(nneu)

            archivo.write('\nfecha\n'+x+ '\nTotal:' + str(nMess)+ '\nPositivos:' + str(np)+ '\nNegativos:' + str(nn)+ '\nNeutros:' + str(nneu) +'\n')

        contador += 1
        contMes += 2
    
    contador = 0
    contMes = 1


    archivo.close()
    arbol = ET.ElementTree(lista_respuestas)
    arbol.write("BackEnd0//request.xml")
    lista_de_mensajes = ''
    palabrasNeutras = ''
    palabrasNegativas = ''
    palabrasPositivas = ''


# lectorXML(ruta,0)
# cua()