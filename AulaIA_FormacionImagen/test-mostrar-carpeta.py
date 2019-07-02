import glob, os
import cv2

# carpeta y patrón de las imágenes a mostrar
ruta = '../AulaIA_imagenes/*.jpg'

# obtener los nombres de las imágenes de la carpeta especificada
nombreImagenes = glob.glob(ruta)
print('Imágenes a mostrar: {}'.format(nombreImagenes))

# mostrar las imágenes de la carpeta
for unNombre in nombreImagenes:
    # Cargamos la imagen del disco duro
    imagen = cv2.imread(unNombre)

    # comprobar si la imagen se ha leído bien
    if imagen is None:
        print('Error leyendo imagen !!!!')
        exit(0)

    # mostrar la imagen en pantalla y esperar a pulsar una tecla
    cv2.imshow('imagen orginal', imagen)
    cv2.waitKey(-1)

