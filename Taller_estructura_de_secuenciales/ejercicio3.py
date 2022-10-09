# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 3

"""
Un vendedor recibe un sueldo base, más un 10% extra por comisiones de  sus ventas. El vendedor desea saber cuánto dinero obtendrá por concepto  
de  comisiones  por  las  tres  ventas  que  realizó  en  el  mes  y  el  total  que  recibirá tomando en cuenta su sueldo base y sus comisiones.
"""

#Entradas
sueldo_bs=int(input("Ingrese el sueldo base mensual: "))
ventas=int(input("Ingrese las comisiones realizadas en el mes: "))
#Caja Negra
comisiones= (sueldo_bs*0.1)*ventas
sueldo_final= sueldo_bs + comisiones
#Salidas
print("El dinero recibido por comision de ventas es de:",comisiones)
print("El sueldo final es",sueldo_final)
