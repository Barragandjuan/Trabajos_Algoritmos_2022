# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 13

"""
Determine cuánto dinero hay en un banco que contiene 
N1 billetes de 50000, 
N2 billetes de 20000, 
N3 billetes de 10000,
N4 billetes de 5000, 
N5 billetes de 2000, 
N6 billetes 1000, 
N7 billetes de 500 y
N8 billetes de 100
"""

#Entradas
billetes_50k= int(input("Digite la cantidad de billetes de $50.000: "))
billetes_20k= int(input("Digite la cantidad de billetes de $20.000: "))
billetes_10k= int(input("Digite la cantidad de billetes de $10.000: "))
billetes_5k= int(input("Digite la cantidad de billetes de $5.000: "))
billetes_2k= int(input("Digite la cantidad de billetes de $2.000: "))
billetes_1k= int(input("Digite la cantidad de billetes de $1.000: "))
billetes_500= int(input("Digite la cantidad de billetes de $500: "))
billetes_100= int(input("Digite la cantidad de billetes de $100: "))
#Caja Negra
total_Billetes50k= (50000*billetes_50k)
total_Billetes20k= (20000*billetes_20k)
total_Billetes10k= (10000*billetes_10k)
total_Billetes5k= (5000*billetes_5k)
total_Billetes2k= (2000*billetes_2k)
total_Billetes1k= (1000*billetes_1k)
total_Billetes500= (500*billetes_500)
total_Billetes100= (100*billetes_100)
total_Billetes= total_Billetes50k+total_Billetes20k+total_Billetes10k+total_Billetes5k+total_Billetes2k+total_Billetes1k+total_Billetes500+total_Billetes100
#Salida
print("El total del dinero es de:",total_Billetes)