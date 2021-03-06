from contextlib import ContextDecorator
from distutils.archive_util import make_archive
import math
from posixpath import split
from xml.dom import minidom
import re
import sys 
import numpy as np 

from unicodedata import normalize

""" A VER SI NO DA PROBLEMAS"""
import xml.etree.cElementTree as ET
""""""

ruta = 'entrada.xml'


mydoc = minidom.parse(ruta)            # Creamos un objeto del documento
# diccionario = mydoc.getElementsByTagName('diccionario')      # Obtenemos los nodos con el tag 'item'
palabrasPositivas = ''
palabrasNegativas = ''
palabrasNeutras = ''
empresas_y_servicios = ''
lista_de_mensajes = ''
listado_fechas = ''

def lectorXML(rutanueva):
    global palabrasPositivas, palabrasNegativas, empresas_y_servicios, lista_de_mensajes, palabrasNeutras

    mydoc = minidom.parse(rutanueva)    

    """ SENTIMIENTOS """
    """"""        
    sentimientos_positivos = mydoc.getElementsByTagName('sentimientos_positivos')      
    for x in sentimientos_positivos:
        for palabritas in x.getElementsByTagName('palabra'):
            palabra = (palabritas.childNodes[0].data).lower()

            palabra = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", palabra), 0, re.I)
            # -> NFC
            palabra = normalize( 'NFC', palabra)
            print(palabra)
            
            # print(palabra)
            palabrasPositivas += str.strip(palabra) + ' '            
    listaPPositivas = (str.rstrip(palabrasPositivas)).split(' ')
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
            # print(palabra)
            palabrasNegativas += str.strip(palabra) + ' '            
    listaPNegativas = (str.rstrip(palabrasNegativas)).split(' ')
    palabrasNegativas = listaPNegativas
    # for x in palabrasNegativas:
    #     print(x)
    """"""
    """"""
    """ EMPRESAS Y SUS SERVICIOS """
    """"""
    empresas = mydoc.getElementsByTagName('empresa')      
    for x in empresas:
        if x.getElementsByTagName("nombre")[0]:
            cua = x.getElementsByTagName('nombre')[0]   
            # print(cua.nodeName, ':', str.strip(cua.childNodes[0].data))
            nombreEmpresa = str.strip(cua.childNodes[0].data)
            # print(nombreEmpresa)
            empresas_y_servicios += (nombreEmpresa.lower()) + ' '


            servicios = x.getElementsByTagName('servicio')
            for s in servicios:
                nameServicio = str.strip(s.getAttribute('nombre'))
                # print(nameServicio)
                empresas_y_servicios += (nameServicio).lower() + ' '
                   
                    
                for aliass in s.getElementsByTagName('alias'):
                    dAlias = str.strip(aliass.childNodes[0].data)
                    # print(dAlias)
                    empresas_y_servicios += (dAlias).lower() + ' '
                    ####################################################
                    palabrasNeutras += (dAlias).lower() + ' '
                    ####################################################
                    # print('')
            empresas_y_servicios += '1' + " "
                    

    listaEmpresas = (str.rstrip(empresas_y_servicios)).split(' ')
    empresas_y_servicios = listaEmpresas
    # print(palabrasNeutras)
    # for x in empresas_y_servicios:
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
            # print(mensaje)
            lista_de_mensajes += (mensaje).lower() + '$$44$$'
    listaMensaje = lista_de_mensajes.split('$$44$$')
    lista_de_mensajes = listaMensaje
    lista_de_mensajes.pop()
    # for x in lista_de_mensajes:
    #     print('******'+ x)
    """"""
    """"""
    analizar_fehcas_en_mensaje()


def analizar_fehcas_en_mensaje():
    global lista_de_mensajes, listado_fechas
    # lista = ['Ricky', 'Alvaro', 'David', 'Edgardo', 'Jacinto', 'Jose', 'Ricky', 'Jose', 'Jose', 'Gerardo']
    # lista.pop()
    """ INGRESANDO FECHAS A LISTA """
    """"""
    # print(len(lista_de_mensajes))
    # lista_de_mensajes.pop()
    # print(len(lista_de_mensajes))
    for x in lista_de_mensajes:
        match = re.search(r'(\d+/\d+/\d+)',x)
        listado_fechas += match.group(1) + ' '
        # print(match.group(1))
    cuas = (str.rstrip(listado_fechas)).split(' ')
    listado_fechas = cuas
    """ sacando solo las fechas que no se repiten """
    copy_listad_fechas = listado_fechas
    # print("Original List is: ",listado_fechas)
    convert_list_to_set = set(copy_listad_fechas)
    # print("Set is: ",convert_list_to_set)
    new_list = list(convert_list_to_set)
    # print("Resultant List is: ",new_list)
    copy_listad_fechas = list(convert_list_to_set)
    # print("Removed duplicates from original list: ",listado_fechas)
    # print(copy_listad_fechas)
    """"""   
    ##########################################################################################################
    """"""
    """ DETECTANDO FECHAS EN MENSAJES """
    """"""
    fechas_pal_xml = ''
    for x in copy_listad_fechas:
        # print(listado_fechas.count(x))
        fechas_pal_xml += x + ',' + str(listado_fechas.count(x)) + ' '
    
    # print(fechas_pal_xml)
    fechas_pal_xml_espacio = (str.rstrip(fechas_pal_xml)).split(' ')
    fechas_temp = ''
    for x in fechas_pal_xml_espacio:
        fechas_temp+= x + ','
        # print(x)
        
    fechas_pal_xml_coma = fechas_temp.split(',')
    fechas_pal_xml_coma.pop()
    # print(fechas_pal_xml_coma) #Con las fechas y su numero de mensajes
    """"""
    ##########################################################################################################
    """"""
    """"""
    """"""

    numeroFechas = len(copy_listad_fechas)
    # analizar_sentimientos_en_mensajes()
    cua(fechas_pal_xml_coma, numeroFechas)
    


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

            if fechaita == fecha and n_palab == 1:
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


def cua(fechas_pal_xml_coma, numeroFechas)           :
    lista_respuestas = ET.Element("lista_respuestas")
    respuesta = ET.SubElement(lista_respuestas, "respuesta")

    contador = 0
    contMes = 1
    for x in range(numeroFechas):
        fecha = ET.SubElement(respuesta, "fecha").text = fechas_pal_xml_coma[contador]
        mensajes = ET.SubElement(respuesta, "mensajes")
        ET.SubElement(mensajes, "total").text = fechas_pal_xml_coma[contMes]

        np = p_fech(fechas_pal_xml_coma[contador])
        # print(np)
        ET.SubElement(mensajes, "positivos").text = str(np)

        nn = n_fech(fechas_pal_xml_coma[contador])
        ET.SubElement(mensajes, "negativos").text = str(nn)
        ET.SubElement(mensajes, "neutros").text = "neutros"
        contador += 2
        contMes += 2

    arbol = ET.ElementTree(lista_respuestas)
    arbol.write("prueba.xml")



lectorXML(ruta)
# cua()