# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 10

"""
Construya un programa en Python que, dados como datos la categoría y el sueldo 
bruto del trabajador, calcule el aumento correspondiente teniendo en cuenta la siguiente tabla:
"""
#Entradas
salario_neto= float(input("Ingrese el valor de su salario neto: "))
#Caja Negra
mensaje=""
if(salario_neto>0 and salario_neto<=900000):
    Categoria= 5
    aumento=salario_neto*0.6
    salario_f= salario_neto+aumento
    mensaje= "Su categoria es la #",Categoria,"y su sueldo final es de: $",salario_f
elif(salario_neto>900000 and salario_neto<=2000000):
    Categoria= 4
    aumento=salario_neto*0.4
    salario_f= salario_neto+aumento
    mensaje= "Su categoria es la #",Categoria,"y su sueldo final es de: $",salario_f
elif(salario_neto>2000000 and salario_neto<=3600000):
    Categoria= 3
    aumento=salario_neto*0.2
    salario_f= salario_neto+aumento
    mensaje= "Su categoria es la #",Categoria,"y su sueldo final es de: $",salario_f
elif(salario_neto>3600000 and salario_neto<=4300000):
    Categoria= 2
    aumento=salario_neto*0.15
    salario_f= salario_neto+aumento
    mensaje= "Su categoria es la #",Categoria,"y su sueldo final es de: $",salario_f
elif(salario_neto>4300000 and salario_neto<=5000000):
    Categoria= 1
    aumento=salario_neto*0.1
    salario_f= salario_neto+aumento
    mensaje= "Su categoria es la #",Categoria,"y su sueldo final es de: $",salario_f
else:
    mensaje="Ha excedido el limite o haintroducido un dato erroneo, intentelo nuevamente"
#Salida
print(mensaje)