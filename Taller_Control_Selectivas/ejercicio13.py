# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 13
from datetime import datetime

#Entradas
hoy= datetime.now()
dia_actual=hoy.day
mes_actual=hoy.month
año_actual=hoy.year

fecha_nacimiento= input("Poner en formato dd/mm/yy:")
(dia,mes,año)= fecha_nacimiento.split("/")
dia_nacimiento= int(dia)
mes_nacimiento= int(mes)
año_nacimiento= int(año)

#Caja Negra
#Calculo edad
edad=0
if(mes_actual>mes_nacimiento):
    edad= año_actual-año_nacimiento
elif(mes_actual<mes_nacimiento):
    edad= (año_actual-año_nacimiento)-1
elif(mes_actual==mes_nacimiento):
    if(dia_actual<dia_nacimiento):
        edad=(año_actual-año_nacimiento)
    elif(dia_actual>dia_nacimiento):
        edad=(año_actual-año_nacimiento)
    elif(dia_actual==dia_nacimiento):
        edad=(año_actual-año_nacimiento)

signo=""
if(dia_nacimiento>=21 or dia_nacimiento<32 and mes_nacimiento==1)or(dia_nacimiento>=1 or dia_nacimiento<=19 and mes_nacimiento==2):
    signo="Acuario"
    print("Su edad es:",edad)
    print("Su signo zodiacal es:",signo)
elif(dia_nacimiento>=20 or dia_nacimiento<30 and mes_nacimiento==2)or(dia_nacimiento>=1 or dia_nacimiento<=19 and mes_nacimiento==3):
    signo="Piscis"
    print("Su edad es:",edad)
    print("Su signo zodiacal es:",signo)
elif(dia_nacimiento>=20 or dia_nacimiento<32 and mes_nacimiento==3)or(dia_nacimiento>=1 or dia_nacimiento<=20 and mes_nacimiento==4):
    signo="Aries"
    print("Su edad es:",edad)
    print("Su signo zodiacal es:",signo)
elif(dia_nacimiento>=21 or dia_nacimiento<31 and mes_nacimiento==4)or(dia_nacimiento>=1 or dia_nacimiento<=21 and mes_nacimiento==5):
    signo="Tauro"
    print("Su edad es:",edad)
    print("Su signo zodiacal es:",signo)
elif(dia_nacimiento>=22 or dia_nacimiento<32 and mes_nacimiento==5)or(dia_nacimiento>=1 or dia_nacimiento<=21 and mes_nacimiento==6):
    signo="Geminis"
    print("Su edad es:",edad)
    print("Su signo zodiacal es:",signo)
elif(dia_nacimiento>=22 or dia_nacimiento<31 and mes_nacimiento==6)or(dia_nacimiento>=1 or dia_nacimiento<=22 and mes_nacimiento==7):
    signo="Cancer"
    print("Su edad es:",edad)
    print("Su signo zodiacal es:",signo)
elif(dia_nacimiento>=23 or dia_nacimiento<32 and mes_nacimiento==7)or(dia_nacimiento>=1 or dia_nacimiento<=23 and mes_nacimiento==8):
    signo="Leo"
    print("Su edad es:",edad)
    print("Su signo zodiacal es:",signo)
elif(dia_nacimiento>=24 or dia_nacimiento<32 and mes_nacimiento==8)or(dia_nacimiento>=1 or dia_nacimiento<=22 and mes_nacimiento==9):
    signo="Virgo"
    print("Su edad es:",edad)
    print("Su signo zodiacal es:",signo)
elif(dia_nacimiento>=23 or dia_nacimiento<31 and mes_nacimiento==9)or(dia_nacimiento>=1 or dia_nacimiento<=22 and mes_nacimiento==10):
    signo="Libra"
    print("Su edad es:",edad)
    print("Su signo zodiacal es:",signo)
elif(dia_nacimiento>=23 or dia_nacimiento<32 and mes_nacimiento==10)or(dia_nacimiento>=1 or dia_nacimiento<=21 and mes_nacimiento==11):
    signo="Escorpion"
    print("Su edad es:",edad)
    print("Su signo zodiacal es:",signo)
elif(dia_nacimiento>=22 or dia_nacimiento<31 and mes_nacimiento==11)or(dia_nacimiento>=1 or dia_nacimiento<=21 and mes_nacimiento==12):
    signo="Sagitario"
    print("Su edad es:",edad)
    print("Su signo zodiacal es:",signo)
elif(dia_nacimiento>=22 or dia_nacimiento<32 and mes_nacimiento==12)or(dia_nacimiento>=1 or dia_nacimiento<=20 and mes_nacimiento==1):
    signo="Capricornio"
    print("Su edad es:",edad)
    print("Su signo zodiacal es:",signo)