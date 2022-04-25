  //Declaracion de Headers

let headers = new Headers()
headers.append('Content-Type', 'application/json');
headers.append('Accept', 'application/json');
headers.append('Access-Control-Allow-Origin', 'http://35.193.113.191:5000');
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

function convertirdata(medico){
  var data ={
    "NOMBRE":medico.nombrem,
    "APELLIDO":medico.apellidom,
    "FECHA":medico.fecham,
    "SEXO":medico.sexom,
    "USUARIO":medico.userm,
    "CONTRASEÑA":medico.passwordm,
    "ESPECIALIDAD":medico.especialidadm,
    "TELEFONO":medico.telm
  }

  return data

}

function crearpdfm(){
  
  fetch('http://35.193.113.191:5000/obtenermedicos')
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
      "ESPECIALIDAD",
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
    doc.table(2, 1, datos, headers, { autoSize: false });
    doc.save("Medicos.pdf")
  })
}

//

//

function cargarm(){
    let file = document.getElementById("cargam").files[0];
    if (file) {
        let reader = new FileReader();
        reader.readAsText(file, "UTF-8");
        reader.onload = function (evt) {
            let cuerpo = {
                data:evt.target.result
            }
            console.log(JSON.stringify(cuerpo))
            fetch('http://35.193.113.191:5000/cargamedicos', {
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


function modificarMedico(){
  let nombrem_o = document.getElementById("vnombrem");
  let nombrem = document.getElementById("mnombrem");
  let apellidom = document.getElementById("mapellidom");
  let fecham = document.getElementById("mfecham");
  let sexom = document.getElementById("msexom");
  let userm = document.getElementById("muserm");
  let passwordm = document.getElementById("mpasswordm");
  let especialidadm = document.getElementById("mespecialidadm");
  let telm = document.getElementById("mtelm")

  let headers = new Headers();
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');

  let reque = `{
    "nombrem":"${nombrem.value}",
    "apellidom":"${apellidom.value}",
    "fecham":"${fecham.value}",
    "sexom":"${sexom.value}",
    "userm":"${userm.value}",
    "passwordm":"${passwordm.value}",
    "especialidadm":"${especialidadm.value}",
    "telm":"${telm.value}"
  }`

  fetch('http://35.193.113.191:5000/medicos/'+nombrem_o.value, {
    method: 'PUT',
    headers,
    body: reque,
  })
  .then(response => response.json())
  .then(result => {
    console.log('Success:', result);
    actualizar()
    nombrem_o.value=''
    nombrem.value=''
    apellidom.value=''
    sexom.value='Selecciona una opcion'
    userm.value=''
    passwordm.value=''
    especialidadm.value=''
    telm.value=''
  })
  .catch(error => {
    console.error('Error:', error);
  });

  

}


/*function eliminar(libro,autor){
    console.log(libro,autor)
    
    fetch('http://35.193.113.191:5000/medicos/'+libro+'/'+autor,{
        method:'DELETE'
    })
    .then(res => res.text())
    .then(res=> {
        alert(res)
        actualizar()
    })
    
}*/

function eliminar(medico,userm){
  fetch('http://35.193.113.191:5000/medicos/'+medico+'/'+userm,{
  method:'DELETE'
  })
  .then(res => res.text())
  .then(res => {
    alert(res)
    actualizar()
  })
}

function agregarMedico(){
  let nombrem = document.getElementById("nombrem");
  let apellidom = document.getElementById("apellidom");
  let fecham = document.getElementById("fecham");
  let sexom = document.getElementById("sexom");
  let userm = document.getElementById("userm");
  let passwordm = document.getElementById("passwordm");
  let especialidadm = document.getElementById("especialidadm");
  let telm = document.getElementById("telm");
  fetch('http://35.193.113.191:5000/medicos', {
    method: 'POST',
    headers,
    body: `{
        "nombrem":"${nombrem.value}",
        "apellidom":"${apellidom.value}",
        "fecham":"${fecham.value}",
        "sexom":"${sexom.value}",
        "userm":"${userm.value}",
        "passwordm":"${passwordm.value}",
        "especialidadm":"${especialidadm.value}",
        "telm":"${telm.value}"
      }`,
  })
  .then(response => response.json())
  .then(result => {
    console.log('Success:', result);
    actualizar()
    nombrem.value=''
    apellidom.value=''
    sexom.value='Selecciona una opcion'
    userm.value=''
    passwordm.value=''
    especialidadm.value=''
    telm.value=''
  })
  .catch(error => {
    console.error('Error:', error);
  });

}


function actualizar(){
  document.getElementById("cardsc").innerHTML = '';
  let text="";
text = `<table class="table" style="margin=10px">
<thead>
<tr>
<th scope="col">#</th>
<th scope="col">Nombre</th>
<th scope="col">Apellido</th>
<th scope="col">Fecha Nacimiento</th>
<th scope="col">Sexo</th>
<th scope="col">Usuario</th>
<th scope="col">Contraseña</th>
<th scope="col">Especialidad</th>
<th scope="col">Telefono</th>
<th scope="col">Opciones</th>
</tr>
</thead>
<tbody>`

  fetch('http://35.193.113.191:5000/obtenermedicos')
  .then(response => response.json())
  .then(data =>{
      var i;
  
      
      for(i=0;i<data.length;i++){
          text+= `
                  <tr>
                  <th scope="row">${i+1}</th>
                  <td>${data[i].nombrem}</td>
                  <td>${data[i].apellidom}</td>
                  <td>${data[i].fecham}</td>
                  <td>${data[i].sexom}</td>
                  <td>${data[i].userm}</td>
                  <td>${data[i].passwordm}</td>
                  <td>${data[i].especialidadm}</td>
                  <td>${data[i].telm}</td>
                  <td><button href="#" class="btn btn btn-danger" onclick="eliminar('${data[i].nombrem}','${data[i].userm}')">Eliminar</button></td>
                  </tr>
                  `
                  console.log(data[i].nombrem,'prueba')
      }
      text+=`</tbody>
              </table>`
      document.getElementById("cardsc").innerHTML = text;
  });


}



  // Carga medicos
/*
  let text="";
  fetch('http://35.193.113.191:5000/obtenermedicos')
  .then(response => response.json())
  .then(data =>{
      var i;
      for(i=0;i<data.length;i++){
          text+= `<br>
                  <div class="col-sm-5 col-md-5 col-lg-5" style="margin-top: 30px;border-style: dotted;">
                  <div class="card bg-light" style="width: auto;">
                  <div class="card-body">
                      <h4 class="card-title">${data[i].nombrem}</h4>
                      <h4 class="card-title">${data[i].apellidom}</h4>
                      <h4 class="card-title">${data[i].fecham}</h4>
                      <h4 class="card-title">${data[i].sexom}</h4>
                      <h4 class="card-title">${data[i].userm}</h4>
                      <h4 class="card-title">${data[i].passwordm}</h4>
                      <h4 class="card-title">${data[i].telm}</h4>
                      <button href="#" class="btn btn btn-danger" onclick="eliminar('${data[i].nombrem}','${data[i].userm}')">Eliminar</button>
                  </div>
                  </div>
                  </div>
                  <br>`
          console.log(data[i].nombrem,'prueba')
      }
      document.getElementById("cardsc").innerHTML = text;
  });

  */


// Carga de medicos 2.0

let text2=""
text2 = `<table class="table" style="margin=10px">
<thead>
<tr>
<th scope="col">#</th>
<th scope="col">Nombre</th>
<th scope="col">Apellido</th>
<th scope="col">Fecha Nacimiento</th>
<th scope="col">Sexo</th>
<th scope="col">Usuario</th>
<th scope="col">Contraseña</th>
<th scope="col">Especialidad</th>
<th scope="col">Telefono</th>
<th scope="col">Opciones</th>
</tr>
</thead>
<tbody>`

fetch('http://35.193.113.191:5000/obtenermedicos')
.then(response => response.json())
.then(data =>{
    var i;

    
    for(i=0;i<data.length;i++){
        text2+= `
                <tr>
                <th scope="row">${i+1}</th>
                <td>${data[i].nombrem}</td>
                <td>${data[i].apellidom}</td>
                <td>${data[i].fecham}</td>
                <td>${data[i].sexom}</td>
                <td>${data[i].userm}</td>
                <td>${data[i].passwordm}</td>
                <td>${data[i].especialidadm}</td>
                <td>${data[i].telm}</td>
                <td><button href="#" class="btn btn btn-danger" onclick="eliminar('${data[i].nombrem}','${data[i].userm}')">Eliminar</button></td>
                </tr>
                `
    }
    text2+=`</tbody>
            </table>`
    document.getElementById("tablamedicos").innerHTML = text2;
});