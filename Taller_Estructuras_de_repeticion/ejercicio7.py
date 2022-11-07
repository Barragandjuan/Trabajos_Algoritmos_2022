# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 7

#https://www.urionlinejudge.com.br/judge/es/problems/view/2172



while True:
    vlr1= int
    vlr2= int
    entrada= input()
    (vlr1,vlr2)= entrada.split(" ")
    entrada1= int(vlr1)
    entrada2= int(vlr2)

    op= 0
    if(entrada1>0 and entrada1<=3):
        op= entrada1 * entrada2
    elif(entrada1==0 and entrada1==0):
        break
    print(op)

    