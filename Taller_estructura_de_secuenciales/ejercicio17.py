# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 17
"""
En un hospital rural existen tres áreas: Ginecología, Pediatría y Traumatología. El presupuesto anual del hospital se reparte
conforme a la siguiente tabla:
Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestado.
"""

#Entradas
presupuesto= float(input("Ingrese la cantidad de dinero: "))
#Caja Negra
Ginecologia= (presupuesto*0.4)
typ= (presupuesto*0.3)
#Salidas
print("El area de Ginecologia recibira:",Ginecologia)
print("El area de Traumatología recibira:",typ)
print("El area de Pediatria recibira:",typ)