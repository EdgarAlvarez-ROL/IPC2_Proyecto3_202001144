import json
import os
# import os
import Procedimientos
import analizadorXML
import consultar_por_fecha
import generadrPDF

class Gestor:
    def __init__(self):
        self.text = ''
        self.textSalida = ''
        self.listEmpresas = ''
        self.listFechas = ''

    #Create
    def recibirXML(self, data):
        self.text = data
        Procedimientos.hacerXML_carga(data)
        # print('Esta es la info del xml: '+self.text)
        

    def analizarXML(self):
        analizadorXML.lectorXML('BackEnd0\\xmlCopyEntrada.xml')
        
        file = 'BackEnd0\\request.xml'

        archivo = open(file, 'r') # abre el archivo datos.txt
        self.textSalida = archivo.readlines()
        # print(archivo.readline())
        archivo.close()
        return json.dumps(self.textSalida)



    def consultar_por_fecha(self,nFecha):
        consultar_por_fecha.lectorXML('BackEnd0\\xmlCopyEntrada.xml',nFecha)

        file = 'BackEnd0\\request.xml'

        archivo = open(file, 'r') # abre el archivo datos.txt
        self.textSalida = archivo.readlines()
        # print(archivo.readline())
        archivo.close()
        return json.dumps(self.textSalida)



    def rangofechas(self,fechaA,fechaB):
        print()
    # def crearUsuario(self,nombre,apellido,password,user):
    #     self.usuarios.append(Usuario(nombre,apellido,password,user))
    def hacerPDF(self):
        generadrPDF.recibirText()


    #Read
    def obtenerDataXML(self):
        return self.text

    def obtener_entrada(self):
        return  json.dumps(self.text)


    # def obtener_usuarios(self):
    #     return json.dumps([ob.__dict__ for ob in self.usuarios])

    


    #Update
    # def actualizar_medico(self,nombrem,nombrenuevo,apellidom,fecham,sexom,userm,passwordm,especialidadm,telm):
    #     for x in self.medicos:
    #         if x.nombrem==nombrem:
    #             self.medicos[self.medicos.index(x)]=Medico(nombrenuevo,apellidom,fecham,sexom,userm,passwordm,especialidadm,telm)
    #             return True
    #     return False



    #Delete
    # def eliminar_paciente(self,nombre,autor):
    #     for x in self.pacientes:
    #         if x.nombrep==nombre and x.userp == autor:
    #             self.pacientes.remove(x)
    #             return True
    #     return False



    #Iniciar Sesion
    # def iniciar_sesion(self,user,password):
    #     for x in self.usuarios:
    #         if (x.password==password and x.user==user.lower()):
    #             return json.dumps(x.__dict__)
    #         else:
    #             for x in self.pacientes:
    #                 if (x.passwordp==password and x.userp==user.lower()):
    #                   return json.dumps(x.__dict__)
    #                 else:
    #                     for x in self.enfermeros:
    #                         if (x.passworde==password and x.usere==user.lower()):
    #                             return json.dumps(x.__dict__)
    #                         else:
    #                              for x in self.medicos:
    #                                   if (x.passwordm==password and x.userm==user.lower()):
    #                                     return json.dumps(x.__dict__)
    #     return '{"nombre":"false"}'

    



    #Registrar
    # def registrar_usuario(self,nombre,apellido,password,user):
    #     self.usuarios.append(Usuario(nombre,apellido,password,user))


    #Carga Masiva
    # def cargamasiva(self,data):
    #     hola = re.split('\n',data)
    #     print(hola[0])
    #     i=1
    #     while i < len(hola):
    #         texto = re.split(',',hola[i])
    #         self.crearPaciente(texto[0],texto[1],texto[2],texto[3],texto[4],texto[5],texto[6])
    #         i = i+1 


    def cargaXML(self,data):
        self.recibirXML(data)
    


    # analizarXML()