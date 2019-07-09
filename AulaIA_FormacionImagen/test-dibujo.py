import cv2
import numpy as np

# nombre de la imagen a mostrar
nombreImagen = '../AulaIA_imagenes/indurain.jpg'

# lectura de la imagen desde disco
imagen = cv2.imread(nombreImagen)

# comprobar si la imagen se ha leído bien
if imagen is None:
    print('Error leyendo imagen !!!!')
    exit(0)

# dibuja línea
imagenLinea = np.copy(imagen)
ptoInicial = (500, 10)  # (x,y)
ptoFinal = (500, 565)
color = (255, 0, 255)  # (B,G,R)
ancho = 2
cv2.line(imagenLinea, ptoInicial, ptoFinal, color, ancho)

# muestra imagen con línea
cv2.imshow('Línea', imagenLinea)
cv2.waitKey(1)

# dibuja círculo
imagenCirculo = np.copy(imagen)
centro = (875, 72)
radio = 20
color = (0, 255, 0)  # (B,G,R)
cv2.circle(imagenCirculo, centro, radio, color, ancho)

# muestra imagen con círculo
cv2.imshow('Círculo', imagenCirculo)
cv2.waitKey(1)

# dibuja elipse
imagenElipse = np.copy(imagen)
centro = (380, 175)
radios = (30, 60) # (radio X, radio Y)
color = (255,255,0)
anguloRotacion = 0
anguloInicial = 0
anguloFinal = 360
cv2.ellipse(imagenElipse, centro, radios, anguloRotacion, anguloInicial, anguloFinal, color, ancho)

# muestra imagen con elipse
cv2.imshow('Elipse', imagenElipse)
cv2.waitKey(1)

# dibuja rectángulo
imagenRectangulo = np.copy(imagen)
esquinaSupIzda = (500, 60)
esquinaInfDcha = (890, 300) # (radio X, radio Y)
color = (0, 0, 255)
cv2.rectangle(imagenRectangulo, esquinaSupIzda, esquinaInfDcha, color, ancho)

# muestra imagen con rectángulo
cv2.imshow('Reactángulo', imagenRectangulo)
cv2.waitKey(1)

# dibuja triángulo relleno
imagentriangulo = np.copy(imagen)
pt1 = (10, 10)
pt2 = (200, 100)
pt3 = (120, 400)
triangle_cnt = np.array([pt1, pt2, pt3])
cv2.drawContours(imagentriangulo, [triangle_cnt], 0, (0, 255, 0), -1)

# muestra imagen con triángulo
cv2.imshow('Rectángulo', imagentriangulo)
cv2.waitKey(1)

# espera pulsar tecla para terminar programa
cv2.waitKey(-1)

