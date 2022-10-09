# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 9

"""
Calcular el salario neto de un trabajador en función del número de horas trabajadas, el precio de la hora y considerando un descuento fijo al 
sueldo base por concepto de impuestos del 20%
"""

#Entradas
precio_h=float(input("Digite el precio de la hora de trabajo: "))
horas_t=int(input("Digite el numero de horas trabajadas: "))
#Caja Negra
salario_n= precio_h*horas_t
impuesto= salario_n*0.2
salario_f= salario_n-impuesto
#Salidas
print("El salario final es de:",salario_f)