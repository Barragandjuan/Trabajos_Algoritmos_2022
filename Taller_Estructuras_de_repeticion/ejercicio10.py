# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 10

"""
Dado la altura de n estudiantes de la universidad, hallar la mayor de todas las alturas
"""

n= int(input("Ingrese el numero de estudiantes: "))
alt2=0
for i in range(n):
    alt1= float(input("Ingrese la estatura del estudiante: "))
    if(alt1>alt2):
        altMax= alt1
    alt2= alt1
print("La altura maxima es:",altMax)