lista_nombres=[]
lista_notas=[]
contador=0
contadorperdidas=0
contadorganar=0
i=1

for i in range(1,11):
    nombre= input("Ingrese el nombre del estudiante: ")
    nota= float(input("Ingrese la nota: "))
    lista_nombres.append(nombre)
    lista_notas.append(nota)
    contador+= nota
    if nota<60:
        contadorperdidas=+1
    else:
        contadorganar+=1

diccionario={
    "1":{
        "nombrestudiante": f"{lista_nombres[0]}",
        "notaestudiante": f"{lista_notas[0]}"
    },
    "2":{
        "nombrestudiante": f"{lista_nombres[1]}",
        "notaestudiante": f"{lista_notas[1]}"
    },
    "3":{
        "nombrestudiante": f"{lista_nombres[2]}",
        "notaestudiante": f"{lista_notas[2]}"
    },
    "4":{
        "nombrestudiante": f"{lista_nombres[3]}",
        "notaestudiante": f"{lista_notas[3]}"
    },
    "5":{
        "nombrestudiante": f"{lista_nombres[4]}",
        "notaestudiante": f"{lista_notas[4]}"
    },
    "6":{
        "nombrestudiante": f"{lista_nombres[5]}",
        "notaestudiante": f"{lista_notas[5]}"
    },
    "7":{
        "nombrestudiante": f"{lista_nombres[6]}",
        "notaestudiante": f"{lista_notas[6]}"
    },
    "8":{
        "nombrestudiante": f"{lista_nombres[7]}",
        "notaestudiante": f"{lista_notas[7]}"
    },
    "9":{
        "nombrestudiante": f"{lista_nombres[8]}",
        "notaestudiante": f"{lista_notas[8]}"
    },
    "10":{
        "nombrestudiante": f"{lista_nombres[9]}",
        "notaestudiante": f"{lista_notas[9]}"
    }
}

prom= contador/10
print("Los estudiantes que perdieron fueron:", contadorperdidas)
print("Los estudiantes que superaron la nota fueron:", contadorganar)
print("el promedio de la nota es de:", prom)