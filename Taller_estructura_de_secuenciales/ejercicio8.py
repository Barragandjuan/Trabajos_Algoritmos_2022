import math
# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 8


#Entradas
lado1=float(input("Ingrese el valor del lado uno: "))
lado2=float(input("Ingrese el valor del lado dos: "))
lado3=float(input("Ingrese el valor del lado tres: "))
#Caja Negra
s= (lado1+lado2+lado3)/2
area= math.sqrt(s*(s-lado1)*(s-lado2)*(s-lado3))
#Salidas
print("El valor del semiperimetro es: ",s)
print("El valor del area es:", area)