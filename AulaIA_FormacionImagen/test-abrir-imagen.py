import cv2

# nombre de la imagen a mostrar
nombre_imagen = '../AulaIA_imagenes/indurain.jpg'

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

# mostrar la imagen en pantalla
cv2.imshow('imagen original', imagen)

# convertir la imagen de BGR a RGB
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
cv2.imshow('imagen rgb', imagen_rgb)

# convertir la imagen de RGB a niveles de grises
imagen_grises = cv2.cvtColor(imagen_rgb, cv2.COLOR_RGB2GRAY)
cv2.imshow('imagen grises', imagen_grises)

# esperar a pulsar tecla para terminar
cv2.waitKey(-1)