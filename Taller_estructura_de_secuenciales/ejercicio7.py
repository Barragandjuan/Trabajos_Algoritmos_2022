# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 7

"""
Dada  una  cantidad  en  metros,  se  requiere  que  la  convierta  a  pies  y  pulgadas, considerando lo siguiente: 
1 metro = 39.27 pulgadas; 1 pie = 12 pulgadas
"""

#Entradas
metros= int(input("Digite el numero de metros a convertir: "))
#Caja Negra
pulgadas= float(metros*39.27)
pies= float(metros*39.27)/12
#Salida
print(metros,"metros equivalen a:",pulgadas,"pulgadas")
print(metros,"metros equivalen a:",pies,"pies")