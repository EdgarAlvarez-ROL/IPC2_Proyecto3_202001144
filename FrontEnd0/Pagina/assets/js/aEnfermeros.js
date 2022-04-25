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

function convertirdata(enfermero){
  var data ={
    "NOMBRE":enfermero.nombree,
    "APELLIDO":enfermero.apellidoe,
    "FECHA":enfermero.fechae,
    "SEXO":enfermero.sexoe,
    "USUARIO":enfermero.usere,
    "CONTRASEÑA":enfermero.passworde,
    "TELEFONO":enfermero.tele
  }

  return data

}

function crearpdfm(){
  
  fetch('http://35.193.113.191:5000/obtenerenfermeros')
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
    doc.table(2, 1, datos, headers, { autoSize: false });
    doc.save("Enfermeros.pdf")
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
            fetch('http://35.193.113.191:5000/cargaenfermeros', {
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


function modificarEnfermero(){
  let nombree_o = document.getElementById("vnombree");
  let nombree = document.getElementById("mnombree");
  let apellidoe = document.getElementById("mapellidoe");
  let fechae = document.getElementById("mfechae");
  let sexoe = document.getElementById("msexoe");
  let usere = document.getElementById("musere");
  let passworde = document.getElementById("mpassworde");
  let tele = document.getElementById("mtele")

  let headers = new Headers();
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');


    let reque = `{
      "nombree":"${nombree.value}",
      "apellidoe":"${apellidoe.value}",
      "fechae":"${fechae.value}",
      "sexoe":"${sexoe.value}",
      "usere":"${usere.value}",
      "passworde":"${passworde.value}",
      "tele":"${tele.value}"
    }`
  
    fetch('http://35.193.113.191:5000/enfermeros/'+nombree_o.value, {
    method: 'PUT',
    headers,
    body: reque,
  })
  .then(response => response.json())
  .then(result => {
    console.log('Success:', result);
    actualizar()
    nombree_o.value=''
    nombree.value=''
    apellidoe.value=''
    sexoe.value='Selecciona una opcion'
    usere.value=''
    passworde.value=''
    tele.value=''
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

function eliminar(enfermero,usere){
  fetch('http://35.193.113.191:5000/enfermeros/'+enfermero+'/'+usere,{
  method:'DELETE'
  })
  .then(res => res.text())
  .then(res => {
    alert(res)
    actualizar()
  })
}

function agregarEnfermero(){
  let nombree = document.getElementById("nombree");
  let apellidoe = document.getElementById("apellidoe");
  let fechae = document.getElementById("fechae");
  let sexoe = document.getElementById("sexoe");
  let usere = document.getElementById("usere");
  let passworde = document.getElementById("passworde");
  let tele = document.getElementById("tele");
  fetch('http://35.193.113.191:5000/enfermeros', {
    method: 'POST',
    headers,
    body: `{
        "nombree":"${nombree.value}",
        "apellidoe":"${apellidoe.value}",
        "fechae":"${fechae.value}",
        "sexoe":"${sexoe.value}",
        "usere":"${usere.value}",
        "passworde":"${passworde.value}",
        "tele":"${tele.value}"
      }`,
  })
  .then(response => response.json())
  .then(result => {
    console.log('Success:', result);
    actualizar()
    nombree.value=''
    apellidoe.value=''
    sexoe.value='Selecciona una opcion'
    usere.value=''
    passworde.value=''
    tele.value=''
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
<th scope="col">Telefono</th>
<th scope="col">Opciones</th>
</tr>
</thead>
<tbody>`

  fetch('http://35.193.113.191:5000/obtenerenfermeros')
  .then(response => response.json())
  .then(data =>{
      var i;
  
      
      for(i=0;i<data.length;i++){
          text+= `
                  <tr>
                  <th scope="row">${i+1}</th>
                  <td>${data[i].nombree}</td>
                  <td>${data[i].apellidoe}</td>
                  <td>${data[i].fechae}</td>
                  <td>${data[i].sexoe}</td>
                  <td>${data[i].usere}</td>
                  <td>${data[i].passworde}</td>
                  <td>${data[i].tele}</td>
                  <td><button href="#" class="btn btn btn-danger" onclick="eliminar('${data[i].nombree}','${data[i].usere}')">Eliminar</button></td>
                  </tr>
                  `
                  console.log(data[i].nombree,'prueba')
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
                      <h4 class="card-title">${data[i].nombree}</h4>
                      <h4 class="card-title">${data[i].apellidoe}</h4>
                      <h4 class="card-title">${data[i].fechae}</h4>
                      <h4 class="card-title">${data[i].sexoe}</h4>
                      <h4 class="card-title">${data[i].usere}</h4>
                      <h4 class="card-title">${data[i].passworde}</h4>
                      <h4 class="card-title">${data[i].tele}</h4>
                      <button href="#" class="btn btn btn-danger" onclick="eliminar('${data[i].nombree}','${data[i].usere}')">Eliminar</button>
                  </div>
                  </div>
                  </div>
                  <br>`
          console.log(data[i].nombree,'prueba')
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
<th scope="col">Telefono</th>
<th scope="col">Opciones</th>
</tr>
</thead>
<tbody>`

fetch('http://35.193.113.191:5000/obtenerenfermeros')
.then(response => response.json())
.then(data =>{
    var i;

    
    for(i=0;i<data.length;i++){
        text2+= `
                <tr>
                <th scope="row">${i+1}</th>
                <td>${data[i].nombree}</td>
                <td>${data[i].apellidoe}</td>
                <td>${data[i].fechae}</td>
                <td>${data[i].sexoe}</td>
                <td>${data[i].usere}</td>
                <td>${data[i].passworde}</td>
                <td>${data[i].tele}</td>
                <td><button href="#" class="btn btn btn-danger" onclick="eliminar('${data[i].nombree}','${data[i].usere}')">Eliminar</button></td>
                </tr>
                `
    }
    text2+=`</tbody>
            </table>`
    document.getElementById("tablamedicos").innerHTML = text2;
});