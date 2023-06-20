//Validación de formulario: Contacto
$(function(){
    $("#mi-formulario").validate({
        rules:{     //Inicio rules
            nombre:{
                required: true,
                minlength: 2
            },
            apellido:{
                required: true,
                minlength: 2
            },
            correo:{
                required: true,
                email: true
            },
            telefono: {
                required: true,
                minlength: 9,
                maxlength: 9,
                digits: true
            },
            mensaje:{
                required: true,
                minlength: 50
            }
        },      //Fin de rules
        messages:{      //Inicio mensajes
            nombre: {
                required: 'Ingrese su nombre',
                minlength: 'Nombre no cumple con los requisitos mínimos'
            },
            apellido: {
                required: 'Ingrese su apellido',
                minlength: 'Apellido no cumple con los requisitos mínimos'
            },
            correo: {
                required: 'Ingrese su correo electrónico',
                email: 'Correo no cumple con los requisitos mínimos'
            },
            telefono: {
                required: 'Ingresa tu número de teléfono',
                minlength: 'El número debe tener 9 dígitos',
                maxlength: 'El número debe tener 9 dígitos',
                digits: 'Solo se permiten dígitos'
            },
            mensaje: {
                required: 'Ingrese su mensaje',
                minlength: 'El mensaje debe tener a lo menos 50 carácteres'
            }
        }       //Fin mensajes
    });
});

//Validación de formulario: Crear producto
$(function(){
    $("#mi-formulario2").validate({
        rules:{     //Inicio rules
            id:{
                required: true,
                digits: true
            },
            nombre:{
                required: true,
                minlength: 2,
                maxlength: 50
            },
            descripcion:{
                maxlength: 100
            },
            precio:{
                required: true,
                digits: true,
                maxlength: 10
            },
            stock:{
                required: true,
                digits: true,
                maxlength: 6
            },
            imagen:{
                required: false
            }
        },      //Fin de rules
        messages:{      //Inicio mensajes
            id: {
                required: 'Ingrese el ID del producto',
                digits: 'Solo se permiten dígitos'
            },
            nombre: {
                required: 'Ingrese el nombre del producto',
                minlength: 'Nombre no cumple con los requisitos mínimos',
                maxlength: 'Nombre no cumple con los requisitos máximos'
            },
            descripcion: {
                maxlength: 'Descripción no cumple con los requisitos máximos'
            },
            precio: {
                required: 'Ingrese el precio del producto',
                digits: 'Solo se permiten dígitos',
                maxlength: 'Precio no cumple con los requisitos máximos'
            },
            stock: {
                required: 'Ingrese el stock del producto',
                digits: 'Solo se permiten dígitos',
                maxlength: 'Stock no cumple con los requisitos máximos'
            }
        }       //Fin mensajes
    });
});

// Hora actual
function actualizarHora() {
    const fecha = new Date();
    const hora = fecha.getHours();
    const minutos = fecha.getMinutes();
    const segundos = fecha.getSeconds();
    const horaString = hora.toString().padStart(2, '0');
    const minutosString = minutos.toString().padStart(2, '0');
    const segundosString = segundos.toString().padStart(2, '0');
    const horaCompleta = `${horaString}:${minutosString}:${segundosString}`;
    document.getElementById('hora').textContent = horaCompleta;
}
setInterval(actualizarHora, 1000);