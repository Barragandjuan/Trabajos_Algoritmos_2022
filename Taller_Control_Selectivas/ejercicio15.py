# Juan Esteban Barragan C. - Algoritmos y Programacion Grupo 2 - Ejercicio 15

"""
Tomando como base los resultados obtenidos en un laboratorio de análisis 
clínicos, un médico determina si una persona tiene anemia o no, lo cual depende 
de su nivel de hemoglobina en la sangre, de su edad y de su sexo. Si el nivel de 
hemoglobina que tiene una persona es menor que el rango que le corresponde, se 
determina su resultado como positivo y en caso contrario como negativo. La 
tabla en la que el médico se basa para obtener el resultado es la siguiente:
"""
#Entrada
validacion= input("¿El paciente a evaluar tiene entre 0 a 12 meses?, Responda con ´´SI´´ o ´´NO´´ segun corresponda: ")
#Caja Negra y Salida
if(validacion=="SI" or validacion=="Si" or validacion=="si" or validacion=="sI"):
    edadM= int(input("Digite cuantos meses tiene el paciente: "))
    hemoglobina= float(input("Ingrese el porcentaje de Hemoglobina del paciente: "))
    resultado=""
    if(edadM>=0 and edadM<=1):
        if(hemoglobina<13):
            resultado="POSITIVO"
            print("El paciente arrojo un resultado:",resultado,"por lo que presenta anemia")
        else:
            resultado="NEGATIVO"
            print("El paciente arrojo un resultado:",resultado,"por lo que NO presenta anemia")
    elif(edadM>1 and edadM<=6):
        if(hemoglobina<10):
            resultado="POSITIVO"
            print("El paciente arrojo un resultado:",resultado,"por lo que presenta anemia")
        else:
            resultado="NEGATIVO"
            print("El paciente arrojo un resultado:",resultado,"por lo que presenta anemia")
    elif(edadM>6 and edadM<=12):
        if(hemoglobina<11):
            resultado="POSITIVO"
            print("El paciente arrojo un resultado:",resultado,"por lo que presenta anemia")
        else:
            resultado="NEGATIVO"
            print("El paciente arrojo un resultado:",resultado,"por lo que presenta anemia")
    else:
        print("Ha digitado un dato erroneo, intente nuevamente")
elif(validacion=="NO" or validacion=="No" or validacion=="no" or validacion=="nO"):
    edad= int(input("Digite cuantos años tiene el paciente: "))
    hemoglobina= float(input("Ingrese el porcentaje de Hemoglobina del paciente: "))
    resultado=""
    if(edad>=1 and edad<=5):
        if(hemoglobina<11.5):
            resultado="POSITIVO"
            print("El paciente arrojo un resultado:",resultado,"por lo que presenta anemia")
        else:
            resultado="NEGATIVO"
            print("El paciente arrojo un resultado:",resultado,"por lo que NO presenta anemia")
    elif(edad>5 and edad<=10):
        if(hemoglobina<12.6):
            resultado="POSITIVO"
            print("El paciente arrojo un resultado:",resultado,"por lo que presenta anemia")
        else:
            resultado="NEGATIVO"
            print("El paciente arrojo un resultado:",resultado,"por lo que presenta anemia")
    elif(edad>10 and edad<=15):
        if(hemoglobina<13):
            resultado="POSITIVO"
            print("El paciente arrojo un resultado:",resultado,"por lo que presenta anemia")
        else:
            resultado="NEGATIVO"
            print("El paciente arrojo un resultado:",resultado,"por lo que presenta anemia")
    elif(edad>15 and edad<=110):
        genero= input("Digite ´´H´´ si el paciente es hombre o ´´M´´ si el paciente es mujer")
        if(genero =="M" or genero=="m"):
            if(hemoglobina<12):
                resultado="POSITIVO"
                print("El paciente arrojo un resultado:",resultado,"por lo que presenta anemia")
            else:
                resultado="NEGATIVO"
                print("El paciente arrojo un resultado:",resultado,"por lo que presenta anemia")
        elif(genero =="H" or genero=="h"):
            if(hemoglobina<14):
                resultado="POSITIVO"
                print("El paciente arrojo un resultado:",resultado,"por lo que presenta anemia")
            else:
                resultado="NEGATIVO"
                print("El paciente arrojo un resultado:",resultado,"por lo que presenta anemia")
        else:
            print("Ha introducido un dato erroneo, intente nuevamente")
