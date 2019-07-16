import cv2
import numpy as np
import matplotlib.pyplot as plt

# nombre de la imagen a mostrar
nombre_imagen = '../AulaIA_imagenes/Lenna.jpg'

# lectura de la imagen desde disco
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

mascaraMedia = 1/9 * np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

print('Máscara media \n{}'.format(mascaraMedia))

numFilas, numColumnas = imagenGrises.shape

# realizar convolución con máscara de media
resultadoSuavizado = np.zeros((numFilas, numColumnas))
for fila in range(1, numFilas - 1):
    print('Procesando fila {} :'.format(fila))
    for columna in range(1, numColumnas - 1):
        resultadoSuavizado[fila, columna] = np.sum(imagenGrises[fila - 1:fila + 2, columna - 1:columna + 2] * mascaraMedia)

# convertir los valores a un byte (0,255)
resultadoSuavizado = resultadoSuavizado.astype(np.uint8)

# mostrar resultado convolución máscara X
cv2.imshow('resultado', resultadoSuavizado)
cv2.waitKey(-1)


# cerrar todas las ventanas antes de terminar script
cv2.destroyAllWindows()

