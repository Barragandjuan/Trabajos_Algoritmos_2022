# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 3

"""
Desarrolle un algoritmo o programa que permita calcular y mostrar la suma de todos los números pares comprendidos entre 97 y 1003. 
Respuesta: 249150 
"""

sum=0 
for i in range(97,1004,1):
    if(i%2==0):
        sum= sum+i

assert(sum==249150)
print("Prueba superada!")