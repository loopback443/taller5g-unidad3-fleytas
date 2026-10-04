# ejercicio1_casa.py
# Ejercicio 1 - Casa dibujada con el algoritmo DDA
from PIL import Image
import math


# Algoritmo DDA avanza de a pasos pequeños desde (x0,y0) hasta (x1,y1)
def dda(pixels, x0, y0, x1, y1, color, ancho, alto):
    dx = x1 - x0
    dy = y1 - y0
    pasos = max(abs(dx), abs(dy))
    if pasos == 0:
        return
    x_inc = dx / pasos
    y_inc = dy / pasos
    x, y = x0, y0
    for i in range(int(pasos) + 1):
        if 0 <= round(x) < ancho and 0 <= round(y) < alto:
            pixels[round(x), round(y)] = color
        x += x_inc
        y += y_inc


# Rectangulo -> 4 lineas (arriba, derecha, abajo, izquierda)
def dibujar_rectangulo(pixels, x0, y0, x1, y1, color, ancho, alto):
    dda(pixels, x0, y0, x1, y0, color, ancho, alto)
    dda(pixels, x1, y0, x1, y1, color, ancho, alto)
    dda(pixels, x1, y1, x0, y1, color, ancho, alto)
    dda(pixels, x0, y1, x0, y0, color, ancho, alto)


# Triangulo -> 3 lineas que unen los vertices
def dibujar_triangulo(pixels, p1, p2, p3, color, ancho, alto):
    dda(pixels, p1[0], p1[1], p2[0], p2[1], color, ancho, alto)
    dda(pixels, p2[0], p2[1], p3[0], p3[1], color, ancho, alto)
    dda(pixels, p3[0], p3[1], p1[0], p1[1], color, ancho, alto)


# Puerta-> un rectangulo
def dibujar_puerta(pixels, color, ancho, alto):
    dibujar_rectangulo(pixels, 270, 330, 330, 420, color, ancho, alto)


# Ventanas-> dos cuadrados de 50x50
def dibujar_ventanas(pixels, color, ancho, alto):
    dibujar_rectangulo(pixels, 195, 280, 245, 330, color, ancho, alto)
    dibujar_rectangulo(pixels, 355, 280, 405, 330, color, ancho, alto)


# Sol-> rayos desde el centro usando coordenadas polares
def dibujar_sol(pixels, cx, cy, radio, n_rayos, color, ancho, alto):
    for i in range(n_rayos):
        angulo = 2 * math.pi * i / n_rayos
        x = cx + int(radio * math.cos(angulo))
        y = cy + int(radio * math.sin(angulo))
        dda(pixels, cx, cy, x, y, color, ancho, alto)


# Piso-> linea horizontal de lado a lado
def dibujar_piso(pixels, y, color, ancho, alto):
    dda(pixels, 0, y, ancho - 1, y, color, ancho, alto)


# Extra-> arbol con tronco (rectangulo) y copa (triangulo)
def dibujar_arbol(pixels, x, y, ancho, alto):
    dibujar_rectangulo(pixels, x - 8, y - 50, x + 8, y, (120, 70, 20), ancho, alto)
    dibujar_triangulo(pixels, (x - 40, y - 50), (x, y - 140), (x + 40, y - 50), (0, 150, 0), ancho, alto)


# Programa principal
ancho, alto = 600, 500
imagen = Image.new("RGB", (ancho, alto), (200, 230, 255))
pixels = imagen.load()

dibujar_piso(pixels, 420, (0, 100, 0), ancho, alto)                                   # verde oscuro
dibujar_rectangulo(pixels, 170, 250, 430, 420, (0, 0, 150), ancho, alto)              # cuerpo, azul
dibujar_triangulo(pixels, (150, 250), (300, 140), (450, 250), (200, 0, 0), ancho, alto)  # techo, rojo
dibujar_puerta(pixels, (100, 50, 0), ancho, alto)                                     # marron
dibujar_ventanas(pixels, (0, 150, 200), ancho, alto)                                  # celeste
dibujar_sol(pixels, 520, 80, 45, 16, (255, 200, 0), ancho, alto)                      # amarillo
dibujar_arbol(pixels, 80, 420, ancho, alto)

imagen.save("casa.png")
print("casa.png generada")
