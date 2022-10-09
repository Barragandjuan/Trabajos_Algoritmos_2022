# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 5

"""
Un  alumno  desea  saber  cuál  será  su  calificación  final  en  la  materia  de  computación.  Dicha calificación se compone de los siguientes 
porcentajes:  55% del promedio de sus tres calificaciones parciales, 30%  de la calificación del examen final y 15% de la calificación de un trabajo final.
"""

#Entradas
prom3=int(input("Ingrese la calificacion del promedio de sus tres calificaciones parciales: "))
examenF=int(input("Ingrese la calificacion del examen final: "))
trabajoF=int(input("Ingrese la calificacion del trabajo final: "))
#Caja Negra
porc_prom3= prom3*0.55
porc_examenF= examenF*0.3
porc_trabajoF= trabajoF*0.15
nota_Final= porc_prom3+porc_examenF+porc_trabajoF
#Salidas
print("Su calificacion final sera:", nota_Final)