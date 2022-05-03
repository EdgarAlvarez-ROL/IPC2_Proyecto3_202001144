  //Declaracion de Headers

let headers = new Headers()
headers.append('Content-Type', 'application/json');
headers.append('Accept', 'application/json');
headers.append('Access-Control-Allow-Origin', 'http://localhost:5000');
headers.append('Access-Control-Allow-Credentials', 'true');
headers.append('GET', 'POST', 'OPTIONS','PUT','DELETE');

//
//PDF
function createHeaders(keys) {
  var result = [];
  for (var i = 0; i < keys.length; i += 1) {
    result.push({
      id: keys[i],
      name: keys[i],
      prompt: keys[i],
      width: 50,
      align: "center",
      padding: 0
    });
  }
  return result;
}

function convertirdata(paciente){
  var data ={
    "NOMBRE":paciente.nombrep,
    "APELLIDO":paciente.apellidop,
    "FECHA":paciente.fechap,
    "SEXO":paciente.sexop,
    "USUARIO":paciente.userp,
    "CONTRASEÑA":paciente.passwordp,
    "TELEFONO":paciente.telp
  }

  return data

}

function crearpdf(){
  
  fetch('http://localhost:5000/obtenerpacientes')
  .then(response => response.json())
  .then(data=>{
    //Declarando los headers
    let headers = createHeaders([
      "NOMBRE",
      "APELLIDO",
      "FECHA",
      "SEXO",
      "USUARIO",
      "CONTRASEÑA",
      "TELEFONO"
    ]);
    // Insertamos la data
    let datos=[]
    for(let i =0;i<data.length;i++){
      datos.push(Object.assign({},convertirdata(data[i])))
    }
    console.log(datos)
    var contentJsPdf = {
      headers,
      datos
  };
    var doc = new jsPDF({ putOnlyUsedFonts: true, orientation: "landscape" });
    doc.table(15, 1, datos, headers, { autoSize: false });
    doc.save("Pacientes.pdf")
  })
}

//

//

function cargar(){
    let file = document.getElementById("carga").files[0];
    if (file) {
        let reader = new FileReader();
        reader.readAsText(file, "UTF-8");
        reader.onload = function (evt) {
            let cuerpo = {
                data:evt.target.result
            }
            // console.log(JSON.stringify(cuerpo))
            fetch('http://localhost:5000/cargaxml', {
            method: 'POST',
            headers,
            body: JSON.stringify(cuerpo),
            })
            .then(response => response.json())
            .then(result => {
              console.log('Success:', result);
              actualizar()
            })
            .catch(error => {
                console.error('Error:', error);
            });

        }
        reader.onerror = function (evt) {
            
        }
    }
}













function modificarPaciente(){
  let nombrep_o = document.getElementById("vnombrep");
  let nombrep = document.getElementById("mnombrep");
  let apellidop = document.getElementById("mapellidop");
  let fechap = document.getElementById("mfechap");
  let sexop = document.getElementById("msexop");
  let userp = document.getElementById("muserp");
  let passwordp = document.getElementById("mpasswordp");
  let telp = document.getElementById("mtelp")

  let headers = new Headers();
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');

  let reque = `{
    "nombrep":"${nombrep.value}",
    "apellidop":"${apellidop.value}",
    "fechap":"${fechap.value}",
    "sexop":"${sexop.value}",
    "userp":"${userp.value}",
    "passwordp":"${passwordp.value}",
    "telp":"${telp.value}"
  }`

  fetch('http://localhost:5000/pacientes/'+nombrep_o.value, {
    method: 'PUT',
    headers,
    body: reque,
  })
  .then(response => response.json())
  .then(result => {
    console.log('Success:', result);
    actualizar()
    nombrep_o.value=''
    nombrep.value=''
    apellidop.value=''
    sexop.value='Selecciona una opcion'
    userp.value=''
    passwordp.value=''
    telp.value=''
  })
  .catch(error => {
    console.error('Error:', error);
  });

  

}


function eliminar(paciente,userp){
  fetch('http://localhost:5000/pacientes/'+paciente+'/'+userp,{
  method:'DELETE'
  })
  .then(res => res.text())
  .then(res => {
    alert(res)
    actualizar()
  })
}

function agregarPaciente(){
  let nombrep = document.getElementById("nombrep");
  let apellidop = document.getElementById("apellidop");
  let fechap = document.getElementById("fechap");
  let sexop = document.getElementById("sexop");
  let userp = document.getElementById("userp");
  let passwordp = document.getElementById("passwordp");
  let telp = document.getElementById("telp");
  fetch('http://localhost:5000/pacientes', {
    method: 'POST',
    headers,
    body: `{
        "nombrep":"${nombrep.value}",
        "apellidop":"${apellidop.value}",
        "fechap":"${fechap.value}",
        "sexop":"${sexop.value}",
        "userp":"${userp.value}",
        "passwordp":"${passwordp.value}",
        "telp":"${telp.value}"
      }`,
  })
  .then(response => response.json())
  .then(result => {
    console.log('Success:', result);
    actualizar()
    nombrep.value=''
    apellidop.value=''
    sexop.value='Selecciona una opcion'
    userp.value=''
    passwordp.value=''
    telp.value=''
  })
  .catch(error => {
    console.error('Error:', error);
  });

}


function actualizar(){
  // document.getElementById("comentarios1").innerHTML = '';
  let text="";
  text = ``

  
  fetch('http://localhost:5000/obtenerEntrada')
  .then(response => response.json())
  .then(data =>{
    var i;
    
    text+= `${data}`
    
    
    document.getElementById("comentarios1").innerHTML = text;
    console.log('actualizar')
    // console.log('ObtenerEntrada Data:',data)

    // alert('Recargue la Pagina porfavor')
});


}



// Carga de Pacientes 2.0

let text2=""
text2 = ``

fetch('http://localhost:5000/obtenerEntrada')
.then(response => response.json())
.then(data =>{
    var i;
    
    text2+= `${data}`
    
    
    document.getElementById("comentarios1").innerHTML = text2;
    // console.log('ObtenerEntrada Data:',data)
    console.log('let entrada cometarios1')

    // alert('Recargue la Pagina porfavor')
});






// CONSULTAR DATA
function consultarData(){
  // document.getElementById("comentarios1").innerHTML = '';
  let textSalida="";
  textSalida = ``

  
  fetch('http://localhost:5000/obtenerDataSalida')
  .then(response => response.json())
  .then(data =>{
    var i;
    
    textSalida+= `${data}`
    
    
    document.getElementById("comentarios2").innerHTML = textSalida;
    console.log('actualizar SALIDA')
    // console.log('ObtenerEntrada Data:',data)

    // alert('Recargue la Pagina porfavor')
});


}





/////////////////////////////////////////////////////////////////////////////////////////////
// Obtener Fechas
function unaFecha(fecha){
  fetch('http://localhost:5000/buscarPorFecha/'+fecha,{
  method:'POST'
  })
  .then(res => res.text())
  .then(res => {
    // alert('Regargue la fecha porfavor')
    // actualizar()
  })
}


function obtenerFechas(){
  document.getElementById("cardsc").innerHTML = '';
  let ftext="";
  ftext = `<table class="table" style="margin=10px">
<thead>
<tr>
<th scope="col">#</th>
<th scope="col">Fecha</th>
<th scope="col">Opciones</th>
</tr>
</thead>
<tbody>`

fetch('http://localhost:5000/obtenerFechas')
  .then(response => response.json())
  .then(data =>{
      var i;
  
      console.log(data)
      for(i=0;i<data.length;i++){
        ftext+= `
                  <tr>
                  <th scope="row">${i+1}</th>
                  <td id="${i+1}">${data[i]}</td>
                  <td><button href="#" class="btn btn btn-danger" onclick="unaFecha('${data[i]}')">Seleccionar</button></td>
                  </tr>
                  `
                  // console.log(data[i].nombree,'prueba')
      }
      ftext+=`</tbody>
              </table>`
      document.getElementById("cardsc").innerHTML = ftext;
      console.log('Click en ObtenerFechas')
  });


}
