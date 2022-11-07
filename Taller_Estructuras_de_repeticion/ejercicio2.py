# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 2

"""
Escriba un programa que imprima todos los enteros positivos impares menores que 100 omitiéndose aquellos que sean divisibles por 7
"""

for i in range(1,100,1):
    if(i%2==1):
        if(i%7!=0):
            print(i)