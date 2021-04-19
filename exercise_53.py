# Simular un carrito de compras

class Carrito:

    def __init__(self):
        self.productos = []
        self.precios = []
        self.total = 0

    def agregarProducto(self, producto, precio):
        self.productos.append((producto))
        self.precios.append(precio)
        self.total += precio
        print(f"Se agregó el producto {producto}")

    def quitarProducto(self, producto):
        if producto in self.productos:
            posicion = self.productos.index(producto)
            self.productos.pop(posicion)
            self.total -= self.precios.pop(posicion)
            print(f"Se quitó el producto {producto}")
        else:
            print("No existe el producto!")
    def mostrarCarrito(self):
        print(f"Lista de productos: {self.productos}")

    def mostrarPrecios(self):
        print(f"Lista de precios: {self.precios}")

carrito = Carrito()
carrito.agregarProducto("Shampoo", 150)
carrito.agregarProducto("Crema", 300)
carrito.agregarProducto("Barbijo", 50)
carrito.mostrarCarrito()
carrito.mostrarPrecios()
carrito.quitarProducto("Barbijo")
carrito.mostrarCarrito()
carrito.mostrarPrecios()
