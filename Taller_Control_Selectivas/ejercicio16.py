# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 16

"""
Confeccionar  un  algoritmo  que  permita  resolver  una  ecuación  de  segundo  grado, de la forma: AX2+BX+C = 0, 
sabiendo que el discriminante (D) se calcula con la fórmula: D= Bˆ2­4*A*C. 
El valor obtenido se evalúa y se aplica la fórmula correspondiente, según muestra la siguiente tabla
"""
import math

#Entradas
valorA= float(input("Ingrese el valor de A: "))
valorB= float(input("Ingrese el valor de B: "))
valorC= float(input("Ingrese el valor de C: "))
#Caja Negra
ecuacionD=valorB**2-4*valorA*valorC
x1= 0
x2= 0
if(ecuacionD==0):
    x1=-valorB/(2*valorA)
    print("El valor de X1 es igual a: ",x1)
elif(ecuacionD>0):
    x1= (-valorB+math.sqrt(ecuacionD))/(2*valorA)
    x2= (-valorB-math.sqrt(ecuacionD))/(2*valorA)
    print("El valor de X1 es igual a: ",x1)
    print("El valor de X2 es igual a: ",x2)
elif(ecuacionD<0):
    print("No tiene solucion en los reales")
