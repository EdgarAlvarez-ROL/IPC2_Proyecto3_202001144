  
from Usuarios import Usuario
from Pacientes import Paciente
from Medicos import Medico
from Enfermeros import Enfermero
from Citas import Cita
from Medicamentos import Medicamento
from Solicitudes import Solicitud
import json
import re


class Gestor:
    def __init__(self):
        self.usuarios =[]
        self.pacientes=[]
        self.medicos=[]
        self.enfermeros=[]
        self.citas=[]
        self.medicamentos=[]
        self.solicitudes=[]
        

        self.pacientes.append(Paciente('Juan','Martinez','02-07-2001','Masculino','jj','1234','42083200'))
        self.medicos.append(Medico('Maria','Lopez','05-12-1999','Femenino','mari','1234','YO QUE SE','12424245'))
        self.enfermeros.append(Enfermero('Fatima','Gutierrez','06-01-2010','Femenino','ff','1234','11111111'))
        self.citas.append(Cita('Pendiente',''))
        self.medicamentos.append(Medicamento('Panadol','Ayuda a la Tos','Q10','2'))
        self.solicitudes.append(Solicitud('fecha','hora','motivo'))


        self.usuarios.append(Usuario('Javier','Golon','1234','admin'))
        self.usuarios.append(Usuario('Edgar','Alvarez','1234','rol'))
        self.usuarios.append(Usuario('Luisa','Ortiz','1234','luitiz'))

    #Create
    def crearUsuario(self,nombre,apellido,password,user):
        self.usuarios.append(Usuario(nombre,apellido,password,user))


    def crearPaciente(self,nombrep,apellidop,fechap,sexop,userp,passwordp,telp):
        self.pacientes.append(Paciente(nombrep,apellidop,fechap,sexop,userp,passwordp,telp)) 


    def crearMedico(self,nombrem,apellidom,fecham,sexom,userm,passwordm,especialidadm,telm):
        self.medicos.append(Medico(nombrem,apellidom,fecham,sexom,userm,passwordm,especialidadm,telm)) 


    def crearEnfermero(self,nombree,apellidoe,fechae,sexoe,usere,passworde,tele):
        self.enfermeros.append(Enfermero(nombree,apellidoe,fechae,sexoe,usere,passworde,tele)) 

    def crearSolicitud(self,fechac,horac,motivoc):
        self.solicitudes.append(Solicitud(fechac,horac,motivoc)) 

    def crearMedicamento(self,nombremed,descripcionmed,preciomed,cantidadmed):
        self.medicamentos.append(Medicamento(nombremed,descripcionmed,preciomed,cantidadmed)) 


    #Read
    def obtener_usuarios(self):
        return json.dumps([ob.__dict__ for ob in self.usuarios])

    def obtener_pacientes(self):
        return json.dumps([ob.__dict__ for ob in self.pacientes])

    def obtener_medicos(self):
        return json.dumps([ob.__dict__ for ob in self.medicos])
   
    def obtener_enfermeros(self):
        return json.dumps([ob.__dict__ for ob in self.enfermeros])

    def obtener_medicamentos(self):
        return json.dumps([ob.__dict__ for ob in self.medicamentos])
   
    def obtener_citas(self):
        return json.dumps([ob.__dict__ for ob in self.citas])

    def obtener_solicitudes(self):
        return json.dumps([ob.__dict__ for ob in self.solicitudes])

    #Update
    def actualizar_paciente(self,nombrep,nombrenuevo,apellidop,fechap,sexop,userp,passwordp,telp):
        for x in self.pacientes:
            if x.nombrep==nombrep:
                self.pacientes[self.pacientes.index(x)]=Paciente(nombrenuevo,apellidop,fechap,sexop,userp,passwordp,telp)
                return True
        return False


    def actualizar_medico(self,nombrem,nombrenuevo,apellidom,fecham,sexom,userm,passwordm,especialidadm,telm):
        for x in self.medicos:
            if x.nombrem==nombrem:
                self.medicos[self.medicos.index(x)]=Medico(nombrenuevo,apellidom,fecham,sexom,userm,passwordm,especialidadm,telm)
                return True
        return False

    def actualizar_enfermero(self,nombree,nombrenuevo,apellidoe,fechae,sexoe,usere,passworde,tele):
        for x in self.enfermeros:
            if x.nombree==nombree:
                self.enfermeros[self.enfermeros.index(x)]=Enfermero(nombrenuevo,apellidoe,fechae,sexoe,usere,passworde,tele)
                return True
        return False

    def actualizar_medicamento(self,nombremed,descripcionmed,preciomed,cantidadmed):
        for x in self.medicamentos:
            if x.nombremed==nombremed:
                self.medicamentos[self.medicamentos.index(x)]=Medicamento(nombremed,descripcionmed,preciomed,cantidadmed)
                return True
        return False


    #Delete
    def eliminar_paciente(self,nombre,autor):
        for x in self.pacientes:
            if x.nombrep==nombre and x.userp == autor:
                self.pacientes.remove(x)
                return True
        return False

    def eliminar_medico(self,nombre,autor):
        for x in self.medicos:
            if x.nombrem==nombre and x.userm == autor:
                self.medicos.remove(x)
                return True
        return False

    def eliminar_enfermero(self,nombre,autor):
        for x in self.enfermeros:
            if x.nombree==nombre and x.usere == autor:
                self.enfermeros.remove(x)
                return True
        return False

    def eliminar_solicitud(self,nombre,autor):
        for x in self.solicitudes:
            if x.fechac==nombre and x.horac==autor:
                self.solicitudes.remove(x)
                return True
        return False


    def eliminar_medicamentos(self,nombre,autor):
        for x in self.medicamentos:
            if x.nombremed==nombre and x.preciomed==autor:
                self.medicamentos.remove(x)
                return True
        return False

    #Iniciar Sesion
    def iniciar_sesion(self,user,password):
        for x in self.usuarios:
            if (x.password==password and x.user==user.lower()):
                return json.dumps(x.__dict__)
            else:
                for x in self.pacientes:
                    if (x.passwordp==password and x.userp==user.lower()):
                      return json.dumps(x.__dict__)
                    else:
                        for x in self.enfermeros:
                            if (x.passworde==password and x.usere==user.lower()):
                                return json.dumps(x.__dict__)
                            else:
                                 for x in self.medicos:
                                      if (x.passwordm==password and x.userm==user.lower()):
                                        return json.dumps(x.__dict__)
        return '{"nombre":"false"}'

    



    #Registrar
    def registrar_usuario(self,nombre,apellido,password,user):
        self.usuarios.append(Usuario(nombre,apellido,password,user))

    def registrar_paciente(self,nombrep,apellidop,fechap,sexop,userp,passwordp,telp):
        self.pacientes.append(Paciente(nombrep,apellidop,fechap,sexop,userp,passwordp,telp)) 

    def registrar_medico(self,nombrem,apellidom,fecham,sexom,userm,passwordm,especialidadm,telm):
        self.medicos.append(Medico(nombrem,apellidom,fecham,sexom,userm,passwordm,especialidadm,telm)) 

    def registrar_enfermero(self,nombree,apellidoe,fechae,sexoe,usere,passworde,tele):
        self.enfermeros.append(Enfermero(nombree,apellidoe,fechae,sexoe,usere,passworde,tele)) 

    def registrar_solicitud(self,fechac,horac,motivoc):
        self.solicitudes.append(Solicitud(fechac,horac,motivoc)) 

    def registrar_medicamento(self,nombremed,descripcionmed,preciomed,cantidadmed):
        self.medicamentos.append(Medicamento(nombremed,descripcionmed,preciomed,cantidadmed)) 


    #Carga Masiva
    def cargamasiva(self,data):
        hola = re.split('\n',data)
        print(hola[0])
        i=1
        while i < len(hola):
            texto = re.split(',',hola[i])
            self.crearPaciente(texto[0],texto[1],texto[2],texto[3],texto[4],texto[5],texto[6])
            i = i+1 


    def cargamasivam(self,data):
        hola = re.split('\n',data)
        print(hola[0])
        i=1
        while i < len(hola):
            texto = re.split(',',hola[i])
            self.crearMedico(texto[0],texto[1],texto[2],texto[3],texto[4],texto[5],texto[6],texto[7])
            i = i+1 


    def cargamasivae(self,data):
        hola = re.split('\n',data)
        print(hola[0])
        i=1
        while i < len(hola):
            texto = re.split(',',hola[i])
            self.crearEnfermero(texto[0],texto[1],texto[2],texto[3],texto[4],texto[5],texto[6])
            i = i+1 

            

    def cargamasivamed(self,data):
        hola = re.split('\n',data)
        print(hola[0])
        i=1
        while i < len(hola):
            texto = re.split(',',hola[i])
            self.crearMedicamento(texto[0],texto[1],texto[2],texto[3])
            i = i+1 