# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 10

"""
El cambio de divisas en la bolsa de Madrid el 25/08/1987 fue el siguiente 
100 chelines austríacos = 956.871 pesetas
1 dólar EEUU = 122.499 pesetas
100 dracmas griegos  = 88.607 pesetas
100 francos belgas = 323.728 pesetas
1 franco francés = 20.110 pesetas
1  libra  esterlina = 178.938  pesetas
100 liras italianas = 9.289 pesetas
-Lea una cantidad en chelines austriacos e imprima el equivalente en pesetas. 
-Lea una cantidad en dracmas griegos e imprima su equivalente en francos franceses. 
-Finalmente, lea una cantidad en pesetas e imprima su equivalente en dólares y liras italianas.
"""

#Entradas
chelinesa= float(input("Ingrese la cantidad de chelines austriacos a convertir: "))
dracmas= float(input("Ingrese la cantidad de dracmas a convertir: "))
pesetas= float(input("Ingrese la cantidad de pesetas a convertir: "))
#Caja Negra
c_chelines= (chelinesa*956.871)/100
c_dracmas= (dracmas*88.607)/(100*20.110)
c_peseta1= (pesetas/122.499)
c_peseta2= (pesetas*100)/9.289
#Salidas
print(int(chelinesa),"Chelines austriacos equivalen a",c_chelines,"Pesetas")
print(int(dracmas),"Dracmas Griegos equivalen a",c_dracmas,"Francos Franceses")
print(int(pesetas),"Pesetas equivalen a",c_peseta1,"Dolares")
print(int(pesetas),"Pesetas equivalen a",c_peseta2,"Liras Italianas")