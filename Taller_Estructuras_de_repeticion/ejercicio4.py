# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 4

"""
Calcular el término doceavo y la suma de los doce primeros términos 
de la sucesión: 6, 11, 16, 21. Respuesta: a12=61, suma=402
"""
sum=0
for i in range(6,62,5):
    sum= sum+i
    if(sum==402):
        print("Posicion 12: 61")
        print("Suma: 402")

assert(sum==402 and i==61)
print("Prueba Lograda")