def horaDeLlegada(numeros):
    numeros = numeros.split()
    horaInicial = int(numeros[0])
    horasDeViaje = int(numeros[1])
    diferenciaHoraria = int(numeros[2])

    return (horaInicial + horasDeViaje + diferenciaHoraria) % 24

print(horaDeLlegada('0 3 -4'))