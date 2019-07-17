import cv2
import numpy as np

# nombre de la imagen a mostrar
nombre_imagen = '../AulaIA_imagenes/Cicer2.jpg'

# lectura de la imagen desde disco
imagen = cv2.imread(nombre_imagen)

# comprobar si la imagen se ha leído bien
if imagen is None:
    print('Error leyendo imagen !!!!')
    exit(0)

alto, ancho, componentes = imagen.shape

print('Alto de la imagen: {}'.format(alto))
print('Ancho de la imagen: {}'.format(ancho))
print('Número componentes: {}'.format(componentes))

for x in range(0, ancho):
    for y in range(0, (int)(alto / 2)):
        # Cancelamos una componente
        imagen[y,x,1] = 0

cv2.imshow("Imagen", imagen)

# esperar a pulsar tecla para terminar
cv2.waitKey(-1)
