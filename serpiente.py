#---Se importa la librería pygame para crear juegos y random para posiciones aleatorias.
# Se inicializa Pygame con pygame.init() para preparar todo lo necesario.---
import pygame
import random

# --- INICIALIZAR PYGAME ---
pygame.init()

# --- CONFIGURACIÓN DE LA VENTANASe definen el ancho y alto de la ventana.
# Se crea la ventana donde se dibujará el juego.
# Se pone un título a la ventana. ---
ancho = 600
alto = 400
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de la Serpiente - Parte 1")

# --- COLORES ---
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# --- CONFIGURACIÓN DE LA SERPIENTE
# La serpiente está representada como un cuadrado de 20x20 píxeles.
# La posición inicial de la serpiente está en el centro de la ventana.
# La velocidad inicial es 0 (la serpiente no se mueve hasta que se presione una tecla). ---
tamaño_bloque = 20
serpiente_x = ancho // 2
serpiente_y = alto // 2
velocidad_x = 0
velocidad_y = 0

# --- CONFIGURACIÓN DE LA FRUTA
# La fruta aparece en una posición aleatoria, pero alineada con la cuadrícula de bloques de 20 px.
# Esto garantiza que la fruta siempre esté en una posición válida para la serpiente. ---
fruta_x = random.randrange(0, ancho - tamaño_bloque, tamaño_bloque)
fruta_y = random.randrange(0, alto - tamaño_bloque, tamaño_bloque)

# --- BUCLE PRINCIPAL DEL JUEGO 
# Aquí se ejecuta todo el juego hasta que el jugador cierre la ventana.---
juego_terminado = False
while not juego_terminado:

    # --- MANEJAR EVENTOS (TECLADO, SALIDA)
    # Se detecta si el jugador quiere salir (cerrar ventana).
    # Si presiona una flecha, se cambia la dirección y velocidad de la serpiente para que se mueva en esa dirección.
    # La velocidad es igual al tamaño del bloque para que la serpiente se mueva exactamente un bloque por actualización. ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_terminado = True
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                velocidad_x = 0
                velocidad_y = -tamaño_bloque
            elif evento.key == pygame.K_DOWN:
                velocidad_x = 0
                velocidad_y = tamaño_bloque
            elif evento.key == pygame.K_LEFT:
                velocidad_x = -tamaño_bloque
                velocidad_y = 0
            elif evento.key == pygame.K_RIGHT:
                velocidad_x = tamaño_bloque
                velocidad_y = 0

    # --- ACTUALIZAR POSICIÓN DE LA SERPIENTE
    # Se mueve la serpiente sumando la velocidad a la posición actual. ---
    serpiente_x += velocidad_x
    serpiente_y += velocidad_y

    # --- DIBUJAR EN PANTALLA 
    # Se pinta el fondo negro.
    # Se dibuja la serpiente como un rectángulo verde.
    # Se dibuja la fruta como un rectángulo rojo.---
    ventana.fill(NEGRO)  # Fondo
    pygame.draw.rect(ventana, VERDE, [serpiente_x, serpiente_y, tamaño_bloque, tamaño_bloque])  # Serpiente
    pygame.draw.rect(ventana, ROJO, [fruta_x, fruta_y, tamaño_bloque, tamaño_bloque])  # Fruta

    # --- ACTUALIZAR PANTALLA ---
    pygame.display.update()

    # --- CONTROLAR LA VELOCIDAD DEL JUEGO ---
    pygame.time.Clock().tick(10)

# --- SALIR DEL JUEGO ---
pygame.quit()
