import cv2
import numpy as np
import matplotlib.pyplot as plt

# nombre de la imagen
nombre_imagen = '../AulaIA_imagenes/Lenna.jpg'

# lectura de la imagen
imagen = cv2.imread(nombre_imagen)

# comprobar si la imagen se ha leído bien
if imagen is None:
    print('Error leyendo imagen !!!!')
    exit(0)

# mostrar imagen
cv2.imshow('imagen original', imagen)
cv2.waitKey(10)

# convertir la imagen de RGB a niveles de grises
imagenGrises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagen grises', imagenGrises)
cv2.waitKey(10)

mascaraX = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
mascaraY = np.transpose(mascaraX)

print('Máscara sobel X\n{}'.format(mascaraX))
print('Máscara sobel Y\n{}'.format(mascaraY))

numFilas, numColumnas = imagenGrises.shape

# realizar convolución con máscara de sobel X
resultadoX = np.zeros((numFilas, numColumnas))
for fila in range(1, numFilas - 1):
    print('Procesando fila {} :'.format(fila))
    for columna in range(1, numColumnas - 1):
        resultadoX[fila, columna] = np.sum(imagenGrises[fila - 1:fila + 2, columna - 1:columna + 2] * mascaraX)

valorMaximo = np.amax(np.abs(resultadoX))
valorMinimo = np.amin(np.abs(resultadoX))
print('Valor máximo después convolución máscara X: {}'.format(valorMaximo))
print('Valor mínimo después convolución máscara Y: {}'.format(valorMinimo))

# normalizar valores del resultado entre 0 y 255
imagenResultado = np.uint8((np.abs(resultadoX) - valorMinimo) / (valorMaximo - valorMinimo) * 255)

valorMaximo = np.amax(imagenResultado)
valorMinimo = np.amin(imagenResultado)
print('Valor máximo después normalizar {}'.format(valorMaximo))
print('Valor mínimo después normalizar {}'.format(valorMinimo))

# mostrar resultado convolución máscara X
cv2.imshow('Resultado Sobel', imagenResultado)
cv2.waitKey(-1)
