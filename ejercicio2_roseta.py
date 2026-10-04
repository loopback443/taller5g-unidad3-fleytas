# ejercicio2_roseta.py
# Ejercicio 2 - Rosetas geometricas con el algoritmo de Bresenham
from PIL import Image
import math
# Algoritmo de Bresenham: solo usa enteros y un termino de error
def bresenham(pixels, x0, y0, x1, y1, color, ancho, alto):
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    while True:
        if 0 <= x0 < ancho and 0 <= y0 < alto:
            pixels[x0, y0] = color
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy
# Devuelve n puntos repartidos sobre una circunferencia
def generar_puntos_circulo(cx, cy, radio, n):
    puntos = []
    for i in range(n):
        angulo = 2 * math.pi * i / n
        x = cx + int(radio * math.cos(angulo))
        y = cy + int(radio * math.sin(angulo))
        puntos.append((x, y))
    return puntos

# Une cada punto con todos los demas.
# El color depende de que tan lejos del centro pasa la linea (usando su punto medio):
# cerca del centro = azul, cerca del borde = rojo
def dibujar_roseta(pixels, puntos, ancho, alto):
    n = len(puntos)
    for i in range(n):
        for j in range(i + 1, n):
            mx = (puntos[i][0] + puntos[j][0]) / 2
            my = (puntos[i][1] + puntos[j][1]) / 2
            d = math.hypot(mx - ancho / 2, my - alto / 2) / 300
            color = (int(255 * d), 0, int(255 * (1 - d)))
            bresenham(pixels, puntos[i][0], puntos[i][1],
                      puntos[j][0], puntos[j][1], color, ancho, alto)


# Generar las tres variantes
for n in [12, 24, 36]:
    img = Image.new("RGB", (700, 700), "white")
    pixels = img.load()
    puntos = generar_puntos_circulo(350, 350, 300, n)
    dibujar_roseta(pixels, puntos, 700, 700)
    img.save(f"roseta_{n}.png")
    if n == 24:
        img.save("roseta.png")

# Extra: roseta uniendo cada punto solo con el que esta 5 lugares adelante
img = Image.new("RGB", (700, 700), "black")
pixels = img.load()
puntos = generar_puntos_circulo(350, 350, 300, 24)
for i in range(24):
    j = (i + 5) % 24
    bresenham(pixels, puntos[i][0], puntos[i][1], puntos[j][0], puntos[j][1], (255, 200, 0), 700, 700)
img.save("roseta_salto5.png")

print("rosetas generadas")
