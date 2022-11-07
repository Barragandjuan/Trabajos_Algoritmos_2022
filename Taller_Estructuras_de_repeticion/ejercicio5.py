# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 5

"""
Calcule e imprima el número de términos necesarios para que el valor de la siguiente sumatoria se aproxime los más cercanamente a 1000
sin que lo exceda:
∑((k ∗∗2 + 1)/k, donde k=1,2,3,4,...
"""
suma= 0
for k in range(1,1001,1):
    operacion=(k**2+1)/k
    if(operacion<=1000):
        suma= suma+operacion
    if(suma>1000):
        break
print("El numero de iteraciones maximas cercanas a 1000 es de:",k)
        
