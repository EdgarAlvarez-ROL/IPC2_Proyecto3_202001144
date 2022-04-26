from posixpath import split
from traceback import print_tb
from tracemalloc import stop
from xml.dom import minidom

from sqlalchemy import null                     # Importamos la libreria
import ListaSimpleDentro
import tkinter
# from tkinter import *
from tkinter import filedialog
# from tkinter import messagebox, ttk, PhotoImage
import re
import xml.etree.ElementTree as ET

import escritorGraphviz


# VARIABLES GLOBALES
ruta = 'Archivo.xml'


mydoc = minidom.parse(ruta)            # Creamos un objeto del documento

pisos = mydoc.getElementsByTagName('piso')      # Obtenemos los nodos con el tag 'item'

nodoHijo = ListaSimpleDentro.nodoHJjo('','','','','','')
lista1 = ListaSimpleDentro.lista_simple()
# listaTemp = ListaSimpleDentro.lista_simple()
listaCodigos = ListaSimpleDentro.nodoHJjo.Codigoss()



# print('Piso #2 atribute.')
# print(pisos[1].attributes['nombre'].value)        # Obtenemos el valor del atributo especificado

# print('\nAll attributes.')
# for elem in pisos:                              # Imprimiendo los valores de los atributos
#     print(elem.attributes['nombre'].value)


"""====EXPLICACION PARA NO HACERME BOLAS====
Primero instancio un objeto de clase nodoHijo dentro del archivo ListaSimpleDentro
para que??
para tener un objeto que se metera luego en una lista y asi manejar mejor los datos
dicho objeto nodoHijo tiene dentro de si una lista manual llamada Codigoss con doble ss
que tiene todos los codigo sin importar el numero que haya dentro del XML
va
luego instancio una lista1 que sera la lista principal que tiene todos los objetos de con los datos de los Pisos
va
luego la listaTemp es una lista manual que tiene datos de codigos temporales, creo que no la usare pero la dejare comentada 
va
luego tenemos una lista Codigos que no se usa para ni miercoles pero ahi la dejo
va
ir abajo para ver mas anotaciones
"""

def lectorXML(rutanueva):
    global ruta, mydoc, pisos, nodoHijo, lista1, listaCodigos
    ruta = rutanueva

    mydoc = minidom.parse(ruta)            

    pisos = mydoc.getElementsByTagName('piso')      

    """Lo que esta comentado de PRINT NO TOCAR"""
    # Intentando leer los pisos
    for x in pisos:
        if x.hasAttribute("nombre"):
            """print("\nnombre:", x.getAttribute("nombre"))"""
            nodoHijo.nombre = x.getAttribute("nombre")

            # elemento de R
            lasR = x.getElementsByTagName('R')[0]
            """print(lasR.nodeName, ':', str.strip(lasR.childNodes[0].data))"""
            nodoHijo.R = (str.strip(lasR.childNodes[0].data))
            # listaNombres.insertar_fin(str.strip(lasR.childNodes[0].data))

            # elemento de C
            lasC = x.getElementsByTagName('C')[0]
            """print(lasC.nodeName, ':', str.strip(lasC.childNodes[0].data))"""
            nodoHijo.C = (str.strip(lasC.childNodes[0].data))

            # elemento de F
            lasF = x.getElementsByTagName('F')[0]
            """print(lasF.nodeName, ':', str.strip(lasF.childNodes[0].data))"""
            nodoHijo.F = (str.strip(lasF.childNodes[0].data))

            # elemento de S
            lasS = x.getElementsByTagName('S')[0]
            """print(lasS.nodeName, ':', str.strip(lasS.childNodes[0].data))"""
            nodoHijo.S = (str.strip(lasS.childNodes[0].data))

            # Instancio el minidom que leera los patron dentro del xml no es necesario poner patrones ya que ira directo a la clase que quiero y sus datos
            patrones = x.getElementsByTagName('patron')
            # print('numero de patrones')
            # print(len(patrones))

            for i in range(len(patrones)):
                cod = patrones[i].getAttribute('codigo')
                patronPiso = str.strip(patrones[i].childNodes[0].data)
                varCod = cod+' '+(str.strip(patronPiso))
                # print('codigo :'+cod)
                # print('patron :'+varCod)

                nodoHijo.codigos.insertar_fin_cua(varCod)

            # nodoHijo.codigos = listaCodigos


            lista1.insertar_fin((nodoHijo))
            nodoHijo = ListaSimpleDentro.nodoHJjo('','','','','','')
    
    # lista1.ordenamiento()
    print('\nDatos analizados correctamente\n')




def mainQ():
    global ruta

    salir = False
    opcion = 0

    espera = False

    par = ''

    while not salir:
        print('====================== MENU ======================')
        print ("1. Ingrese la ruta de su archivo XML            |")
        print ("2. Ver pisos de su archivo xml                  |")
        print ("3. Salir                                        |")
        print ("----Elige una opcion")
        print('==================================================')
        opcion = pedirNumeroEntero()

        if opcion == 1:
            print('\n \n======================OPCION 1======================')
            # ruta = input("introduzca a ruta de tu archivo XML a analizar:    ")
            # print('\nsu ruta escogida es: '+ruta)
            fn_abrirArchivo()
            print('Analizando XML...')
            lectorXML(ruta)

            
        elif opcion == 2:
            print('\n \n==================OPCION 2 -PISOS-==================')
            print('--Escoja un piso para ver su informacion--')
            lista1.obtenerNombres()
            
           
            pisoABuscar = str(input('\nIngrese el nombre del piso que desea ver: \n'))
            # print('\nUsted busco la informacion del piso llamado: '+pisoABuscar+'\n')
            obtenerDatosPiso = lista1.obtener1soloNodo(pisoABuscar) 
            # print(obtenerDatosPiso)

            # ===================================
            print('\nDatos del piso escogio llamado: \"'+pisoABuscar+'\"')
            lista1.imprimir_1soloNodo(pisoABuscar)
            print('Patrones con su codigo: ')
            # ===================================
            cod = obtenerDatosPiso[5].rstrip()
            solo=0
            cods = cod.split(' ')
            for pa in range(0,len(cods),2):
                    print(cods[pa] + ': ' + cods[pa+1])
                    solo += 1 
                
            
            # ===================================
            codEntrada = ''
            codSalida = ''

            codUsar = str(input('\n---->Ingrese el codigo del patron que desea usar: '))
            solo = 0
            for pa in cods:
                if pa == codUsar:
                    codEntrada = (cods[solo+1])
                    escritorGraphviz.crearGraficoEntrada(str(cods[solo+1]), int(obtenerDatosPiso[1]), int(obtenerDatosPiso[2]))
                    break
                solo += 1
            

            # ===================================
            codCamb = str(input('\n---->Ingrese el codigo del patron al que desea cambiar: '))
            solo = 0
            for pa in cods:
                if pa == codCamb:
                    codSalida = (cods[solo+1])
                    escritorGraphviz.crearGraficoSalida(str(cods[solo+1]), int(obtenerDatosPiso[1]), int(obtenerDatosPiso[2]))
                    break
                solo += 1

            voltearF = int(obtenerDatosPiso[3])
            intercambiarS = int(obtenerDatosPiso[4])

            
            contadorB1 = 0
            contadorB2 = 0
            for x in codEntrada:
                if x == 'B':
                    contadorB1 += 1
            for x in codSalida:
                if x =='B':
                    contadorB2 += 1
            restCosto = contadorB2 - contadorB1
            if restCosto <= 0:
                restCosto = restCosto * -1
                            
            contadorB1 = 0
            solo = 0
            for x in range(len(codEntrada)):
                if codEntrada[solo] != codSalida[solo]:
                    contadorB1 += 1
                solo += 1


            print('\n\n-Costo Optimo para realizar los cambios-')
            if  voltearF > intercambiarS:
                print('Intercambiar es menor que Voltear: '+str(intercambiarS)+ ' < ' +str(voltearF))
                # priorizaV = True
                costoOptimo = (contadorB1-restCosto) * intercambiarS
                print('Costo: '+ str(costoOptimo))
                # bitacora(codEntrada, codSalida, priorizaV)
            elif intercambiarS > voltearF:
                print('Voltear es menor que Intercambiar: '+str(voltearF)+ ' < '+str(intercambiarS))
                # priorizaV = False
                costoOptimo = contadorB1 * voltearF
                print('Costo: '+str(costoOptimo))
                # bitacora(codEntrada, codSalida, priorizaV)
            elif voltearF == intercambiarS:
                print('Voltear vale lo mismo que Intercambiar: '+ str(voltearF))
                costoOptimo = (contadorB1-restCosto) * voltearF
                print('Costo optimo: '+str(costoOptimo))

            # espera = False
            # print('\n')
        
        elif opcion == 3:
            salir = True
        elif opcion == 4:
            salir = True
        else:
            print ("====Introduce un numero entre 1 y 3====")

        # print ("Fin")
        print("\n ================================================= \n")

def pedirNumeroEntero():

    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('ERROR, introduce un numero entero: ')
    
    return num

def bitacora(codEntrada, codSalida, priorizaV):
    if priorizaV == True:
        print()


def fn_abrirArchivo():
    global ruta
    ruta = filedialog.askopenfilename(title="Abrir", filetypes = (("Unicamente xml", "*.xml"), ("Archivos xml", "*.xml")) )
    


mainQ()

"""

## Contando elementos del xml
print('\nCantidad de elementos del xml:')
print(len(pisos))


# Imprimiendo las cosas en la lista
print('\nimprimiendo lista con sus nodos individuales')
lista1.imprimir_nodosHijo() # Imprimimos la lista de nodos con los nombres
print("----------")

print('\nimprimiendo obtener Todo')
lista1.obtenerTodo() # Imprimimos la lista de nodos con los nombres
# splitCodigos = split()

print("")

"""



