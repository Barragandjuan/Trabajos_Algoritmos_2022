import random
jugador= True
dealer= True
#Informacion Baraja y Cartas Jugador/Dealer
baraja= [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
            "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A",]
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
    print(f"El dealer tiene: {revelarCartasDealer()}")
    print(f"El jugador tiene: {cartas_Jugador} que es un total de: {total(cartas_Jugador)}")
