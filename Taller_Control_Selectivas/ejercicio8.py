# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 8

"""
Dados como datos los valores enteros P y Q, determine si los mismos satisfacen la 
siguiente expresión: P3 + Q4 - 2*P2 > 680. En caso afirmativo debe mostrar los 
valores  de  “ P  y  Q satisfacen la expresión”,  de  lo  contrario  muestre  un  mensaje  “P 
y Q no Satisfacen la expresión”. Utilice la concatenación para mostrar los valores
"""

#Entradas
p= float(input("Ingrese el valor de P: "))
q= float(input("Ingrese el valor de Q: "))
#Caja Negra
formula= p**3+q**4-2*p**2
if(formula>680):
    print(p,"y",q,"satisfacen la expresión, el valor final es:",formula)
else:
    print(p,"y",q,"no Satisfacen la expresión")