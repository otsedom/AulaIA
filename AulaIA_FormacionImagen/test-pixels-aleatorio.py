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


def pintaMarciano(xIni, yIni, color):

    for x in range(xIni+10, xIni + 90):
        for y in range(yIni-20, yIni):
            imagen[y, x, 0] = color[0]
            imagen[y, x, 1] = color[1]
            imagen[y, x, 2] = color[2]

    for x in range(xIni, xIni + 100):
        for y in range(yIni, yIni + 100):
            imagen[y, x, 0] = color[0]
            imagen[y, x, 1] = color[1]
            imagen[y, x, 2] = color[2]

    for x in range(xIni + 10, xIni + 30):
        for y in range(yIni + 20, yIni + 40):
            imagen[y, x, 0] = 255
            imagen[y, x, 1] = 255
            imagen[y, x, 2] = 255

    for x in range(xIni + 70, xIni + 90):
        for y in range(yIni + 20, yIni + 40):
            imagen[y, x, 0] = 255
            imagen[y, x, 1] = 255
            imagen[y, x, 2] = 255

    for x in range(xIni + 30, xIni + 70):
        for y in range(yIni + 60, yIni + 80):
            imagen[y, x, 0] = 255
            imagen[y, x, 1] = 255
            imagen[y, x, 2] = 255

imagenOriginal = np.copy(imagen)
while True:
    imagen = np.copy(imagenOriginal)

    xInicial = np.random.randint(20, 790)
    yInicial = np.random.randint(20, 490)
    r = np.random.randint(0, 256)
    g = np.random.randint(0, 256)
    b = np.random.randint(0, 256)

    pintaMarciano(xInicial, yInicial, (r, g, b))
    cv2.imshow('Imagen', imagen)

    tecla = cv2.waitKey(500)
    if tecla == 0xFF & ord('q'):
        break

