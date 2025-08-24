#---Se importa la librería pygame para crear juegos y random para posiciones aleatorias.
# Se inicializa Pygame con pygame.init() para preparar todo lo necesario.---

import pygame
import random

# ---------------------------
# INICIALIZAR PYGAME Y VENTANA
# ---------------------------
pygame.init()
ancho = 600
alto = 400
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juego de la Serpiente - Parte 1 & 2 (Inicio | Pausa | Reinicio)")
# --- CONFIGURACIÓN DE LA VENTANASe definen el ancho y alto de la ventana.
# Se crea la ventana donde se dibujará el juego.
# Se pone un título a la ventana. ---

# ---------------------------
# COLORES - CONFIGURACIÓN DE LA SERPIENTE
# ---------------------------
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 200, 0)
VERDE_CABEZA = (0, 255, 120)
ROJO = (255, 50, 50)
GRIS = (80, 80, 80)
# La serpiente está representada como un cuadrado de 20x20 píxeles.
# La posición inicial de la serpiente está en el centro de la ventana.
# La velocidad inicial es 0 (la serpiente no se mueve hasta que se presione una tecla). ---


# ---------------------------
# PARAMETROS DE JUEGO
# ---------------------------
tam_bloque = 20
velocidad_juego = 10  # FPS base

# ---------------------------
# ESTADOS DEL JUEGO
#   "menu"      -> pantalla de inicio
#   "jugando"   -> bucle principal
#   "pausa"     -> detenido temporalmente
#   "gameover"  -> fin de partida
# ---------------------------
estado = "menu"

# ---------------------------
# VARIABLES DE LA SERPIENTE Y FRUTA
# ---------------------------
def reiniciar_variables():
    # Serpiente al centro
    serp_x = ancho // 2
    serp_y = alto // 2
    vel_x = 0
    vel_y = 0

    # Cuerpo (lista de [x,y]) y longitud
    cuerpo = []
    longitud = 1

    # Fruta en posición múltiplo de tam_bloque
    # La fruta aparece en una posición aleatoria, pero alineada con la cuadrícula de bloques de 20 px.
# Esto garantiza que la fruta siempre esté en una posición válida para la serpiente. ---
    fruta_x = random.randrange(0, ancho - tam_bloque, tam_bloque)
    fruta_y = random.randrange(0, alto - tam_bloque, tam_bloque)

    # Puntaje
    puntos = 0

    return serp_x, serp_y, vel_x, vel_y, cuerpo, longitud, fruta_x, fruta_y, puntos

(serp_x, serp_y,
 vel_x, vel_y,
 cuerpo_serp, longitud_serp,
 fruta_x, fruta_y,
 puntuacion) = reiniciar_variables()

mejor_puntuacion = 0  # récord de la sesión

# Fuentes
fuente = pygame.font.SysFont("Arial", 24)
fuente_titulo = pygame.font.SysFont("Arial", 36)

# Reloj
reloj = pygame.time.Clock()

# ---------------------------
# BUCLE PRINCIPAL
# ---------------------------
# Aquí se ejecuta todo el juego hasta que el jugador cierre la ventana.---
ejecutando = True
while ejecutando:
    # -----------------------
    # --- MANEJAR EVENTOS (TECLADO, SALIDA)
    # Se detecta si el jugador quiere salir (cerrar ventana).
    # Si presiona una flecha, se cambia la dirección y velocidad de la serpiente para que se mueva en esa dirección.
    # La velocidad es igual al tamaño del bloque para que la serpiente se mueva exactamente un bloque por actualización. ---
    # -----------------------
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

        if estado == "menu":
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:     # Enter para iniciar
                    estado = "jugando"
                    # Reiniciamos variables al iniciar
                    (serp_x, serp_y,
                     vel_x, vel_y,
                     cuerpo_serp, longitud_serp,
                     fruta_x, fruta_y,
                     puntuacion) = reiniciar_variables()
                if evento.key == pygame.K_ESCAPE:     # Salir
                    ejecutando = False

        elif estado == "jugando":
            if evento.type == pygame.KEYDOWN:
                # Movimiento: evitamos giro 180° (no dejar moverse en eje opuesto inmediato)
                if (evento.key == pygame.K_UP or evento.key == pygame.K_w) and vel_y == 0:
                    vel_x = 0
                    vel_y = -tam_bloque
                elif (evento.key == pygame.K_DOWN or evento.key == pygame.K_s) and vel_y == 0:
                    vel_x = 0
                    vel_y = tam_bloque
                elif (evento.key == pygame.K_LEFT or evento.key == pygame.K_a) and vel_x == 0:
                    vel_x = -tam_bloque
                    vel_y = 0
                elif (evento.key == pygame.K_RIGHT or evento.key == pygame.K_d) and vel_x == 0:
                    vel_x = tam_bloque
                    vel_y = 0

                # Pausar
                if evento.key == pygame.K_p:
                    estado = "pausa"
                # Escape para salir directo
                if evento.key == pygame.K_ESCAPE:
                    ejecutando = False

        elif estado == "pausa":
            if evento.type == pygame.KEYDOWN:
                # Reanudar
                if evento.key == pygame.K_p or evento.key == pygame.K_RETURN:
                    estado = "jugando"
                # Reiniciar desde pausa
                if evento.key == pygame.K_r:
                    (serp_x, serp_y,
                     vel_x, vel_y,
                     cuerpo_serp, longitud_serp,
                     fruta_x, fruta_y,
                     puntuacion) = reiniciar_variables()
                    estado = "jugando"
                # Salir
                if evento.key == pygame.K_ESCAPE:
                    ejecutando = False

        elif estado == "gameover":
            if evento.type == pygame.KEYDOWN:
                # Reiniciar
                if evento.key == pygame.K_r:
                    (serp_x, serp_y,
                     vel_x, vel_y,
                     cuerpo_serp, longitud_serp,
                     fruta_x, fruta_y,
                     puntuacion) = reiniciar_variables()
                    estado = "jugando"
                # Volver al menú
                if evento.key == pygame.K_m:
                    estado = "menu"
                # Salir
                if evento.key == pygame.K_ESCAPE:
                    ejecutando = False

    # -----------------------
    # LOGICA POR ESTADO
    # -----------------------
    if estado == "menu":
        ventana.fill(NEGRO)
        titulo = fuente_titulo.render("SNAKE", True, BLANCO)
        sub = fuente.render("Presiona ENTER para iniciar", True, BLANCO)
        tips = fuente.render("Flechas/WASD: mover | P: pausa | R: reiniciar (en Game Over/Pausa)", True, GRIS)
        ventana.blit(titulo, (ancho//2 - titulo.get_width()//2, alto//2 - 80))
        ventana.blit(sub, (ancho//2 - sub.get_width()//2, alto//2 - 20))
        ventana.blit(tips, (ancho//2 - tips.get_width()//2, alto//2 + 20))

    elif estado == "jugando":
        # 1) Mover serpiente
        serp_x += vel_x
        serp_y += vel_y

        # 2) Colisión con paredes -> Game Over
        if serp_x < 0 or serp_x >= ancho or serp_y < 0 or serp_y >= alto:
            estado = "gameover"

        # 3) Actualizar cuerpo (agregar cabeza y limitar a longitud)
        cabeza = [serp_x, serp_y]
        cuerpo_serp.append(cabeza)
        if len(cuerpo_serp) > longitud_serp:
            del cuerpo_serp[0]

        # 4) Colisión consigo misma -> Game Over
        for seg in cuerpo_serp[:-1]:
            if seg == cabeza:
                estado = "gameover"
                break

        # 5) Comer fruta -> nueva fruta, crecer y sumar puntos
        if serp_x == fruta_x and serp_y == fruta_y:
            fruta_x = random.randrange(0, ancho - tam_bloque, tam_bloque)
            fruta_y = random.randrange(0, alto - tam_bloque, tam_bloque)
            longitud_serp += 1
            puntuacion += 10
            if puntuacion > mejor_puntuacion:
                mejor_puntuacion = puntuacion

        # 6) DIBUJO
        ventana.fill(NEGRO)
        # Fruta
        pygame.draw.rect(ventana, ROJO, (fruta_x, fruta_y, tam_bloque, tam_bloque))
        # Serpiente (cabeza más clara)
        for i, seg in enumerate(cuerpo_serp):
            color = VERDE_CABEZA if i == len(cuerpo_serp)-1 else VERDE
            pygame.draw.rect(ventana, color, (seg[0], seg[1], tam_bloque, tam_bloque))
        # HUD
        hud = fuente.render(f"Puntos: {puntuacion}   Mejor: {mejor_puntuacion}", True, BLANCO)
        ventana.blit(hud, (10, 10))

    elif estado == "pausa":
        ventana.fill(NEGRO)
        txt = fuente_titulo.render("PAUSA", True, BLANCO)
        hint = fuente.render("ENTER/P: reanudar | R: reiniciar | ESC: salir", True, GRIS)
        ventana.blit(txt, (ancho//2 - txt.get_width()//2, alto//2 - 40))
        ventana.blit(hint, (ancho//2 - hint.get_width()//2, alto//2 + 10))

    elif estado == "gameover":
        ventana.fill(NEGRO)
        msg = fuente_titulo.render("GAME OVER", True, ROJO)
        score = fuente.render(f"Puntuación: {puntuacion}   Mejor: {mejor_puntuacion}", True, BLANCO)
        hint = fuente.render("R: reiniciar | M: menú | ESC: salir", True, GRIS)
        ventana.blit(msg, (ancho//2 - msg.get_width()//2, alto//2 - 60))
        ventana.blit(score, (ancho//2 - score.get_width()//2, alto//2 - 10))
        ventana.blit(hint, (ancho//2 - hint.get_width()//2, alto//2 + 30))

    # -----------------------
    # ACTUALIZAR PANTALLA Y TIEMPO
    # -----------------------
    pygame.display.flip()
    reloj.tick(velocidad_juego)

# Salir
pygame.quit()
