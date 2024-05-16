function eliminarPelicula(id){
    Swal.fire({
        title: "¿Está seguro que desea ELIMINAR esta Película?",
        showDenyButton: true,
        confirmButtonText: "SI",
        denyButtonText: "NO",


    }).then((result)=>{
        if(result.isConfirmed){
            location.href = "/eliminarPelicula/" + id
        }
    });
}

function eliminarGenero(objectId) {
    Swal.fire({
        title: "¿Está seguro que desea ELIMINAR este Género?",
        showDenyButton: true,
        confirmButtonText: "SI",
        denyButtonText: "NO",
    }).then((result) => {
        if (result.isConfirmed) {
            location.href = "/eliminarGenero/" + objectId;
        }
    });
}
