function buscar(){
    
    var name = document.getElementById("inlineFormInputName").value;
    var doc = document.getElementById("inlineFormInputDocument").value;

    if (name=="" && doc=="") {
        alert("campo vacio");
    }else{
        document.getElementById("contentBuscar").style.display="block";
    }
    
}

function eliminar(){
        
}

