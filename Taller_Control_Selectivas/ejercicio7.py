# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 7

"""
Una  compañía  de  alquiler  de  automóviles  sin  conductor,  desea  calcular  y 
mostrar lo que debe pagar cada cliente, de acuerdo a las siguientes condiciones:
"""

#Entradas
distancia=float(input("Ingrese los km recorridos:"))
#Caja Negra
mensaje=""
if(distancia<300):
    mensaje= "El valor del servicio es de: $50.000"
elif(distancia>=300 and distancia<=1000):
    distancia2= distancia-300
    cobro_e= distancia2*3000
    cobro_f=70000+cobro_e
    mensaje= "La distancia recorrida total fue de:",distancia,"kilometros con un total de:",cobro_f
else:
    distancia2=distancia-1000
    cobro_e=distancia2*9000
    cobro_f=150000+cobro_e
    mensaje= "La distancia recorrida total fue de:",distancia,"kilometros con un total de:",cobro_f
#Salida
print(mensaje)