# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 11

"""
Se  conoce  de  un  trabajador  su  nombre,  el  número  de  horas  normales 
trabajadas, el  pago  de  una  hora  normal  y  el  número  de  horas  extras 
trabajadas.  Además,  que, cada hora extra se paga 25% más del valor de 
una hora normal. Si se deducen al trabajador sobre el sueldo base 5% del 
paro forzoso, 2% de política habitacional y 7% para caja de ahorro. Si se 
le asignan 250.000 COP por actualización académica, 173.000 COP por 
cada hijo y una prima por hogar de 180000 COP. Calcule y muestre las 
asignaciones, las deducciones y el sueldo neto del trabajador para el mes 
de diciembre.
"""

#Entradas
nombre= input("Introduzca su nombre y apellido: ")
horast= int(input("Introduzca el numero de horas normales trabajadas: "))
precioh= float(input("Introduzca el valor de cada hora trabajada: "))
horase= int(input("Introduzca el numero de horas extras trabajadas: "))
nhijos= int(input("Introduzca el numero de hijos que tiene: "))
#Caja Negra
sueldo_1= horast*precioh
pagohe= (precioh*0.25)+precioh
horase_p= horase*pagohe
deducciones= ((sueldo_1*0.05)+(sueldo_1*0.02)+(sueldo_1*0.07))
asignaciones= 250000+(nhijos*173000)+180000
salariof= (sueldo_1+horase_p+asignaciones)-deducciones
#Salidas
print("El total de las asignaciones es de:",asignaciones)
print("El total de las deducciones es de:",deducciones)
print("El sueldo neto para el trabajador",nombre,"en el mes de Diciembre es de",salariof)