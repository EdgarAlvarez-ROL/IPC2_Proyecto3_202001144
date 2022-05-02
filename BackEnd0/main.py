#Server: localhost:5000
#Importaciones de Flask
from flask import Flask,  render_template, request, jsonify
from flask_cors import CORS
from Gestor import Gestor
import xmltodict

#Crear la app
app = Flask(__name__)
app.config["DEBUG"] = True

CORS(app)

gestor =  Gestor()


# EndPoints
@app.route('/',methods=['GET'])
def home():
    return 'Funciona esta Mierda UwU'


@app.route('/cargaxml',methods=['POST'])
def recibexml():
    dato = request.json
    gestor.recibirXML(dato['data'])

    # content = xmltodict.parse(request.get_data())
    # print (content)
    return '{"data":"XML Cargado"}'


@app.route('/obtenerEntrada')
def obtener_enntrada():
    return gestor.obtener_entrada()


@app.route('/obtenerDataSalida')
def Consultar_Data():
    return gestor.analizarXML()






@app.route('/usuarios',methods=['POST'])
def crearUsuario():
    dato = request.json
    gestor.crearUsuario(dato['nombre'],dato['apellido'],dato['contraseña'],dato['usuario'])
    return '{"Estado":"Usuario Creado"}'


@app.route('/pacientes',methods=['POST'])
def crearPaciente():
    datop = request.json
    gestor.crearPaciente(datop['nombrep'],datop['apellidop'],datop['fechap'],datop['sexop'],datop['userp'],datop['passwordp'],datop['telp'])
    return '{"Estado":"Paciente Creado"}'

@app.route('/pacientes/<nombrep>/<userp>',methods=['DELETE'])
def eliminar_paciente(nombrep,userp):
    if(gestor.eliminar_paciente(nombrep,userp)):
        return '{"Paciente":"Eliminado"}'
    return '{"data":"Error"}'

@app.route('/pacientes/<mnombrep>',methods=['PUT'])
def actualizarpaciente(mnombrep):
    datop = request.json
    if gestor.actualizar_paciente(mnombrep,datop['nombrep'],datop['apellidop'],datop['fechap'],datop['sexop'],datop['userp'],datop['passwordp'],datop['telp']):
        return '{"data":"Actualizado"}'
    return '{"data":"Error"}'






#MEDICOS
@app.route('/medicos',methods=['POST'])
def crearMedico():
    datom = request.json
    gestor.crearMedico(datom['nombrem'],datom['apellidom'],datom['fecham'],datom['sexom'],datom['userm'],datom['passwordm'],datom['especialidadm'],datom['telm'])
    return '{"Estado":"Medico Creado"}'

@app.route('/medicos/<nombrem>/<userm>',methods=['DELETE'])
def eliminar_medico(nombrem,userm):
    if(gestor.eliminar_medico(nombrem,userm)):
        return '{"Medico":"Eliminado"}'
    return '{"data":"Error"}'

@app.route('/medicos/<mnombrem>',methods=['PUT'])
def actualizarmedico(mnombrem):
    datom = request.json
    if gestor.actualizar_medico(mnombrem,datom['nombrem'],datom['apellidom'],datom['fecham'],datom['sexom'],datom['userm'],datom['passwordm'],datom['especialidadm'],datom['telm']):
        return '{"data":"Actualizado"}'
    return '{"data":"Error"}'


@app.route('/obtenermedicos')
def obtener_medicos():
    return gestor.obtener_medicos()

@app.route('/cargamedicos',methods=['POST'])
def cargam():
    datom = request.json
    gestor.cargamasivam(datom['data'])
    return '{"data":"Cargados"}'
#






#ENFERMERO
@app.route('/enfermeros',methods=['POST'])
def crearEnfermero():
    datoe = request.json
    gestor.crearEnfermero(datoe['nombree'],datoe['apellidoe'],datoe['fechae'],datoe['sexoe'],datoe['usere'],datoe['passworde'],datoe['tele'])
    return '{"Estado":"Enfermero Creado"}'

@app.route('/enfermeros/<nombree>/<usere>',methods=['DELETE'])
def eliminar_enfermero(nombree,usere):
    if(gestor.eliminar_enfermero(nombree,usere)):
        return '{"Enfermero":"Eliminado"}'
    return '{"data":"Error"}'

@app.route('/enfermeros/<mnombree>',methods=['PUT'])
def actualizarenfermero(mnombree):
    datom = request.json
    if gestor.actualizar_enfermero(mnombree,datom['nombree'],datom['apellidoe'],datom['fechae'],datom['sexoe'],datom['usere'],datom['passworde'],datom['tele']):
        return '{"data":"Actualizado"}'
    return '{"data":"Error"}'


@app.route('/obtenerenfermeros')
def obtener_enfermeros():
    return gestor.obtener_enfermeros()

@app.route('/cargaenfermeros',methods=['POST'])
def cargae():
    datoe = request.json
    gestor.cargamasivae(datoe['data'])
    return '{"data":"Cargados"}'
#





@app.route('/obtenerpacientes')
def obtener_pacientes():
    return gestor.obtener_pacientes()

    





@app.route('/login/<user>/<password>')
def login(user,password):
    print('entra')
    return gestor.iniciar_sesion(user,password)





@app.route('/registro',methods=['POST'])
def registrard():
    dato = request.json
    gestor.registrar_usuario(dato['nombre'],dato['apellido'],dato['password'],dato['user'])    
    return '{"data":"Creado"}'


@app.route('/cargapacientes',methods=['POST'])
def carga():
    dato = request.json
    gestor.cargamasiva(dato['data'])
    return '{"data":"Cargados"}'




#CITAS
@app.route('/obtenercitas')
def obtener_citas():
    return gestor.obtener_citas()
#

#MEDICAMENTOS
@app.route('/medicamentos',methods=['POST'])
def crearMedicamento():
    datom = request.json
    gestor.crearMedicamento(datom['nombremed'],datom['descripcionmed'],datom['preciomed'],datom['cantidadmed'])
    return '{"Estado":"Medicamento Creado"}'

@app.route('/obtenermedicamentos')
def obtener_medicamentos():
    return gestor.obtener_medicamentos()

@app.route('/medicamentos/<nombremed>',methods=['PUT'])
def actualizarmedicamento(nombremed):
    datom = request.json
    if gestor.actualizar_medicamento(nombremed,datom['descripcionmed'],datom['preciomed'],datom['cantidadmed']):
        return '{"data":"Actualizado"}'
    return '{"data":"Error"}'

@app.route('/cargamedicamentos',methods=['POST'])
def cargamed():
    datoe = request.json
    gestor.cargamasivamed(datoe['data'])
    return '{"data":"Cargados"}'

    
@app.route('/medicamentos/<nombremed>/<preciomed>',methods=['DELETE'])
def eliminar_medicamentos(nombremed,preciomed):
    if(gestor.eliminar_medicamentos(nombremed,preciomed)):
        return '{"Medicina":"Eliminado"}'
    return '{"data":"Error"}'

#


#Solicitud
@app.route('/solicitudes',methods=['POST'])
def crearSolicitud():
    datoc = request.json
    gestor.crearSolicitud(datoc['fechac'],datoc['horac'],datoc['motivoc'])
    return '{"Estado":"Solicitud Creada"}'

@app.route('/solicitudes/<fechac>/<horac>',methods=['DELETE'])
def eliminar_solicitud(fechac,horac):
    if(gestor.eliminar_solicitud(fechac,horac)):
        return '{"Solicitud":"Eliminado"}'
    return '{"data":"Error"}'

@app.route('/obtenersolicitudes')
def obtener_solicitudes():
    return gestor.obtener_solicitudes()
#


#INICIAR EL SERVIDOR
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)

