# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 14

"""
Calcular  y  mostrar  el  monto  total  a  pagar  en  un  mes  de  luz  eléctrica, 
teniendo como  dato  la  lectura  anterior,  la  lectura  actual  y  el  costo  por 
kilovatio
"""

#Entradas
lectura_anterior= float(input("Ingrese el valor de la lectura anterior de la luz electrica: "))
lectura_actual= float(input("Ingrese el valor de la lectura actual de la luz electrica: "))
costo_kv= float(input("Ingrese el costo por kilovatio: "))
#Caja Negra
lectura_final= lectura_actual - lectura_anterior
consumo= costo_kv*lectura_final
#Salida
print("El costo final a pagar por",lectura_final,"kilovatios es de:",consumo)