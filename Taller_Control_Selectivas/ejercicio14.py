# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 14

"""
Desarrolle  un  programa  en  Python  que  calcule  y  muestre  el  monto  que  debe 
pagar el suscriptor por concepto de consumo de luz eléctrica y servicio de aseo 
urbano. Dicho monto se calcula multiplicando la diferencia de la lectura anterior 
y la lectura actual por el costo de cada Kilovatio hora, según la siguiente escala
"""
#Entradas
lectura_anterior= float(input("Ingrese el consumo de la lectura anterior: "))
lectura_actual= float(input("Ingrese el consumo de la lectura actual: "))
diferencia= lectura_anterior-lectura_actual
#Caja Negra
precio=0
if(diferencia==0):
    precio=4600
elif(diferencia>0 and diferencia<=100):
    precio=diferencia*4600
elif(diferencia>100 and diferencia <=300):
    precio=diferencia*80000
elif(diferencia>300 and diferencia <=500):
    precio=diferencia*100000
elif(diferencia>500 and diferencia <=10000):
    precio=diferencia*120000
else:
    print("Haz introducido un valor incorrecto")
#Salida
print("El valor a pagar es de:",precio)