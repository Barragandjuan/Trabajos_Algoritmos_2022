# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 12

"""
Calcule y muestre, a un alumno, cuál será su promedio general en las tres  materias  más  difíciles  que  cursa  y  cuál  será  el  promedio  
que obtendrá en cada una  de  ellas.  Estas  materias  se  evalúan  como  se  muestra  a continuación:
"""

#Entradas
    #Matematicas
print("A continuacion registre las calificaciones de la materia de Matematicas")
tarea1Mate= float(input("Inserte el valor de la calificacion de la tarea 1 de Matematicas: "))
tarea2Mate= float(input("Inserte el valor de la calificacion de la tarea 2 de Matematicas: "))
tarea3Mate= float(input("Inserte el valor de la calificacion de la tarea 3 de Matematicas: "))
examenMate= float(input("Ingrese el valor de la calificacion del examen de Matematicas: "))
    #Fisica
print("A continuacion registre las calificaciones de la materia de Fisica")
tarea1Fisi= float(input("Inserte el valor de la calificacion de la tarea 1 de Fisica: "))
tarea2Fisi= float(input("Inserte el valor de la calificacion de la tarea 2 de Fisica: "))
examenFisi= float(input("Ingrese el valor de la calificacion del examen de Fisica: "))
    #Quimica
print("A continuacion registre las calificaciones de la materia de Quimica")
tarea1Quimi= float(input("Inserte el valor de la calificacion de la tarea 1 de Quimica "))
tarea2Quimi= float(input("Inserte el valor de la calificacion de la tarea 2 de Quimica: "))
tarea3Quimi= float(input("Inserte el valor de la calificacion de la tarea 3 de Quimica: "))
examenQuimi= float(input("Ingrese el valor de la calificacion del examen de Quimica: "))

#Caja Negra
porc_tareasMate= ((tarea1Mate+tarea2Mate+tarea3Mate)/3)*0.1
porc_ExamenMate= examenMate*0.9
porc_totalMate= porc_ExamenMate + porc_tareasMate

porc_tareasFisi= ((tarea1Fisi+tarea2Fisi)/2)*0.2
porc_ExamenFisi= examenFisi*0.8
porc_totalFisi= porc_ExamenFisi + porc_tareasFisi

porc_tareasQuimi= ((tarea1Quimi+tarea2Quimi+tarea3Quimi)/3)*0.15
porc_ExamenQuimi= examenQuimi*0.75
porc_totalQuimi= porc_ExamenQuimi + porc_tareasQuimi

prom3notas= (porc_totalQuimi+porc_totalMate+porc_totalFisi)/3

#Salidas
print("El valor de la nota final de Matematicas es de:",porc_totalMate)
print("El valor de la nota final de Fisica es de:",porc_totalFisi)
print("El valor de la nota final de Quimica es de:",porc_totalQuimi)
print("El promedio general en las 3 materias es de:", prom3notas)
