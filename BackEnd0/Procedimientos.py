import os

def hacerXML_carga(text):
    print ("\nCreando un archivo XMLCOPY")
    print ("================")

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
