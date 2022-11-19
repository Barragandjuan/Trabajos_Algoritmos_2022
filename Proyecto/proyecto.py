import random

jugador= True
dealer= True

#Informacion Baraja y Cartas Jugador/Dealer
baraja= [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A",]

cartas_Jugador=[]
cartas_Dealer=[]

#Reparto de cartas
def reparto(turno):
    carta= random.choice(baraja)
    turno.append(carta)
    baraja.remove(carta)

#Validacion de Total
def total(turno):
    total=0
    cara=[ "J", "Q", "K"]
    for carta in turno:
        if carta in range(1,11):
            total= total+carta
        elif carta in cara:
            total= total + 10
        else:
            if total > 11:
                total= total+1
            else:
                total= total + 11
    return total

#Ganador
def revelarCartasDealer():
    if len(cartas_Dealer) == 2:
        return cartas_Dealer[0]
    elif len(cartas_Dealer) > 2:
        return cartas_Dealer[0],cartas_Dealer[1]

for _ in range(2):
    reparto(cartas_Dealer)
    reparto(cartas_Jugador)

while jugador or dealer:
    print(f"\nEl dealer tiene: {revelarCartasDealer()}")
    print(f"El jugador tiene: {cartas_Jugador} que es un total de: {total(cartas_Jugador)}")
    if jugador:
        pCarta= int(input("Digite: \n1. Para quedarte  \n2. Para pedir carta \n"))
    if total(cartas_Dealer) > 16:
        dealer = False 
    else:
        reparto(cartas_Dealer)
    if pCarta == 1:
        jugador = False
    else:
        reparto(cartas_Jugador)
    if total(cartas_Jugador) >=21:
        break
    elif total(cartas_Dealer) >=21:
        break

if total(cartas_Jugador) == 21:
    print(f"\nTienes {cartas_Jugador} para un total de {total(cartas_Jugador)} y el dealer tiene {cartas_Dealer} para un total de {total(cartas_Dealer)}")
    print("Felicidades ha obtenido un blackjack, Jugador gana\n")
elif total(cartas_Dealer) == 21:
    print(f"\nTienes {cartas_Jugador} para un total de {total(cartas_Jugador)} y el dealer tiene {cartas_Dealer} para un total de {total(cartas_Dealer)}")
    print("El dealer ha obtenido un blackjack, Dealer gana\n")
elif total(cartas_Jugador) > 21:
    print(f"\nTienes {cartas_Jugador} para un total de {total(cartas_Jugador)} y el dealer tiene {cartas_Dealer} para un total de {total(cartas_Dealer)}")
    print("Haz superado el limite de cartas, Dealer gana\n")
elif total(cartas_Dealer) > 21:
    print(f"\nTienes {cartas_Jugador} para un total de {total(cartas_Jugador)} y el dealer tiene {cartas_Dealer} para un total de {total(cartas_Dealer)}")
    print("El Dealer ha superado el limite de cartas, Jugador gana\n")
elif 21 - total(cartas_Dealer) < 21 - total(cartas_Jugador):
    print(f"\nTienes {cartas_Jugador} para un total de {total(cartas_Jugador)} y el dealer tiene {cartas_Dealer} para un total de {total(cartas_Dealer)}")
    print("Dealer gana\n")
elif 21 - total(cartas_Dealer) > 21 - total(cartas_Jugador):
    print(f"\nTienes {cartas_Jugador} para un total de {total(cartas_Jugador)} y el dealer tiene {cartas_Dealer} para un total de {total(cartas_Dealer)}")
    print("Jugador gana\n")