import pygame
import random

# --- INICIALIZAR PYGAME ---
pygame.init()

# --- CONFIGURACIÓN DE LA VENTANA ---
ancho = 600
alto = 400
ventana = pygame.display.set_mode((ancho, alto))  # Se crea la ventana del juego
pygame.display.set_caption("Juego de la Serpiente - Completo")  # Título de la ventana

# --- COLORES (RGB) ---
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# --- CONFIGURACIÓN DE LA SERPIENTE ---
tamaño_bloque = 20  # Tamaño de cada segmento de la serpiente (cuadrado)
serpiente_x = ancho // 2  # Posición inicial (centro de la pantalla en X)
serpiente_y = alto // 2   # Posición inicial (centro de la pantalla en Y)
velocidad_x = 0           # Velocidad inicial en X (serpiente quieta)
velocidad_y = 0           # Velocidad inicial en Y (serpiente quieta)

# Lista para guardar los segmentos de la serpiente
cuerpo_serpiente = []
longitud_serpiente = 1  # La serpiente empieza con 1 bloque

# --- CONFIGURACIÓN DE LA FRUTA ---
# La fruta aparece en una posición aleatoria que sea múltiplo del tamaño de bloque
fruta_x = random.randrange(0, ancho - tamaño_bloque, tamaño_bloque)
fruta_y = random.randrange(0, alto - tamaño_bloque, tamaño_bloque)

# --- PUNTUACIÓN ---
puntuacion = 0
fuente = pygame.font.SysFont("Arial", 25)  # Fuente para mostrar texto en pantalla

# --- CONTROL DEL TIEMPO ---
reloj = pygame.time.Clock()  # Para controlar los FPS (velocidad del juego)

# --- BUCLE PRINCIPAL DEL JUEGO ---
juego_terminado = False
while not juego_terminado:
    # --- MANEJAR EVENTOS (teclado, salida de ventana) ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # Cuando se cierra la ventana
            juego_terminado = True
        elif evento.type == pygame.KEYDOWN:  # Cuando se presiona una tecla
            # Control de movimiento (evita retroceder sobre sí mismo)
            if evento.key == pygame.K_UP and velocidad_y == 0:
                velocidad_x = 0
                velocidad_y = -tamaño_bloque
            elif evento.key == pygame.K_DOWN and velocidad_y == 0:
                velocidad_x = 0
                velocidad_y = tamaño_bloque
            elif evento.key == pygame.K_LEFT and velocidad_x == 0:
                velocidad_x = -tamaño_bloque
                velocidad_y = 0
            elif evento.key == pygame.K_RIGHT and velocidad_x == 0:
                velocidad_x = tamaño_bloque
                velocidad_y = 0

    # --- ACTUALIZAR POSICIÓN DE LA SERPIENTE ---
    serpiente_x += velocidad_x
    serpiente_y += velocidad_y

    # --- DETECTAR COLISIÓN CON LOS BORDES ---
    if serpiente_x < 0 or serpiente_x >= ancho or serpiente_y < 0 or serpiente_y >= alto:
        juego_terminado = True

    # --- ACTUALIZAR CUERPO DE LA SERPIENTE ---
    cabeza = [serpiente_x, serpiente_y]
    cuerpo_serpiente.append(cabeza)

    # Si la serpiente supera su longitud, eliminar el último bloque (cola)
    if len(cuerpo_serpiente) > longitud_serpiente:
        del cuerpo_serpiente[0]

    # --- DETECTAR COLISIÓN CON EL PROPIO CUERPO ---
    for segmento in cuerpo_serpiente[:-1]:  # Excluye la cabeza
        if segmento == cabeza:
            juego_terminado = True

    # --- DETECTAR SI COME LA FRUTA ---
    if serpiente_x == fruta_x and serpiente_y == fruta_y:
        fruta_x = random.randrange(0, ancho - tamaño_bloque, tamaño_bloque)
        fruta_y = random.randrange(0, alto - tamaño_bloque, tamaño_bloque)
        longitud_serpiente += 1  # Aumenta el tamaño de la serpiente
        puntuacion += 10         # Suma puntos

    # --- DIBUJAR ELEMENTOS EN PANTALLA ---
    ventana.fill(NEGRO)  # Fondo negro

    # Dibujar la serpiente
    for segmento in cuerpo_serpiente:
        pygame.draw.rect(ventana, VERDE, [segmento[0], segmento[1], tamaño_bloque, tamaño_bloque])

    # Dibujar la fruta
    pygame.draw.rect(ventana, ROJO, [fruta_x, fruta_y, tamaño_bloque, tamaño_bloque])

    # --- MOSTRAR PUNTUACIÓN ---
    texto_puntos = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
    ventana.blit(texto_puntos, [10, 10])

    # --- ACTUALIZAR PANTALLA ---
    pygame.display.update()

    # --- CONTROLAR LA VELOCIDAD DEL JUEGO ---
    reloj.tick(10)  # El juego corre a 10 FPS

# --- PANTALLA DE GAME OVER ---
ventana.fill(NEGRO)
texto_game_over = fuente.render("GAME OVER", True, ROJO)
texto_final = fuente.render(f"Puntuación final: {puntuacion}", True, BLANCO)
ventana.blit(texto_game_over, [ancho // 2 - 50, alto // 2 - 30])
ventana.blit(texto_final, [ancho // 2 - 80, alto // 2 + 10])
pygame.display.update()
pygame.time.wait(3000)  # Espera 3 segundos antes de cerrar

# --- SALIR DEL JUEGO ---
pygame.quit()