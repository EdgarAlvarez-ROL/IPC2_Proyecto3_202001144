import os
from unicodedata import normalize
import re

def hacerXML_carga(text):
    print ("\nTocaste CARGAR")
    print ("\nCreando un xml Copy del archivo cargado")
    print ("================")
    

               

    # print(nameServicio)
    text = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", normalize( "NFD", text), 0, re.I)
    # -> NFC
    text = normalize( 'NFC', text)


    # print(text)

    file = 'BackEnd0\\xmlCopyEntrada.xml'


    archivo = open(file, 'w') # abre el archivo datos.txt
    archivo.write(text)
    # print(archivo.readline())
    archivo.close()


    # print ("\nCreando un archivo TEXTCOPY")
    # print ("================")

    # file = 'BackEnd0\\xmlDB.txt'

    # archivo = open(file, 'w') # abre el archivo datos.txt
    # archivo.write(text)
    # # print(archivo.readline())
    # archivo.close()