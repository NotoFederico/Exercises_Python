# Lectura y escritura de archivos

# Lectura de un archivo
with open("text.txt", "r") as file:
    aux = len(file.read())//2
    print(aux)
    file.seek(1)
    text = file.read()
    print(text)
    file.close()

# Escritura de un nuevo archivo
newText = open("new_text.txt", "w")
newText.write("Esto es un test de escritura de un nuevo archivo")
newText.close()

# Escritura de un archivo ya creado

with open("text.txt", "w") as file:
    file.write("Texto agregado desde el script exercise_55.py")
    file.close()

# Escritura de un texto sin borrar el contenido previo (modo 1)
text = open("text.txt", "a+") #se puede leer si esta presente el +
text.write("\nNuevo string de text agregado con append1")
print(text.read())
text.close()

# Escritura de un texto sin borrar el contenido previo (modo 2)
with open("text.txt", "a+") as file:
    file.write("\nNuevo string de text agregado con append2")
    print(file.read())
    file.close()
