from xml.dom import minidom
import re


ruta = 'entrada.xml'


mydoc = minidom.parse(ruta)            # Creamos un objeto del documento
# diccionario = mydoc.getElementsByTagName('diccionario')      # Obtenemos los nodos con el tag 'item'
palabrasPositivas = ''
palabrasNegativas = ''
empresas_y_servicios = ''

def lectorXML(rutanueva):
    global palabrasPositivas, palabrasNegativas, empresas_y_servicios

    mydoc = minidom.parse(rutanueva)    

    """ SENTIMIENTOS """
    ##########################################################################################################
    """"""        
    sentimientos_positivos = mydoc.getElementsByTagName('sentimientos_positivos')      
    for x in sentimientos_positivos:
        for palabritas in x.getElementsByTagName('palabra'):
            palabra = palabritas.childNodes[0].data
            # print(palabra)
            palabrasPositivas += str.strip(palabra) + ' '            
    listaPPositivas = (str.rstrip(palabrasPositivas)).split(' ')
    for x in listaPPositivas:
        print(x)
    """"""
    ##########################################################################################################
    """"""        
    sentimientos_negativos = mydoc.getElementsByTagName('sentimientos_negativos')      
    for x in sentimientos_negativos:
        for palabritas in x.getElementsByTagName('palabra'):
            palabra = palabritas.childNodes[0].data
            # print(palabra)
            palabrasNegativas += str.strip(palabra) + ' '            
    listaPNegativas = (str.rstrip(palabrasNegativas)).split(' ')
    for x in listaPNegativas:
        print(x)
    """"""
    """"""
    """"""
    """"""
    empresas = mydoc.getElementsByTagName('empresa')      
    for x in empresas:
        if x.getElementsByTagName("nombre")[0]:
            cua = x.getElementsByTagName('nombre')[0]   
            # print(cua.nodeName, ':', str.strip(cua.childNodes[0].data))
            nombreEmpresa = str.strip(cua.childNodes[0].data)
            # print(nombreEmpresa)
            empresas_y_servicios += nombreEmpresa + ' '


            servicios = x.getElementsByTagName('servicio')
            for s in servicios:
                nameServicio = str.strip(s.getAttribute('nombre'))
                # print(nameServicio)
                empresas_y_servicios += nameServicio + ' '
                   
                    
                for aliass in s.getElementsByTagName('alias'):
                    dAlias = str.strip(aliass.childNodes[0].data)
                    # print(dAlias)
                    empresas_y_servicios += dAlias + ' '

                    # print('')
            empresas_y_servicios += '1' + " "
                    

    listaEmpresas = (str.rstrip(empresas_y_servicios)).split(' ')
    for x in listaEmpresas:
        print(x)
    """"""

lectorXML(ruta)