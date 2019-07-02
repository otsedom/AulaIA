import cv2

# nombre de la imagen a mostrar
nombreImagen = '../AulaIA_imagenes/indurain.jpg'

# lectura de la imagen desde disco
imagen = cv2.imread(nombreImagen)

# comprobar si la imagen se ha leído bien
if imagen is None:
    print('Error leyendo imagen !!!!')
    exit(0)

alto, ancho, componentes = imagen.shape

print('Alto de la imagen: {}'.format(alto))
print('Ancho de la imagen: {}'.format(ancho))
print('Número componentes: {}'.format(componentes))

# mostrar la imagen en pantalla
cv2.imshow('imagen orginal', imagen)
cv2.waitKey(1)

# reduce la dimensión
factorReduccion = 64
nuevoAncho = (int)(ancho / factorReduccion)
nuevoAlto = (int)(alto / factorReduccion)
imagenReducida = cv2.resize(imagen, (nuevoAncho, nuevoAlto), interpolation=cv2.INTER_LINEAR)

# Initialize output image
imagenPixelada = cv2.resize(imagenReducida, (ancho, alto), interpolation=cv2.INTER_NEAREST)

# mostrar la imagen pixelada
cv2.imshow('imagen pixelada', imagenPixelada)
cv2.waitKey(1)

# esperar a pulsar tecla para terminar
cv2.waitKey(-1)



