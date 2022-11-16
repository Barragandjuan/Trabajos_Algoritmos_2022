diccionario={}

datos= int(input("Ingrese el numero de datos a ingresar: "))
k=1
for i in range(datos):
    nombre= input("Ingrese el nombre del estudiante: ")
    nota= float(input("Ingrese la nota del estudiante: "))

    diccionario.update({"nombre":nombre}, {"nota":nota})
