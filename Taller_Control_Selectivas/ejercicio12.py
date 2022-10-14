# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 12

"""
Dada una cantidad entera de COP, desarrolle un algoritmo que permita 
desglosar dicha cantidad en los billetes y monedas de curso legal en el País. 
Recuerde que estos son: 
Billetes
100.000 COP,
50.000 COP, 
20.000 COP, 
10.000 COP, 
5.000 COP, 
2.000 COP, 
1.000 COP
Monedas
500 COP, 
200 COP, 
100 COP,
50 COP
Nota: si la cantidad tiene unidades no las tenga en cuenta 
ejemplo:
Entrada:2251
Salida: 2.000,200,50
"""

#Entrada
cop= float(input("Ingrese la cantidad en COP: "))
#Caja Negra
if(cop>=100000):
    division1= cop//100000
    resultado= division1*100000