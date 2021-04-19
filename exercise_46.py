# Crear una funcion que reciba por parametro/argumento
# una lista con números y pasar por referencia
# multiplique todos los valores por 2

def multValues(lista):
    for pos, elem in enumerate(lista):
        lista[pos]*=2

lista = [1,2,3,4,5]
print("La lista sin modificar:", lista)
multValues(lista)
print("La nueva lista es:", lista)

"""
"Si es un dato de tipo compuesto como las listas, 
si lo pasamos a una funcion, la funcion va a modificar 
el valor, si es dato es tradicional o simple, va a hacer 
una copia."
(Dicho por el profesor del curso, se ve que pasar un parametro
por referencia es una magia negra para este lenguaje
"""