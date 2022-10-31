#Juan Barragan C.   Quiz Algoritmos y Programacion      Ejercicio 1

#Entradas
vlr1= int
vlr2= int
vlr3= int

entrada= input()
(vlr1,vlr2,vlr3)= entrada.split(" ")
entrada1= int(vlr1)
entrada2= int(vlr2)
entrada3= int(vlr3)
#Caja Negra
sumahrs= entrada1+entrada2
hrfinal=0
if(entrada1!=0):
    if(sumahrs>24):
        hrfinal= entrada1+entrada2+entrada3
        if(hrfinal!=24):
            hrfinal= abs(hrfinal-sumahrs)
            print(hrfinal)
        elif(hrfinal==24):
            hrfinal==24
            print(hrfinal)
    elif(sumahrs<24):
        hrfinal= entrada1+entrada2+entrada3
        if(hrfinal==24):
            hrfinal=0
            print(hrfinal)
        else:
            print(hrfinal)
else:
        sumahrs=24
        hrfinal= sumahrs+entrada2+entrada3
        print(hrfinal)


