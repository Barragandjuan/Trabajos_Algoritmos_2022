# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 19

"""
Un  mayorista  compra  a  un  agricultor  un  lote  de  X  naranjas  a  Bs.  Y  la 
docena. Después de vender todas las naranjas a los detallistas, obtiene Bs. 
K. Calcular el porcentaje de ganancia obtenida en la inversión. Pruebe su 
programa  con  los  siguientes  valores:  X=48000,  Y=6,  K=42000  para 
obtener 75% como resultado.
"""

#Entradas
naranjast= int(input("Ingrese el lote de naranjas compradas: "))
docena= float(input("Ingrese el costo de la docena: "))
ganancia= float(input("Ingrese el total de las ganancias: "))
#Caja Negra
c_unidad= docena/12
c_lote=naranjast*c_unidad
ganancias= (100*ganancia/c_lote)-100
#Salida
print("El porcentaje de ganancia es del:",ganancias,"%")