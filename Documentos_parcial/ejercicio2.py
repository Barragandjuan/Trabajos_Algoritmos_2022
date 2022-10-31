#Juan Barragan C.   Quiz Algoritmos y Programacion      Ejercicio 2

#Entradas
vlr1= int
vlr2= int

entrada= input()
(vlr1,vlr2)= entrada.split(" ")
p= int(vlr1)
m= int(vlr2)

#Caja Negra
operacion= (p*100/m)/100
x= round(operacion,2)
print(x)