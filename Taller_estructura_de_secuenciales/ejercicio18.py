# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 18

"""
Calcule qué tanto por ciento anual cobraron por un préstamo de Bolívares X, 
si se pagaron Bolívares Y de intereses en 4 años.  La fórmula del interés es
"""

#Entradas
C_prestamo= float(input("Ingrese la cantidad prestada: "))
tiempo= int(input("Ingrese la duracion del prestamo: "))
tasa= float(input("Ingrese la tasa de prestamo: "))
#Caja Negra
Interes= (C_prestamo*tiempo*tasa)/100
Interes_t= Interes/tiempo
porc_interesanula= (Interes_t*100)/Interes
#Salidas
print("El total de Intereses fue de", Interes)
print("La tasa anual fue de", Interes_t, "Con un porcentaje de", porc_interesanula)