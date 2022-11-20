import pygame
from enum import Enum, IntEnum
import random

class Carta():
    def __init__(self,V,N,S,P):
        self.valor = V      # Valor de la Carta
        self.nombre = N       # Nombre de la Carta
        self.palo = S       # Palo de la Carta
        self.imagen = P      # Imagen de la Carta


def crearBaraja():
    baraja = []
    i = 0
    for j in range(len(VALORES_CARTAS)):
        for k in PALOS_CARTAS:
            # Create Carta object and append to baraja
            baraja.append(Carta(VALORES_CARTAS[j], NOMBRES_CARTAS[j], k, IMAGENES_CARTAS[i]))
            i += 1

    return baraja


def index_carta(V,S):
    if S == 'S':
        T = 1
    elif S == 'C':
        T = 2
    elif S == 'D':
        T = 3
    elif S == 'H':
        T = 4
    else:
        print("Error en funcion index_carta")

    return (V-1)*4 + (T-1)


def mostrar_carta():

    # Muestra todas las cartas de la mano del jugador    
    if (len( mano_jugador) != 0):
        for i in range(len( mano_jugador)):
            win.blit( mano_jugador[i].imagen, (carta_x_pos[i],carta_y_pos[i]))

    if(revelar or espectar):
        # Muestra todas las cartas de la mano del AI boca arriba      
        if (len( mano_AI) != 0):
            for i in range(len( mano_AI)):
                win.blit( mano_AI[i].imagen, (AI_carta_x_pos[i],AI_carta_y_pos[i]))
    else:
        # Muestra todas las cartas de la mano del AI boca abajo  
        if (len( mano_AI_escondida) != 0):
            for i in range(len( mano_AI_escondida)):
                win.blit( mano_AI_escondida[i].imagen, (escondida_carta_x_pos[i], escondida_carta_y_pos[i]))

    pygame.display.update() 


# Seleccionar carta al azar de la baraja
def carta_aleatoria():
    global baraja_entera
    r = random.randint(0,len(baraja_entera)-1)

    # Remueve y devuelve una carta de la baraja
    return baraja_entera.pop(r)


# Reparte carta al jugador
def repartir_jugador():
    global carta_x_pos
    global carta_y_pos

    mano_jugador.append(carta_aleatoria())

    if (len(carta_x_pos) == 0):
        carta_x_pos.append(X_INICIAL)
    else:
        carta_x_pos.append(carta_x_pos[-1] + DESPLAZO_INICIAL)

    carta_y_pos.append(Y_INICIAL)


# Reparte carta al AI
def repartir_AI():
    global AI_carta_x_pos
    global AI_carta_y_pos
    global escondida_carta_x_pos
    global escondida_carta_y_pos

    # Si mano del AI es menor que 18, reparte
    if obtener_valor_mano(mano_AI) < 18:
        mano_AI.append(carta_aleatoria())
        mano_AI_escondida.append(carta_escondida)

        # Añadir carta a posicion inicial si la mano del AI esta vacia
        if (len(AI_carta_x_pos) == 0):
            AI_carta_x_pos.append(X_INICIAL)
            escondida_carta_x_pos.append(X_INICIAL)
        else:
            # Añadir carta si la mano del AI no esta vacia
            AI_carta_x_pos.append(AI_carta_x_pos[-1] + DESPLAZO_INICIAL)
            escondida_carta_x_pos.append(escondida_carta_x_pos[-1] + DESPLAZO_INICIAL)

        # Todas las cartas tienen el mismo valor en Y
        AI_carta_y_pos.append(AI_Y_INICIAL)
        escondida_carta_y_pos.append(AI_Y_INICIAL)

        return True
    else:
        return False


# Obtener valor de la mano de jugador o del AI     
def obtener_valor_mano(mano):
    # Si la mano esta vacia, valor es igual a 0
    if len(mano) == 0:
        return 0
    else:
        Aces = []
        suma = 0

        for i in mano:
            # Cuantos Aces hay en la mano?
            if i.nombre == 1:
                Aces.append(i)

            # Sum of Carta values
            suma += i.valor
        
        # Reduce valor de los Aces para evitar perder
        if suma > 21 and (len(Aces) != 0):
            suma -= 10
        return suma


# Muestra texto en GUI
def mostrar_texto():
    ai_texto_mano = GUI_font.render("MANO DEL AI:",True,blanco)
    jugador_texto_mano = GUI_font.render("MANO DEL JUGADOR:",True,blanco)
    texto_valor_mano = GUI_font.render('Valor de la mano: '+ str(obtener_valor_mano(mano_jugador)),True,blanco)
    texto_ganador = WIN_font.render(win_str[win_int],True,blanco)

    win.blit(texto_ganador, (LARGO_VENTANA//2-win_x[win_int], ALTO_VENTANA//2-win_y[win_int]))
    win.blit(texto_valor_mano, (15,ALTO_VENTANA-ALTO_CARTA-85))
    win.blit(ai_texto_mano, (15,15))
    win.blit(jugador_texto_mano, (15,ALTO_VENTANA-ALTO_CARTA-60))

    # Mostrar Instrucciones
    texto_esc = INST_font.render('Presiona [ESC] para reiniciar', True, blanco)
    texto_espacio = INST_font.render('Presiona [ESPACIO] para pedir carta', True, blanco)
    texto_enter = INST_font.render('Presiona [ENTER] para quedarte', True, blanco)
    texto_tab = INST_font.render('Presiona [TAB] para activar modo espectador', True, blanco)

    win.blit(texto_esc, (LARGO_VENTANA//2+30,ALTO_VENTANA//2+15))
    win.blit(texto_espacio, (LARGO_VENTANA//2+30,ALTO_VENTANA//2+30))
    win.blit(texto_enter, (LARGO_VENTANA//2+30,ALTO_VENTANA//2+45))
    win.blit(texto_tab, (LARGO_VENTANA//2+30,ALTO_VENTANA//2+60))

    # Mostrar Credito
    texto_autores = INST_font.render('Proyecto de Pedro Garcia, Juan Barragan, Santiago Isaza', True, blanco)
    texto_clase = INST_font.render('Algoritmos y programacion', True, blanco)

    win.blit(texto_autores, (290,7))
    win.blit(texto_clase, (450,7+15))

    # Mostrar Cartas de AI si modo espectador esta activado
    if espectar:
        texto_valor_mano_AI = GUI_font.render(str(obtener_valor_mano(mano_AI)),True,blanco)
        win.blit(texto_valor_mano_AI, (175,15))



# Crear GUI
pygame.init()

# Inicializar ventana GUI
LARGO_VENTANA = 600
ALTO_VENTANA = 500
win = pygame.display.set_mode((LARGO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("BlackJack (Proyecto de PG, JB, SI)")


# Inicializar Datos de las Cartas
VALORES_CARTAS = [11,2,3,4,5,6,7,8,9,10,10,10,10]
NOMBRES_CARTAS = list(range(1,14))
PALOS_CARTAS = list(range(1,5))

# Define tamaño de las cartas en pixeles
LARGO_CARTA = 100
ALTO_CARTA = 150

cartas_img_dir = []
IMAGENES_CARTAS = []

# Define colors in RGB values
negro = (0,0,0)
blanco = (255,255,255)


for i in NOMBRES_CARTAS:
    for j in PALOS_CARTAS:
        cartas_img_dir.append("images/" + str(i) + "-" + str(j) + ".png")

for i in cartas_img_dir:
    IMAGENES_CARTAS.append(pygame.transform.scale(pygame.image.load(i), (LARGO_CARTA, ALTO_CARTA)))

carta_escondida = Carta(0,0,0,pygame.transform.scale(pygame.image.load("images/carta_escondida.png"), (LARGO_CARTA, ALTO_CARTA)))


# Inicializar barajas de jugador y AI
mano_jugador = []
carta_x_pos = []
carta_y_pos = []

mano_AI = []
AI_carta_x_pos = []
AI_carta_y_pos = []

mano_AI_escondida = []
escondida_carta_x_pos = []
escondida_carta_y_pos = []

X_INICIAL = 30
Y_INICIAL = ALTO_VENTANA-ALTO_CARTA-30
AI_Y_INICIAL = 45
DESPLAZO_INICIAL = 30


# Inicializar propiedades de texto
GUI_font = pygame.font.SysFont(None, 32)
WIN_font = pygame.font.SysFont(None, 42)
INST_font = pygame.font.SysFont(None, 16)
TITLE_font = pygame.font.SysFont(None, 24)

win_int = 0
win_str = ['', 'JUGADOR GANA', 'AI GANA', 'JUGADOR SE EXCEDE — AI GANA', 'JUGADOR GANA — AI SE EXCEDE', 'EMPATE', 'NO HAY GANADOR']
win_x = [0, 100, 65, 180, 180, 40, 100]
win_y = [0, 30, 30, 30, 30, 30, 30]


# Inicializar booleans para controlar GUI
loop_principal = 0
ejecutar_juego = True
revelar = False
sesion = True
espectar = False


# Crear baraja y una copia de la baraja para mantener la copia original intacta
baraja_original = crearBaraja()
baraja_entera = list(baraja_original)


# Loop principal del juego
while ejecutar_juego:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutar_juego = False

    # Crear fondo
    bg = pygame.image.load("images/fondo.png")
    win.blit(bg, (0, 0))
    mostrar_texto()

    # Para prevenir 'button spam'
    if loop_principal > 0:
        loop_principal += 1
    if loop_principal > 5:
        loop_principal = 0


    # Obtener teclas presionadas
    teclas = pygame.key.get_pressed()

    # Reiniciar juego
    if teclas[pygame.K_ESCAPE]:
        baraja_entera = list(baraja_original)
        ejecutar_juego = True
        loop_principal = 0
        win_int = 0
        revelar = False
        sesion = True
        mano_jugador = []
        carta_x_pos = []
        carta_y_pos = []
        mano_AI = []
        AI_carta_x_pos = []
        AI_carta_y_pos = []
        mano_AI_escondida = []
        escondida_carta_x_pos = []
        escondida_carta_y_pos = []

    # Pedir carta
    if teclas[pygame.K_SPACE] and loop_principal == 0 and sesion:
        repartir_jugador()
        loop_principal = 1
        
        pide_AI = repartir_AI()

        print("AI: ", end='')
        print(obtener_valor_mano(mano_AI))

        # Probar todos los resultados posibles
        if obtener_valor_mano(mano_AI) > 21 and obtener_valor_mano(mano_jugador) > 21:
            sesion = False
            print("NO HAY GANADOR")
            win_int = 6
            revelar = True
        elif obtener_valor_mano(mano_AI) > 21:
            sesion = False
            print("AI SE EXCEDE, JUGADOR GANA")
            win_int = 4
            revelar = True
        elif obtener_valor_mano(mano_jugador) > 21:
            print('JUGADOR SE EXCEDE, AI GANA')
            win_int = 3
            sesion = False
            revelar = True
        elif obtener_valor_mano(mano_AI) == 21 and obtener_valor_mano(mano_jugador) == 21:
            print('EMPATE')
            win_int = 5
            sesion = False
            revelar = True
        elif obtener_valor_mano(mano_AI) == 21 and obtener_valor_mano(mano_jugador) != 21:
            print('AI GANA')
            win_int = 2
            sesion = False
            revelar = True
        elif obtener_valor_mano(mano_AI) != 21 and obtener_valor_mano(mano_jugador) == 21:
            print('JUGADOR GANA')
            win_int = 1
            sesion = False
            revelar = True
    
    # JUGADOR PASA
    if (teclas[pygame.K_KP_ENTER] or teclas[pygame.K_RETURN]) and loop_principal == 0 and sesion:
        loop_principal = 1

        pide_AI = repartir_AI()

        print("AI: ", end='')
        print(obtener_valor_mano(mano_AI))

        # Probar todos los resultados posibles
        if (pide_AI == False):
            if obtener_valor_mano(mano_AI) > obtener_valor_mano(mano_jugador):
                sesion = False
                print('AI GANA')
                win_int = 2
                revelar = True
            elif obtener_valor_mano(mano_AI) < obtener_valor_mano(mano_jugador):
                sesion = False
                print('JUGADOR GANA')
                win_int = 1
                revelar = True
            else:
                sesion = False
                print("TIED")
                win_int = 5
                revelar = True
        else:
            if obtener_valor_mano(mano_AI) > 21 and obtener_valor_mano(mano_jugador) > 21:
                sesion = False
                print("NO HAY GANADOR")
                win_int = 6
                revelar = True
            elif obtener_valor_mano(mano_AI) > 21:
                sesion = False
                print("AI SE EXCEDE, JUGADOR GANA")
                win_int = 4
                revelar = True
            elif obtener_valor_mano(mano_AI) == 21 and obtener_valor_mano(mano_jugador) == 21:
                print('EMPATE')
                win_int = 5
                sesion = False
                revelar = True
            elif obtener_valor_mano(mano_AI) == 21 and obtener_valor_mano(mano_jugador) != 21:
                print('AI GANA')
                win_int = 2
                sesion = False
                revelar = True
            elif obtener_valor_mano(mano_AI) != 21 and obtener_valor_mano(mano_jugador) == 21:
                print('JUGADOR GANA')
                win_int = 1
                sesion = False
                revelar = True

    # ACTIVAR O DESACTIVAR MODO DE ESPECTADOR
    if teclas[pygame.K_TAB] and loop_principal == 0:
        if espectar == False:
            espectar = True
        else:
            espectar = False

        loop_principal = 1

    mostrar_carta()

pygame.quit()