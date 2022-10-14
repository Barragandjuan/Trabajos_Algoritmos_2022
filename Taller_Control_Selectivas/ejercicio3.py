# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 3

"""
Dados los datos A, B, C y D que representan números enteros; escriba un 
algoritmo que calcule el resultado de las siguientes expresiones:
"""

#Entradas
a= float(input("Ingrese los datos del valor A:"))
b= float(input("Ingrese los datos del valor B:"))
c= float(input("Ingrese los datos del valor C:"))
d= float(input("Ingrese los datos del valor D:"))
#Caja Negra & Salida
if(d==0):
    operacion=(a-c)**2
    print("El valor de la operacion es igual a=",operacion)
elif(d>0):
    operacion=(a-b)**3/d
    print("El valor de la operacion es igual a=",operacion)
else:
    print("No hay operacion para el valor de D menor a 0")