# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 6
"""
Efectuar la división de dos números enteros, utilizando el método de 
las restas sucesivas. Observe el siguiente ejemplo:
Dividir 8 entre 2
8 – 2 = 6
6 – 2 = 4    número de restas efectuadas es igual al cociente =4
4 – 2 = 2
2 – 2 = 0      %resto de la división
Imprima el restante efectuado Ejemplos de prueba 
"""
contador=0

dividendo=int(input("Ingrese el dividendo: "))
divisor=int(input("Ingrese el divisor: "))

dividendo= dividendo - divisor

while(dividendo>=0):
    contador= contador+1
    dividendo= dividendo - divisor

print("La division es igual a:", contador)