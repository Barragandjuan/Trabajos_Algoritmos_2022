# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 1

"""
Un hombre desea saber cuánto dinero se generará por concepto de intereses sobre la cantidad que tiene en inversión en el banco.
El decidirá reinvertir los intereses siempre y cuando éstos excedan a $100.000 COP y en ese caso, desea saber cuánto 
dinero tendrá finalmente en su cuenta.
"""

#Entradas
capital= float(input("Ingrese la cantidad a invertir: "))
tasa= float(input("Ingrese la tasa de interes: "))
Interes= (capital*tasa)/100

#Caja Negra y Salidas
if (Interes>100000):
    print("Los intereses superan los $100.000")
    print("El total de los intereses es de:", Interes)
else:
    print("Los intereses NO superan los $100.000")
    print("El total de los intereses es de:", Interes)