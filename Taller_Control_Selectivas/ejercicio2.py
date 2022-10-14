# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 2

"""
Escriba  un  algoritmo,  que  dado  como  dato  el  sueldo  de  un  trabajador,  le  aplique un aumento del 15% 
si su salario bruto es inferior a $900.000 COP y 12% en caso contrario. Imprima el nuevo sueldo del trabajador.
"""

#Entradas
salario_neto= float(input("Ingrese el valor de su salario neto: "))
#Caja Negra
if(salario_neto<900000):
    aumento= salario_neto*0.15
    salario_final= salario_neto+aumento
else:
    aumento= salario_neto*0.12
    salario_final= salario_neto+aumento
#Salida
print("El valor de su nuevo sueldo es de",salario_final)