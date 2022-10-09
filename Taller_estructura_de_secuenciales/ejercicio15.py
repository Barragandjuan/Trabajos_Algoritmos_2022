# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 15

"""
Dados como datos el precio final pagado por un producto y su precio de venta al público (PVP), se requiere que calcule y 
muestre el porcentaje de descuento que le ha sido aplicado
"""
#Entradas
precio_final= float(input("Digite el precio final pagado por el producto: "))
precio_publico= float(input("Digite el precio al publico por el producto: "))
#Caja Negra
calculo=  precio_publico - precio_final
descuento= (calculo*100)/precio_publico
#Salida
print("El articulo ha sufrido un porcentaje de descuento de", descuento,"%")