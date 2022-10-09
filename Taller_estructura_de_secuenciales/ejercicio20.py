# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 20

"""
Un comerciante de computadores ofrece P precio por compra al contado 
ó 12 cuotas de T COP cada una. Desarrolle un programa para calcular y 
mostrar  cuál  es  el  porcentaje  que  se  cobra  por  el  recargo  en  el  pago  del 
computador por cuota
"""

#Entradas
p_computadorco= float(input("Ingrese el precio del computador a contado: "))
p_computadorcu= float(input("Ingrese el precio del computador a cuotas: "))      
#Caja Negra
diferencia= p_computadorcu - p_computadorco
porc= (diferencia*100)/p_computadorcu
d_porc= porc/12
#Salidas
print("El porcentaje de recargo en las 12 cuotas es de", porc,"%")    
print("Cada mes el porcentaje de la cuota es de", d_porc,"%")                                                                            