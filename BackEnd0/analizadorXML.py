from configparser import ParsingError
from contextlib import ContextDecorator
import math
from xml.dom import minidom
import re
import sys 
import numpy as np 

from unicodedata import normalize

from urllib3 import Retry

""" A VER SI NO DA PROBLEMAS"""
import xml.etree.cElementTree as ET
""""""

from retornadorListas import Retornador

ruta = 'BackEnd0//xmlCopyEntrada.xml'


mydoc = minidom.parse(ruta)            # Creamos un objeto del documento

palabrasPositivas = []
palabrasNegativas = []
palabrasNeutras = []
empresas_y_servicios = ''
lista_de_mensajes = ''
listado_fechas = ''

listEmpresas = ''
namesServicios = ''





def lectorXML(rutanueva):
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
            palabrasPositivas.append(palabra)          
    # listaPPositivas = ((str.rstrip(palabrasPositivas))).split(' ')
    # palabrasPositivas = listaPPositivas
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
            palabrasNegativas.append(palabra)        
    # listaPNegativas = (str.rstrip(palabrasNegativas)).split(' ')
    # palabrasNegativas = listaPNegativas
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
            """ IMPORTANTE ABAJO """
            # empresas_y_servicios += (nombreEmpresa.lower()) + ' '
            listEmpresas += (nombreEmpresa.lower()) + ' '


            servicios = x.getElementsByTagName('servicio')
            for s in servicios:
                nameServicio = str.strip(s.getAttribute('nombre'))
               

                # print(nameServicio)
                nameServicio = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", nameServicio), 0, re.I)
                    # -> NFC
                nameServicio = normalize( 'NFC', nameServicio)
                

                empresas_y_servicios += (nameServicio).lower() + ' '
                namesServicios += ((nameServicio).lower()) + ','
                # print(nameServicio)
                    
                for aliass in s.getElementsByTagName('alias'):
                    dAlias = str.strip(aliass.childNodes[0].data)

                    dAlias = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", dAlias), 0, re.I)
                    # -> NFC
                    dAlias = normalize( 'NFC', dAlias)
                    # print(palabra)

                    # print(dAlias)
                    empresas_y_servicios += (dAlias).lower() + ' ' # + '1' + ' '
                    ####################################################
                    palabrasNeutras.append((str.strip(dAlias)).lower())
                    ####################################################
                    # print(dAlias)
            empresas_y_servicios += '$6$44$6$' + " "
                    

    listaEmpresas = (str.rstrip(empresas_y_servicios)).split(' ')
    empresas_y_servicios = listaEmpresas
    # empresas_y_servicios.pop()

    tempEmpre = (str.rstrip(listEmpresas)).split(' ')
    listEmpresas = tempEmpre

    # listNeutras = (str.rstrip(palabrasNeutras)).split(' ')
    # palabrasNeutras = listNeutras
    # print(palabrasNeutras)

    # print(namesServicios)
    namesTemp = (str.strip(namesServicios)).split(',')
    namesServicios = namesTemp
    namesServicios.pop()

    # print(namesServicios)
    # print(empresas_y_servicios)
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
    cua(fechas_pal_xml_coma, numeroFechas, copy_listad_fechas)
    

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
""""""
""" DEF ANALISIS """
def ns_empre(empresa):
    global lista_de_mensajes, listEmpresas
    contador = 0
    
    for mess in lista_de_mensajes:
        n_palab = mess.count((empresa))
        # print(n_palab)
        # print(fecha)

        if  n_palab >= 1:
            contador += 1
        # print('')   
    # print('')
    return contador

def p_empre(empresa):
    global palabrasPositivas, lista_de_mensajes
    contador = 0
    for x in range(len(palabrasPositivas)):
        for mess in lista_de_mensajes:
            # print(empresa)
            
            n_palab = mess.count(palabrasPositivas[x])
            # print(n_palab)
            # print(empresa in mess)

            if ((empresa in mess) == True) and n_palab >= 1:
                contador += 1
        # print('')   

    return contador

def n_empre(empresa):
    global palabrasNegativas, lista_de_mensajes
    contador = 0
    for x in range(len(palabrasNegativas)):
        for mess in lista_de_mensajes:
            # print(empresa)
            
            n_palab = mess.count(palabrasNegativas[x])
            # print(n_palab)
            # print(empresa in mess)

            if ((empresa in mess) == True) and n_palab >= 1:
                contador += 1
        # print('')   

    return contador

def neu_empre(empresa):
    global palabrasNeutras, lista_de_mensajes
    contador = 0
    for x in range(len(palabrasNeutras)):
        for mess in lista_de_mensajes:
            # print(empresa)
            
            n_palab = mess.count(palabrasNeutras[x])
            # print(n_palab)
            # print(empresa in mess)

            if ((empresa in mess) == True) and n_palab >= 1:
                contador += 1
        # print('')   

    return contador
""""""
""" DEF SERVICIOS """
def p_serv(empresa, services):
    global lista_de_mensajes, listEmpresas, namesServicios, empresas_y_servicios, palabrasPositivas

    contador = 0

    for x in range(len(palabrasPositivas)):
        for mess in lista_de_mensajes:
            n_palab = mess.count(palabrasPositivas[x])
            for cuacua in empresas_y_servicios:
                
                # print(n_palab)
                # print(empresa in mess)
                if ((empresa in mess) == True) and n_palab >= 1 and ((cuacua in mess) == True):
                    contador += 1
                elif contador < 1 and cuacua == 1:
                    contador = 0

        # print('')   
    return contador

def n_serv(empresa, services):
    global lista_de_mensajes, listEmpresas, namesServicios, empresas_y_servicios, palabrasNegativas

    contador = 0

    for x in range(len(palabrasNegativas)):
        for mess in lista_de_mensajes:
            n_palab = mess.count(palabrasNegativas[x])
            for cuacua in empresas_y_servicios:
                
                # print(n_palab)
                # print(empresa in mess)
                if ((empresa in mess) == True) and n_palab >= 1 and ((cuacua in mess) == True):
                    contador += 1
                elif contador < 1 and cuacua == 1:
                    contador = 0

        # print('')   
    return contador

def neu_serv(empresa, services):
    global lista_de_mensajes, listEmpresas, namesServicios, empresas_y_servicios, palabrasNeutras

    contador = 0
    contadorres = 0
    for x in range(len(palabrasNeutras)):
        for mess in lista_de_mensajes:
            n_palab = mess.count(palabrasNeutras[x])
            for cuacua in empresas_y_servicios:
                
                # print(n_palab)
                # print(empresa in mess)
                if ((empresa in mess) == True) and n_palab >= 1 and ((cuacua in mess) == True):
                    contador += 1
                elif contador < 1 and cuacua == 1:
                    contador = 0
        contadorres += 1
        # print('')   
    return contador - contadorres
  

def ns_serv(empresa, services):
    global lista_de_mensajes, listEmpresas, namesServicios, empresas_y_servicios

    contador = 0
    # print(services)
    # print(empresas_y_servicios)

    bandera = False

    # print(empresa)
    for mess in lista_de_mensajes:
        for cuacua in empresas_y_servicios:
            
            # print(n_palab)
            # print(empresa in mess)
            # print(cuacua)
            

            if bandera == True:
                if ((empresa in mess) == True) and ((cuacua in mess) == True):
                    
                    contador += 1
                    # print(services + ' ' + empresa + ' ' +cuacua + ' '  + str(contador))
                    
                elif cuacua == '$6$44$6$':
                    break
            
            if cuacua == services:
                bandera = True
            
    # print(services)
    # print(empresas_y_servicios)   
    return (contador-1)
""""""



def cua(fechas_pal_xml_coma, numeroFechas,   copy_listad_fechas):  
    global listEmpresas, namesServicios, empresas_y_servicios,lista_de_mensajes, listado_fechas 
    file = 'Backend0//textPDF.txt'
    archivo = open(file, 'w') 
    

    lista_respuestas = ET.Element("lista_respuestas")
    respuesta = ET.SubElement(lista_respuestas, "respuesta")

    contador = 0
    contMes = 1
    for x in range(numeroFechas):
        fecha = ET.SubElement(respuesta, "fecha").text = fechas_pal_xml_coma[contador]
        mensajes = ET.SubElement(respuesta, "mensajes")
        ET.SubElement(mensajes, "total").text = fechas_pal_xml_coma[contMes]

        np = p_fech(fechas_pal_xml_coma[contador])
        ET.SubElement(mensajes, "positivos").text = str(np)

        nn = n_fech(fechas_pal_xml_coma[contador])
        ET.SubElement(mensajes, "negativos").text = str(nn)

        nneu = neu_fech(fechas_pal_xml_coma[contador])
        ET.SubElement(mensajes, "neutros").text = str(nneu)

        archivo.write('\nfecha\n'+fechas_pal_xml_coma[contador]+ '\nTotal:' + fechas_pal_xml_coma[contMes]+ '\nPositivos:' + str(np)+ '\nNegativos:' + str(nn)+ '\nNeutros:' + str(nneu) +'\n')
        contador += 2
        contMes += 2
    
    contador = 0
    contMes = 1
    analisis = ET.SubElement(respuesta, "analisis")
    for x in range(len(listEmpresas)):
        empresa = ET.SubElement(analisis, "empresa", {'nombre': listEmpresas[contador]})
        mensajes2 = ET.SubElement(empresa, "mensajes")

        # print(listEmpresas[contador])
        nMensaje = ns_empre(listEmpresas[contador]) 
        ET.SubElement(mensajes2, "total").text = str(nMensaje)


        np = p_empre(listEmpresas[contador])
        ET.SubElement(mensajes2, "positivos").text = str(np)

        nn = n_empre(listEmpresas[contador])
        ET.SubElement(mensajes2, "negativos").text = str(nn)

        nneu = neu_empre(listEmpresas[contador])
        ET.SubElement(mensajes2, "neutros").text = str(nneu)
        
        archivo.write('\nEmpresa\n'+listEmpresas[contador]+ '\nTotal:' + str(nMensaje) + '\nPositivos:' + str(np)+ '\nNegativos:' + str(nn)+ '\nNeutros:' + str(nneu) +'\n')


        for serbicio in namesServicios:
            servicio = ET.SubElement(empresa, "servicio", {'nombre': serbicio})
            mensajes3 = ET.SubElement(servicio, "mensajes")

            ttSErv = ns_serv(listEmpresas[contador], serbicio)
            ET.SubElement(mensajes3, "total").text = str(ttSErv)

            pServ = p_serv(listEmpresas[contador], serbicio)
            ET.SubElement(mensajes3, "positivos").text = str(pServ)

            nServ = n_serv(listEmpresas[contador], serbicio)
            ET.SubElement(mensajes3, "negativos").text = str(nServ)
            
            neuServ = neu_serv(listEmpresas[contador], serbicio)
            ET.SubElement(mensajes3, "neutros").text = str(neuServ)

            archivo.write('\nServicio\n'+serbicio+ '\nTotal:' + str(ttSErv) + '\nPositivos:' + str(pServ)+ '\nNegativos:' + str(nServ)+ '\nNeutros:' + str(neuServ) +'\n')


        
        contador += 1


    archivo.close()
    arbol = ET.ElementTree(lista_respuestas)
    arbol.write("BackEnd0//request.xml")
    
    
    ####################################################################################
    """"""
    retornadorF =  Retornador()
    retornadorF.recibirFechas(copy_listad_fechas, listEmpresas)
    
    
    empresas_y_servicios = ''
    lista_de_mensajes = ''
    listado_fechas = ''

    listEmpresas = ''
    namesServicios = ''


# lectorXML(ruta)