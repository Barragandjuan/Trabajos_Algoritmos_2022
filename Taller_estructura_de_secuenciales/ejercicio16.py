# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 16

"""
Resuelva  el  problema  que  tienen  en  una  gasolinera.  Los  surtidores  de  la misma registran lo que surten en galones, 
pero el precio de la gasolina está fijado en litros. Se requiere que calcule y muestre lo que hay que cobrarle a 
un cliente, considerando que: 
(a) cada galón tiene 3.785 litros; 
(b) el precio del litro es de 50.000 COP
"""

#Entradas
galones= float(input("Ingrese los galones a surtir: "))
#Caja Negra
Litros= (galones*3.785)
precio_Litro= (Litros*50000)
#Salida
print("El total a pagar de",Litros,"Litros es de:", precio_Litro)