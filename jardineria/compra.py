class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito = carrito

    #def agregar(self, producto):
    #    if producto.id not in self.carrito.keys():
    #        self.carrito[producto.id] = {
    #            "producto_id": producto.id,
    #            "nombre": producto.nombre,
    #            "precio": producto.precio,
    #            "cantidad": 1,
    #            "total": producto.precio,
    #        }
    #    else:
    #        for key, value in self.carrito.items():
    #            if key == producto.id:
    #                value["cantidad"] = value["cantidad"] + 1
    #                value["precio"] = producto.precio
    #                value["total"] = value["total"] + producto.precio
    #                break
    #    self.guardar_carrito()

    def agregar(self, producto):
        if producto.id in self.carrito:
            self.carrito[producto.id]['cantidad'] += 1
            self.carrito[producto.id]['total'] += producto.precio
        else:
            self.carrito[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": 1,
                "total": producto.precio,
            }
        self.guardar_carrito()
    
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = producto.id
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar(self, producto):
        for key, value in self.carrito.items():
            if key == producto.id:
                value["cantidad"] = value["cantidad"] - 1
                value["total"] = int(value["total"]) - producto.precio
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True