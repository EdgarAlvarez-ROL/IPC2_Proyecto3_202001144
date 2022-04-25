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
            console.log(JSON.stringify(cuerpo))
            fetch('http://localhost:5000/cargaxml', {
            method: 'POST',
            headers,
            body: JSON.stringify(cuerpo),
            })
            .then(response => response.json())
            .then(result => {
              console.log('Success:', result);
              // actualizar()
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


// function actualizar(){
//   document.getElementById("cardsc").innerHTML = '';
//   let text="";
// text = `<table class="table" style="margin=10px">
// <thead>
// <tr>
// <th scope="col">#</th>
// <th scope="col">Nombre</th>
// <th scope="col">Apellido</th>
// <th scope="col">Fecha Nacimiento</th>
// <th scope="col">Sexo</th>
// <th scope="col">Usuario</th>
// <th scope="col">Contraseña</th>
// <th scope="col">Telefono</th>
// <th scope="col">Opciones</th>
// </tr>
// </thead>
// <tbody>`

//   fetch('http://localhost:5000/obtenerpacientes')
//   .then(response => response.json())
//   .then(data =>{
//       var i;
  
      
//       for(i=0;i<data.length;i++){
//           text+= `
//                   <tr>
//                   <th scope="row">${i+1}</th>
//                   <td>${data[i].nombrep}</td>
//                   <td>${data[i].apellidop}</td>
//                   <td>${data[i].fechap}</td>
//                   <td>${data[i].sexop}</td>
//                   <td>${data[i].userp}</td>
//                   <td>${data[i].passwordp}</td>
//                   <td>${data[i].telp}</td>
//                   <td><button href="#" class="btn btn btn-danger" onclick="eliminar('${data[i].nombrep}','${data[i].userp}')">Eliminar</button></td>
//                   </tr>
//                   `
//                   console.log(data[i].nombrep,'prueba')
//       }
//       text+=`</tbody>
//               </table>`
//       document.getElementById("cardsc").innerHTML = text;
//   });


// }




// Carga de Pacientes 2.0

// let text2=""
// text2 = `<table class="table" style="margin=10px">
// <thead>
// <tr>
// <th scope="col">#</th>
// <th scope="col">Nombre</th>
// <th scope="col">Apellido</th>
// <th scope="col">Fecha Nacimiento</th>
// <th scope="col">Sexo</th>
// <th scope="col">Usuario</th>
// <th scope="col">Contraseña</th>
// <th scope="col">Telefono</th>
// <th scope="col">Opciones</th>
// </tr>
// </thead>
// <tbody>`

// fetch('http://localhost:5000/obtenerpacientes')
// .then(response => response.json())
// .then(data =>{
//     var i;

    
//     for(i=0;i<data.length;i++){
//         text2+= `
//                 <tr>
//                 <th scope="row">${i+1}</th>
//                 <td>${data[i].nombrep}</td>
//                 <td>${data[i].apellidop}</td>
//                 <td>${data[i].fechap}</td>
//                 <td>${data[i].sexop}</td>
//                 <td>${data[i].userp}</td>
//                 <td>${data[i].passwordp}</td>
//                 <td>${data[i].telp}</td>
//                 <td><button href="#" class="btn btn btn-danger" onclick="eliminar('${data[i].nombrep}','${data[i].userp}')">Eliminar</button></td>
//                 </tr>
//                 `
//     }
//     text2+=`</tbody>
//             </table>`
//     document.getElementById("tablapacientes").innerHTML = text2;
// });