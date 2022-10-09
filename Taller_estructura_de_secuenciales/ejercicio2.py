# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 2

"""
Suponga que un individuo decide invertir su capital en un banco y desea saber  cuánto  dinero  ganará  después  de  un  mes  si  el  banco  paga  a  razón  de  2%  mensual.
"""

#Entradas
inversion=int(input("Ingrese el capital a invertir: "))
#Caja Negra
razon2= inversion*0.02
pago_final= inversion+razon2
#Salidas
print("El pago final que recibira es de:",pago_final)