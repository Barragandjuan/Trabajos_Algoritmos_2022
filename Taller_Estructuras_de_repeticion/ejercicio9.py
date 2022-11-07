# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 9

#https://www.urionlinejudge.com.br/judge/es/problems/view/1134


Alcool=0
Gasolina=0
Diesel=0

while True:
    combustible= int(input())
    if(combustible==1):
        Alcool= Alcool+1
    elif(combustible==2):
        Gasolina= Gasolina+1
    elif(combustible==3):
        Diesel= Diesel+1
    elif(combustible==4):
        break

print("MUITO OBRIGADO")
print("Alcool:",Alcool)
print("Gasolina:",Gasolina)
print("Diesel:",Diesel)