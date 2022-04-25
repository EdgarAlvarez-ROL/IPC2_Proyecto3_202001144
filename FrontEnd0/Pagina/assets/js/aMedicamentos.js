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

function convertirdata(medicamento){
  var data ={
    "NOMBRE":medicamento.nombremed,
    "DESCRIPCION":medicamento.descripcionmed,
    "PRECIO":medicamento.preciomed,
    "CANTIDAD":medicamento.cantidadmed
  }

  return data

}

function crearpdfmedicamentos(){
  
  fetch('http://35.193.113.191:5000/obtenermedicamentos')
  .then(response => response.json())
  .then(data=>{
    //Declarando los headers
    let headers = createHeaders([
      "NOMBRE",
      "DESCRIPCION",
      "PRECIO",
      "CANTIDAD"
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
    doc.table(25, 1, datos, headers, { autoSize: false });
    doc.save("Medicamentos.pdf")
  })
}

//

//

function cargarMed(){
    let file = document.getElementById("cargam").files[0];
    if (file) {
        let reader = new FileReader();
        reader.readAsText(file, "UTF-8");
        reader.onload = function (evt) {
            let cuerpo = {
                data:evt.target.result
            }
            console.log(JSON.stringify(cuerpo))
            fetch('http://35.193.113.191:5000/cargamedicamentos', {
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


function modificar(){
  let nombree_o = document.getElementById("vnombrem");
  let nombremed = document.getElementById("bnombremed");
  let descripcionmed = document.getElementById("bdescripcionmed");
  let preciomed= document.getElementById("bpreciomed");
  let cantidadmed = document.getElementById("bcantidadmed");

  let headers = new Headers();
    headers.append('Content-Type', 'application/json');
    headers.append('Accept', 'application/json');


    let reque = `{
      "nombremed":"${nombremed.value}",
      "descripcionmed":"${descripcionmed.value}",
      "preciomed":"${preciomed.value}",
      "cantidadmed":"${cantidadmed.value}"
    }`
  
    fetch('http://35.193.113.191:5000/medicamentos/'+nombree_o.value, {
    method: 'PUT',
    headers,
    body: reque,
  })
  .then(response => response.json())
  .then(result => {
    console.log('Success:', result);
    actualizar()
    nombree_o.value=''
    nombremed.value=''
    descripcionmed.value=''
    preciomed.value=''
    cantidadmed.value=''
  })
  .catch(error => {
    console.error('Error:', error);
  });

  

}



function eliminar(nombremed,preciomed){
  fetch('http://35.193.113.191:5000/medicamentos/'+nombremed+'/'+preciomed,{
  method:'DELETE'
  })
  .then(res => res.text())
  .then(res => {
    alert(res)
    actualizar()
  })
}

function agregar(){
  let nombremed = document.getElementById("nombremed");
  let descripcionmed = document.getElementById("descripcionmed");
  let preciomed = document.getElementById("preciomed");
  let cantidadmed = document.getElementById("cantidadmed");
  fetch('http://35.193.113.191:5000/medicamentos', {
    method: 'POST',
    headers,
    body: `{
        "nombremed":"${nombremed.value}",
        "descripcionmed":"${descripcionmed.value}",
        "preciomed":"${preciomed.value}",
        "cantidadmed":"${cantidadmed.value}"
      }`,
  })
  .then(response => response.json())
  .then(result => {
    console.log('Success:', result);
    actualizar()
    nombremed.value=''
    descripcionmed.value=''
    preciomed.value=''
    cantidadmed.value=''
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
<th scope="col">Descripcion</th>
<th scope="col">Precio</th>
<th scope="col">Cantidad</th>
<th scope="col">Opciones</th>
</tr>
</thead>
<tbody>`

  fetch('http://35.193.113.191:5000/obtenermedicamentos')
  .then(response => response.json())
  .then(data =>{
      var i;
  
      
      for(i=0;i<data.length;i++){
          text+= `
                  <tr>
                  <th scope="row">${i+1}</th>
                  <td>${data[i].nombremed}</td>
                  <td>${data[i].descripcionmed}</td>
                  <td>${data[i].preciomed}</td>
                  <td>${data[i].cantidadmed}</td>
                  <td><button href="#" class="btn btn btn-danger" onclick="eliminar('${data[i].nombremed}','${data[i].preciomed}')">Eliminar</button></td>
                  </tr>
                  `
                  console.log(data[i].nombremed,'NICE')
      }
      text+=`</tbody>
              </table>`
      document.getElementById("cardsc").innerHTML = text;
  });


}


let text4=""
text4 = `<table class="table" style="margin=10px">
<thead>
<tr>
<th scope="col">#</th>
<th scope="col">Nombre</th>
<th scope="col">Descripcion</th>
<th scope="col">Precio</th>
<th scope="col">Cantidad en el Almacen</th>
<th scope="col">Opciones</th>
</tr>
</thead>
<tbody>`

fetch('http://35.193.113.191:5000/obtenermedicamentos')
.then(response => response.json())
.then(data =>{
    var i;
    for(i=0;i<data.length;i++){
      text4+= `
                <tr>
                <th scope="row">${i+1}</th>
                <td>${data[i].nombremed}</td>
                <td>${data[i].descripcionmed}</td>
                <td>${data[i].preciomed}</td>
                <td>${data[i].cantidadmed}</td>
                <td><button href="#" class="btn btn btn-danger" onclick="eliminar('${data[i].nombremed}','${data[i].preciomed}')">Eliminar</button></td>
                </tr>
                `
    }
    text4+=`</tbody>
            </table>`
    document.getElementById("tabla").innerHTML = text4;
});

