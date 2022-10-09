# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 4

"""
Una tienda ofrece un descuento del 15% sobre el total de la compra y un  cliente desea saber cuánto deberá pagar finalmente por su compra.
"""

#Entradas
preciobs=int(input("Ingrese el valor del producto: "))
#Caja Negra
desc= preciobs*0.15
precio_final= preciobs-desc
#Salidas
print("El descuento es de:", desc)
print("El valor final del producto es:",precio_final)

