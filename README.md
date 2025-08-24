# 🐍 Juego de la Serpiente en Python (Pygame)

##Materia
**Lógica de Programación 2-ECC-1A**

##Alumno
**Abel Andréss Ortiz Haro**

---

## 📌 Introducción
Este proyecto es una implementación básica del clásico **juego de la serpiente** usando **Python** y la librería **Pygame**.  

El objetivo del juego es mover la serpiente por la pantalla usando las flechas del teclado para alcanzar la fruta.  
Cada vez que la serpiente come una fruta, debería crecer y aumentar la dificultad (⚠️ en esta versión inicial, aún no crece ni hay colisiones).  

Este proyecto sirve como ejemplo educativo para aprender:
- ✅ Manejo de eventos en Pygame  
- ✅ Dibujo de elementos en pantalla  
- ✅ Uso de bucles de juego  
- ✅ Principios básicos de diseño de videojuegos

## Ejecución

Para ejecutar el juego, abre la terminal en la carpeta del proyecto y escribe:

python snake_game.py

## Diagramas
**1. Diagrama de Casos de Uso**

Jugador controla la serpiente con las flechas del teclado.

La serpiente se mueve automáticamente.

El sistema genera frutas en posiciones aleatorias.

**2. Diagrama de Arquitectura**

Jugador → controla la serpiente.

Sistema (Pygame) → maneja los eventos, dibuja la serpiente y fruta.

Lógica del juego → controla el movimiento y la detección de colisiones.

**3. Diagrama de Flujo**

Iniciar juego

Mostrar ventana

Mover serpiente

Detectar colisión con fruta

Actualizar pantalla

Repetir ciclo

##🛠️ Explicación de las principales funcionalidades
**1. Inicialización del juego**
pygame.init()


Inicia los módulos de Pygame para poder usar sus funciones.

**2. Configuración de la ventana**
ancho = 600
alto = 400
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Snake Game")

**3. Colores**
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)


#Se definen colores en formato RGB para pintar objetos en pantalla.

**4. Variables de la serpiente y fruta**
x = 300
y = 200
velocidad = 20
dx = 0
dy = 0
fruta_x = random.randrange(0, ancho, 20)
fruta_y = random.randrange(0, alto, 20)


x, y: posición inicial de la serpiente.

dx, dy: dirección del movimiento (cambia con las flechas).

fruta_x, fruta_y: posición aleatoria de la fruta.

**5. Bucle principal del juego**
while en_juego:
    for evento in pygame.event.get():
        ...
    ventana.fill(NEGRO)
    pygame.draw.rect(ventana, VERDE, (x, y, 20, 20))
    pygame.draw.rect(ventana, ROJO, (fruta_x, fruta_y, 20, 20))
    pygame.display.update()
    reloj.tick(10)

