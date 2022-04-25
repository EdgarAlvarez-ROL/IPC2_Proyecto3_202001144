import os

def hacerXML_carga(text):
    print ("\nCrear un archivo")
    print ("================")

    file = 'BackEnd0\\xmlDB.xml'

    archivo = open(file, 'w') # abre el archivo datos.txt
    archivo.write(text)
    # print(archivo.readline())
    archivo.close()

def leerXML(file):
    print ("\Leer un archivo")
    print ("================")

    file = 'BackEnd0\\xmlDB.xml'

    archivo = open(file, 'w') # abre el archivo datos.txt
    # archivo.write(text)
    print(archivo)
    archivo.close()