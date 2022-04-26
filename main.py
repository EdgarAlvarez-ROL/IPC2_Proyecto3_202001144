from csv import unix_dialect
from queue import PriorityQueue
from xml.dom import minidom
from numpy import TooHardError, delete

from sqlalchemy import null                     

import tkinter
from tkinter import filedialog
import re
import xml.etree.ElementTree as ET

import ListaDoble
import escritorGraphviz
import algoritmo

ciudadx = ListaDoble.Ciudad('','','','','')
listaCiudades = ListaDoble.doubleList()

listMilitares = ListaDoble.Ciudad.lista_Militares()
militar = ListaDoble.unidadMilitar('','','')


listaRobots = ListaDoble.lista_Robots()
robot = ListaDoble.Robot('','','')

# VARIABLES GLOBALES
todo_papa = ''
ruta = ''
list_unidadesTexto = ''
unidadesTexto = ''


def lectorXML(rutanueva):
    global todo_papa, ruta, ciudadx, list_unidadesTexto, unidadesTexto, listMilitares, militar, listaRobots, robot
    ruta = rutanueva

    sub2 = 0

    mydoc = minidom.parse(ruta)            

    ciudades = mydoc.getElementsByTagName('ciudad')      

    """Lo que esta comentado de PRINT NO TOCAR"""
    # Intentando leer los pisos
    for x in ciudades:
        todo_papa=''
        if x.getElementsByTagName("nombre")[0]:
            e_nombre = x.getElementsByTagName('nombre')[0]
            print(e_nombre.nodeName, ':', str.strip(e_nombre.childNodes[0].data))

            filas = e_nombre.getAttribute('filas')
            columnas = e_nombre.getAttribute('columnas')
            # print('Filas: ' + str(filas))
            # print('Filas: ' + str(columnas))
            
            contF = 1
            for filitas in x.getElementsByTagName('fila'):
                n_fila = filitas.getAttribute('numero')
                # print('#fila: '+ str(n_fila) + ' Data: '+  filitas.childNodes[0].data)
                todo_papa += filitas.childNodes[0].data
                contF += 1
            # print(todo_papa)
            
            # e_fila = x.getElementsByTagName('fila')[0]
            # n_fila = e_fila.getAttribute('numero')
            # print('# Fila: ' + n_fila)
            # d_fila = e_fila.childNodes[0].data
            # print(e_fila.nodeName, ':', str(d_fila))

            unidadesTexto = divisorMapeador(todo_papa)
            # print(unidadesTexto)
            nuevaCadena = ''
            for unidades in x.getElementsByTagName('unidadMilitar'):
                n_u_fila = unidades.getAttribute('fila')
                n_u_columna = unidades.getAttribute('columna')
                # print('#fila: '+ str(n_u_fila) + ' #columna: ' + str(n_u_columna) + ' Data: '+  unidades.childNodes[0].data)
                

                militar.fila = n_u_fila
                militar.columna = n_u_columna
                militar.capacidad = unidades.childNodes[0].data
                listMilitares.insertar_final(militar)
                militar = ListaDoble.unidadMilitar('','','')

                
                cont = 0
                for cosas in unidadesTexto[int(n_u_fila)-1]:
                    # print('primero: '+cosas)
                    if cont == (int(n_u_columna)-1):
                        # print(cosas)
                        cosas = 'M'
                        # print(cosas)
                    nuevaCadena += cosas
                    cont+=1
                # cont = 0
                unidadesTexto[int(n_u_fila)-1] = nuevaCadena
                nuevaCadena = ''
                # print(unidadesTexto)
                """"""
                # ARREGLAR
                
            
            ciudadx.listRobots = listMilitares
            # 
            # listMilitares.lista_vacia()

            """"""
            ciudadx.nombre = str.strip(e_nombre.childNodes[0].data)
            ciudadx.filas = filas
            ciudadx.columnas = columnas
            ciudadx.todo_papa = unidadesTexto
            # ciudadx.listRobots = ''
            listaCiudades.insertar_final(ciudadx)            
            ciudadx = ListaDoble.Ciudad('','','','','')
            """"""
                
            listMilitares = ListaDoble.Ciudad.lista_Militares()
               
            """"""
            # list_unidadesTexto += unidadesTexto
            # list_unidadesTexto += ' '
            """"""

            # for unidades in x.getElementsByTagName('unidadMilitar'):
            #     listMilitares.eliminar_final()
        # todo_papa = ''
        print('\nDatos Ciudades correctamente\n')
        
        

    robots = mydoc.getElementsByTagName('robot')      
    for x in robots:
        if x.getElementsByTagName("nombre")[0]:
            e_r_nombre = x.getElementsByTagName('nombre')[0]
            # print(e_r_nombre.nodeName, ':', str.strip(e_r_nombre.childNodes[0].data))

            e_r_tipo = e_r_nombre.getAttribute('tipo')
            e_r_capacidad = e_r_nombre.getAttribute('capacidad')
            # print('Tipo: ' + str(tipo))
            # print('Capacidad: ' + str(capacidad))
            # print('\n')
            """"""
            robot.tipo = str(e_r_tipo)
            robot.capacidad = (e_r_capacidad)
            robot.nombre = (str.strip(e_r_nombre.childNodes[0].data))
            listaRobots.insertar_final(robot)
            robot = ListaDoble.Robot('','','')
            """"""




def divisorMapeador(texto):
   
    d_texto =  texto.split('""')
    caracter = '\"'

    for x in range(len(d_texto)):
        d_texto[x] = d_texto[x].replace(caracter,'')
    
    # print(d_texto)
    return d_texto



def menu():
    global list_unidadesTexto, unidadesTexto, ciudadx
    salir = False

    while not salir:
        print('====================== MENU ======================')
        print ("1. Ingrese la ruta de su archivo XML            |")
        print ("2. Ver Ciudades                                 |")
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
            print('--Escoja una ciudad para ver su informacion--')
            # Mostrar CIUDADES
            namesCiudades = listaCiudades.return_infoEspecifica(1)
            # aver = listaCiudades.return_infoEspecifica(5)
            # print(aver)
            # break

            list_namesCiudades = (namesCiudades).rstrip().split(' ')
            cont = 0
            for x in list_namesCiudades:
                print(str(cont) + ') ' + str(x))
                cont += 1


            cont = 0
            nCiud = input("ingrese el numero de la ciudad: ")
            data_Ciudad = ''
            for x in list_namesCiudades:
                if cont == int(nCiud):
                    data_Ciudad = listaCiudades.return_Data_Ciudad(x)
                    # listicaRobot = 
                cont += 1
            """
            #0 Filas
            #1 Columnas
            #2 Todo_papa
            #3 Lista Militares
            """
            data_Ciudad = (data_Ciudad.rstrip().split('Y'))
            # print(data_Ciudad)

            cont = 1
            for x in data_Ciudad:
                if cont == 1:
                    filas = x   
                elif cont == 2:
                    columnas = x
                elif cont == 3:
                    todo_papa = x
                elif cont == 4:
                    militares = x
                    
                cont += 1

            print('Filas de la Ciudad: ' + filas)
            print('Columnas de la Ciudad: '+ columnas)
            print('')
            todo_papa = todo_papa.replace('\']','') #.split('\', \'')
            todo_papa = todo_papa.replace('[\'','')
            todo_papa = todo_papa.split('\', \'')
            """"""
            listicaMilitares = militares[:-1].split('L')
            cont = 0
            capacidad_enemigos_global = 0
            print('Unidades Militares en la Ciudad')
            for x in listicaMilitares:
                if cont == 0:
                    print('Fila: ' + x)
                    cont += 1
                elif cont == 1:
                    print('Columna: ' + x)
                    cont += 1
                elif cont == 2:
                    print('Capacidad: '+ x)
                    print('')
                    cont = 0

                    capacidad_enemigos_global += int(x)
            """"""
            # print(todo_papa)
            # print(unidadesTexto)
            # unidadesTexto = list_unidadesTexto[nCiud]
            """"""
            escritorGraphviz.crearGraficoEntrada(todo_papa,(filas),(columnas))
            """"""
   
            
            """"""
            # SECCION ROBOTS:
            tiposRobots = listaRobots.return_infoEspecifica_ROBOTS(1)
            list_tRbts = (tiposRobots).rstrip().split(' ')
            cont = 0
            for x in list_tRbts:
                print(str(cont) + ') ' + str(x))
                cont += 1



            cont = 0
            nCiud = input("ingrese el # del Tipo de Robot: ")
            parC = ''
            dif_robots = ''
            for x in list_tRbts:
                if cont == int(nCiud):
                    dif_robots = listaRobots.return_Data_ROBOT(x)


                    if int(nCiud) % 2 == 0:
                        # print("par")
                        parC = 'par'
                    else:
                        # print("impar")
                        parC = 'impar'
                    



                cont += 1


            dif_robots = (dif_robots[:-1].split('Y'))
            print('Escoja su robot: ')

            cont = 0
            for x in dif_robots:
                if x.isnumeric():
                    # cont += -1
                    pass
                elif x!= '0':
                    print(str(cont) + ') ' + str(x))
                cont += 1


            cont = 0
            nCiud = input("Ingrese el numero de su Robot: ")
            capacidad_rR = ''
            for x in dif_robots:
                if cont == int(nCiud):
                    capacidad_rR = listaRobots.return_Data_ROBOT(x)
                    # listicaRobot = 
                cont += 1

            print('Capacidad de su ROBOT: '+capacidad_rR)
            print('')
            """"""
            """"""
            """"""
            #Entrada     
            buscarEntradas(todo_papa)
            print('')
            print('Ingrese las Coordenas de la Entrada: ')
            xEntrada = input("ingrese x: ")
            yEntrada = input("ingrese y: ")
            print('')

            # Fighter o Salvador
            if parC == 'par':
                # enviar capacidad_rR
                buscarRecursos(todo_papa)
                print('Ingrese las Coordenas del Recurso a rescatar: ')
                xRecurso = input("ingrese x: ")
                yRecurso = input("ingrese y: ")
                print('')

                if int(capacidad_rR) >= capacidad_enemigos_global:
                    print('SI')
                    algoritmo.hacerMatrix2(todo_papa, xEntrada, yEntrada, xRecurso, yRecurso, filas , columnas)

                else:
                    print('NO')
                    algoritmo.hacerMatrix3(todo_papa, xEntrada, yEntrada, xRecurso, yRecurso, filas , columnas, listicaMilitares, capacidad_rR)
                    cont = 0
                    suax = 0
                    suay = 0
                    # for x in listicaMilitares:
                    #     if cont == 0:
                    #         # print('Fila: ' + x)
                    #         if yRecurso == x:
                    #             sua = 1
                    #             filaw = x
                    #         cont += 1
                    #     elif cont == 1:
                    #         # print('Columna: ' + x)
                    #         if xRecurso == x:
                    #             sua = 1 
                    #             columnaw = x
                    #         cont += 1
                    #     elif cont == 2:
                    #         if suax == 1 and suay == 1:
                    #             print('Capacidad: '+ x)
                    #             if 

                    #         print('')
                    #         cont = 0

                    #         capacidad_enemigos_global += int(x)
                    

                
            elif parC == 'impar':
                # enviar capacidad_rR con 0
                buscarCiviles(todo_papa)
                print('Ingrese las Coordenas del Civil a rescatar: ')
                xCivil = input("ingrese x: ")
                yCivil = input("ingrese y: ")
                print('')

                algoritmo.hacerMatrix(todo_papa, xEntrada, yEntrada, xCivil, yCivil, filas , columnas)



            
        elif opcion == 3:
            salir = True


  



def fn_abrirArchivo():
    global ruta
    ruta = filedialog.askopenfilename(title="Abrir", filetypes = (("Unicamente xml", "*.xml"), ("Archivos xml", "*.xml")) )
    


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





def buscarEntradas(todo_papa):
    x = 0
    y = 0
    xcua = 0
    ycua = 0
    for cosas in todo_papa:
        
        for xi in cosas:
            if xi == '*':
                pass
            elif xi == ' ':
                pass
            elif xi == 'M':
                pass
            elif xi == 'R':
                pass
            elif xi == 'E':
                xcua = x
                ycua = y
          
                print('ENTRADA: '+ xi)  
                print('x: '+str(xcua)+' y: '+str(ycua))

                x+=1
            elif xi == 'C':
                pass
            x += 1
        x=0       
        y += 1

        


def buscarCiviles(todo_papa):
    x = 0
    y = 0
    xcua = 0
    ycua = 0
    for cosas in todo_papa:
        
        for xi in cosas:
            if xi == '*':
                pass
            elif xi == ' ':
                pass
            elif xi == 'M':
                pass
            elif xi == 'R':
                pass
            elif xi == 'E':
                pass
            elif xi == 'C':
                xcua = x
                ycua = y
          
                print('CIVIL: '+ xi)  
                print('x: '+str(xcua)+' y: '+str(ycua))

                x+=1


            x += 1
        x=0       
        y += 1

     
def buscarRecursos(todo_papa):
    x = 0
    y = 0
    xcua = 0
    ycua = 0
    for cosas in todo_papa:
        
        for xi in cosas:
            if xi == '*':
                pass
            elif xi == ' ':
                pass
            elif xi == 'M':
                pass
            elif xi == 'C':
                pass
            elif xi == 'E':
                pass
            elif xi == 'R':
                xcua = x
                ycua = y
          
                print('RECURSO: '+ xi)  
                print('x: '+str(xcua)+' y: '+str(ycua))

                x+=1


            x += 1
        x=0       
        y += 1




menu()
