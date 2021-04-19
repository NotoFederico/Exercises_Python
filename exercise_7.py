# Ejercicio 7: Pedir el precio de un producto y calcular su IVA (21%) y su valor original

price = int(input("Ingrese el precio del producto\n"))
print(
    f"El valor nominal del producto es ${price} y le corresponde un IVA de ${price*0.21} (21%), resultando en un total de ${price + price*0.21}")
