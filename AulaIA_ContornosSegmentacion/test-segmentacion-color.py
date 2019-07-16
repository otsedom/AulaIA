import cv2
import numpy as np

# nombre de la imagen
nombreImagen = '../AulaIA_imagenes/indurain.jpg'

# lectura de la imagen desde disco
imagen = cv2.imread(nombreImagen)

# comprobar si la imagen se ha leído bien
if imagen is None:
    print('Error leyendo imagen !!!!')
    exit(0)

# mostrar imagen original
cv2.imshow('imagen original', imagen)
cv2.waitKey(20)

# obtiene tamaño de la imagen
numFilas, numColumnas, numColores = imagen.shape

# crea una nueva imagen en color negro (todo a cero)
imagenResultado = np.zeros((numFilas, numColumnas), dtype=np.uint8)

# recorre toda la imagen comprobando el valor RGB de cada pixel
for fila in range(0, numFilas):
    # print('procesando fila {}'.format(fila))
    for columna in range(0, numColumnas):
        b = imagen[fila, columna, 0]
        g = imagen[fila, columna, 1]
        r = imagen[fila, columna, 2]

        # si el valor RGB está dentro del rango se marca como blanco
        if 120 <= r <= 170 and 0 <= g <= 35 and 0 <= b <= 35:
            imagenResultado[fila, columna] = 255

# mostrar imagen umbralizada
cv2.imshow('imagen umbralizada', imagenResultado)
cv2.waitKey(0)
