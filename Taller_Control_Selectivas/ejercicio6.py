# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 6

"""
Se tienen 4 dígitos en las variables A, B, C, D que forman un entero positivo 
N. Se desea  redondear  N  a  la  centena  más  próxima  y  mostrar  el  resultado. 
Considere los siguientes ejemplos: Si A es 2, B es 3, C es 6 y D es 2, entonces N 
es 2362 y el resultado redondeado es 2400. Si N es 2342, el resultado redondeado 
será 2300 y si N es 2962, el resultado redondeado será 3000
"""

A= int(input("Ingrese el valor del numero A: "))
B= int(input("Ingrese el valor del numero B: "))
C= int(input("Ingrese el valor del numero C: "))
D= int(input("Ingrese el valor del numero D: "))

if(B >=5 and C>=5):
    A= A+1
    B=0
    C=0
    D=0
elif(B >=9 and C<5):
    B= B
    C=0
    D=0
elif(B <9 and C>=5):
    B= B+1
    C=0
    D=0
else:
    C=0
    D=0

print("El valor del numero es:",A,B,C,D)