# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 11

"""
Desarrolle un algoritmo, que dado como dato una temperatura en grados Fahrenheit, determine el deporte que es apropiado 
practicar a esa temperatura, teniendo en cuenta la siguiente tabla:
"""

#Entrada
temperatura= float(input("Ingrese la temperatura actual: "))
#Caja Negra
deporte=""
if(temperatura>0 and temperatura <=10):
    deporte= "Marcha"
elif(temperatura>10 and temperatura <=32):
    deporte= "Esqui"
elif(temperatura>32 and temperatura <=70):
    deporte= "Golf"
elif(temperatura>70 and temperatura <=85):
    deporte= "Tenis"
elif(temperatura>85 and temperatura <=100):
    deporte= "Natacion"
#Salida
print("El deporte a practicar es:",deporte)