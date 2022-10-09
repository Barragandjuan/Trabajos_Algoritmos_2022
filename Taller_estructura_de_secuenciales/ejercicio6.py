# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 6

"""
Un  maestro  desea  saber  qué  porcentaje  de  hombres  y  qué  porcentaje  de  mujeres hay en un grupo de estudiantes
"""

#Entradas
hombres= int(input("Digite el numero de hombres presente en el grupo de estudiantes: "))
mujeres= int(input("Digite el numero de hombres presente en el grupo de estudiantes: "))
#Caja Negra
total= hombres+mujeres
porc_hombres= (hombres*100)/total
porc_mujeres= (mujeres*100)/total
#Salidas
print("El porcentaje de hombres es de ",float(porc_hombres),"%")
print("El porcentaje de mujeres es de ",float(porc_mujeres),"%")