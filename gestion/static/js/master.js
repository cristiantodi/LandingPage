function mostrarContenedor() {
    // Mostrar el contenedor para generar una nueva gestión
    var contenedor = document.getElementById("contenedorGestion");
    contenedor.style.display = "block";
}

function cerrarModales() {
    console.log("CANCELAR")
    $('#myModal, #modalSi, #modalNo').modal('hide');
}


//Agrega el siguiente script al final de tu cuerpo HTML antes de cerrar el tag 

document.addEventListener("DOMContentLoaded", function () {
    // Obtiene el elemento donde deseas mostrar la fecha actual y la fecha futura
    var fechaActualElement = document.getElementById("fecha-actual");
    var fechaFuturaElement = document.getElementById("fecha-futura");

    // Obtiene la fecha actual
    var fechaActual = new Date();

    // Suma 3 días
    fechaActual.setDate(fechaActual.getDate() + 3);

    // Verifica si es fin de semana y ajusta la fecha
    while (fechaActual.getDay() === 0 || fechaActual.getDay() === 6) {
        fechaActual.setDate(fechaActual.getDate() + 1);
    }

    // Inserta la fecha actual en el elemento HTML
    var formatoFecha = { year: 'numeric', month: 'long', day: 'numeric' };
    var fechaActualFormateada = fechaActual.toLocaleDateString("es-ES", formatoFecha);
    fechaActualElement.innerText = fechaActualFormateada;

    // Inserta la fecha futura en el elemento HTML
    var fechaFutura = new Date(fechaActual);
    fechaFutura.setDate(fechaFutura.getDate() + 3); // Añade 3 días adicionales
    var fechaFuturaFormateada = fechaFutura.toLocaleDateString("es-ES", formatoFecha);
    fechaFuturaElement.innerText = fechaFuturaFormateada;
});


function enviarDatos() {
    let texto = document.getElementById('texto').value;
    let nombre = document.getElementById('nombre').value;

    // Aquí puedes enviar la información al servidor utilizando AJAX o cualquier otra tecnología de comunicación
}

//----------------------------------------
