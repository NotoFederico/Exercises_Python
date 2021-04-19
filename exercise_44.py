# Dada una tabla que contiene los artículos y precios de un negocio y cantidad de stock,
# simular generar una factura de a lo sumo 6 artículos, en la cual el usuario solo debe
# ingresar el artículo y la cantidad (revisar que el art. tenga stock). El programa debería
# calcular los subtotales y el total general de la factura.

from tabulate import tabulate

print("\n")
matrix = [
    ["Articulos", "Precios", "Stock"],
    ["Manzanas", 10, 100],
    ["Peras", 15, 150],
    ["Bananas", 9, 60],
    ["Ciruelas", 23, 50],
    ["Kiwis", 50, 20],
    ["Ananas", 20, 70],
    ["Frutillas", 30, 225]
]

# cantidad de filas
n = len(matrix)
# cantidad de columnas
m = len(matrix[0])
# carro de compras
carrito = [["Articulo", "Precio", "Cantidad", "Subtotal"], ]

print(tabulate(matrix, headers="firstrow") + "\n")

def prodSel():
    articulo = input("Ingresar nombre del articulo: ")
    cantidad = int(input("Ingresar cantidad: "))
    flag = False
    if cantidad > 0:
        for fila in range(1, n):
            if matrix[fila][0].lower() == articulo.lower():  # Busco el articulo
                flag = True
                if matrix[fila][2] >= cantidad:
                    matrix[fila][2] -= cantidad
                    carrito.append([matrix[fila][0], matrix[fila][1],
                                    cantidad, matrix[fila][1] * cantidad])
                    print("Producto agregado satisfactoriamente al carrito")
                else:
                    print("El stock requerido es mayor al disponible")
        if not flag:
            print("El articulo ingresado no existe")
    else:
        print("La cantidad debe ser mayor a 0")


def shoppingCart():
    if len(carrito) > 1:
        print(tabulate(carrito, headers="firstrow") + "\n")
    else:
        print("\nNo hay productos en el carrito!\n")


def sell(carrito):
    total = 0
    if len(carrito) > 1:
        for subtotales in range(1, len(carrito)):
            total += carrito[subtotales][3]
        print("El importe a pagar es $", total)
        print("Transaccion finalizada")
        print("El carrito ha sido vaciado")
        carrito = [["Articulo", "Precio", "Cantidad", "Subtotal"], ]
        return carrito
    else:
        print("Imposible concretar la venta, el carrito está vacio")


while (True):
    print("""---Seleccione una opcion---
    
          [1] Seleccionar articulo
          [2] Mostrar articulos en el carrito
          [3] Realizar venta
          [4] Mostrar stock en venta
          [5] Salir
          """)
    opcion = input("Elegir opcion: ")
    if opcion.isnumeric():
        if opcion == "1":
            prodSel()
        elif opcion == "2":
            shoppingCart()
        elif opcion == "3":
            carrito = sell(carrito)
        elif opcion == "4":
            print(tabulate(matrix, headers="firstrow") + "\n")
        elif opcion == "5":
            print("Exit program")
            break
        else:
            print("Opción no listada! Elija una opcion valida")
    else:
        print("Error de ingreso! Elija una opcion valida ")

