let fields = 1;
function add_field(){
  fields++;
  var i = document.createElement("input");
  i.type = "text";
  i.name = "n"+fields.toString();
  i.id = "n"+fields.toString();
  i.required = true;

  var li = document.createElement("Label");
  li.setAttribute("for","n"+fields.toString());
  li.innerHTML = "Name of field:"

    var j=document.createElement("input");
  j.type="Number";
  j.name = "v"+fields.toString();
  j.id = "v"+fields.toString();
  j.step = "0.01";
  j.required = true;

  var lj = document.createElement("Label");
  lj.setAttribute("for","v"+fields.toString());
  lj.innerHTML = "Weight of Field:"


  let f = document.getElementById('form_data');
  var br = document.createElement("br");
  f.appendChild(br);
  f.appendChild(li);   
  f.appendChild(i);
  f.appendChild(lj);     
  f.appendChild(j);
}

function delete_field(){
  let f = document.getElementById('form_data');
  l = f.childNodes.length;
  for(let i=1;i<=5;i++){
    f.removeChild(f.childNodes[l-i]);
  }
}
