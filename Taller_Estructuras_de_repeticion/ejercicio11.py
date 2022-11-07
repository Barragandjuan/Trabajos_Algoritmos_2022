# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 11

"""
Se  realizó una investigación en algunas discotecas y sitios de diversión de la ciudad para determinar el consumo de licor entre las 
personas encuestadas; se preguntó a cada uno de los encuestados lo siguiente:
 Consume licor (Si o No)
 Licor prefereido (1- Aguardiante, 2-Ron, 3-Cerveza, 4-Tequila, 
5-Whisky, 6-Otro)
 Edad
 Sexo
Desarrollar un programa en Python que procese dicha información y obtenga los siguientes resultados:
 Total, de personas encuestadas que consumen licor.
 Total, de mujeres menores de edad
 Total, de hombres que no consumen aguardiente y que tienen entre 20 y 25 años de edad.
 Promedio de edad de las personas que consumen cerveza.
 Porcentaje de personas que consumen whisky en relación con el total encuestado.
Para finalizar la encuesta hay que preguntar después de cada encuesta si desea seguir o no con la investigación
"""

respuesta=True
totalPerLic= 0
mujerMenor=0
totalHombreNoAguard= 0
promedadcerveza=0
consumoWhisky= 0
promedio=0
promWhisky=0
if(respuesta==True):
    totalEncuestados= int(input("Ingrese el total de personas encuestadas: "))
    for k in range(totalEncuestados):
        consumo= input("Consume licor (Responda con Si o No): ")
        if(consumo=="SI" or consumo=="si" or consumo=="sI" or consumo=="Si"):
            licor= input("Inserte su Licor preferido (1- Aguardiante, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro): ")
            edad= int(input("Inserte su edad: "))
            sexo= input("Ingrese su sexo (M= Masculino / F= Femenino): ")
            totalPerLic= totalPerLic+1
            if(licor==3):
                promedadcerveza= edad + promedadcerveza
                promedio= promedadcerveza/totalPerLic
            if(licor==5):
                consumoWhisky= consumoWhisky + 1
                promWhisky= consumoWhisky/totalEncuestados
            if((sexo=="m" or sexo=="M") and (licor!=1) and (edad>=20 or edad<26)):
                totalHombreNoAguard= totalHombreNoAguard+1
        else:
            edad= int(input("Inserte su edad: "))
            sexo= input("Ingrese su sexo (M= Masculino / F= Femenino): ")
        if(edad<18 and (sexo=="f" or sexo=="F")):
            mujerMenor= mujerMenor+1
        if((sexo=="m" or sexo=="M") and (consumo=="no" or consumo=="NO" or consumo=="nO" or consumo=="No") and (edad>=20 or edad<26)):
            totalHombreNoAguard= totalHombreNoAguard+1
    print("El total de personas que consumen licor es de:",totalPerLic)
    print("El total de mujeres menores de edad es de:",mujerMenor)
    print("El total de hombres que no consumen Aguardiente y su edad es de 20 a 25 años es de es de:",totalHombreNoAguard)
    print("El promedio de edad de las personas que toman cerveza es de:",promedio)
    print("El promedio de personas que consumen Whisky es de:",promWhisky)
respuesta= input("Desea seguir con la investigacion (SI/NO): ")
if(respuesta=="SI" or respuesta=="si" or respuesta=="Si"):
    respuesta=True
else:
    respuesta=False