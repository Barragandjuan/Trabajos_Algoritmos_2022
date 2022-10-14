# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 5

"""
Una empresa que comercializa cosméticos tiene organizados a sus vendedores  en tres departamentos y ha establecido 
un programa de incentivos para incrementar su productividad. El gerente, al final del mes, pide el importe global 
de las ventas de los tres departamentos y aquellos que excedan el 33% de las ventas totales se les paga una cantidad 
extra equivalente al 20% de su salario bruto mensual. Si todos los vendedores ganan lo mismo, determinar cuánto 
recibirán los vendedores de los tres departamentos al finalizar el mes.
"""

#Entradas
salario_vendedor= float(input("Ingrese el salario del vendedor: "))
ventas_totales= int(input("Ingrese el numero de ventas totales realizadas por la empresa: "))
departamento1= int(input("Ingrese el numero de ventas realizadas por el departamento 1: "))
departamento2= int(input("Ingrese el numero de ventas realizadas por el departamento 2: "))
departamento3= int(input("Ingrese el numero de ventas realizadas por el departamento 3: "))
bonus= salario_vendedor*0.2
formula= ventas_totales*0.33


if(departamento1>formula and departamento1<ventas_totales):
    salario_f1=salario_vendedor+bonus
elif(departamento1<formula):
    salario_f1= salario_vendedor
else:
    print("Ha digitado un numero menor a 0 o un dato incorrecto")

if(departamento2>formula and departamento2<ventas_totales):
    salario_f2=salario_vendedor+bonus
elif(departamento2<formula):
    salario_f2= salario_vendedor
else:
    print("Ha digitado un numero menor a 0 o un dato incorrecto")

if(departamento3>formula and departamento3<ventas_totales):
    salario_f3=salario_vendedor+bonus
elif(departamento3<formula):
    salario_f3= salario_vendedor
else:
    print("Ha digitado un numero menor a 0 o un dato incorrecto")

suma_salarios= salario_f1+salario_f2+salario_f3
#Salidas
print("El salario del vendedor del departamento 1 es igual a:", salario_f1)
print("El salario del vendedor del departamento 2 es igual a:", salario_f2)
print("El salario del vendedor del departamento 3 es igual a:", salario_f3)
print("La suma de los salarios es es igual a:",suma_salarios)
