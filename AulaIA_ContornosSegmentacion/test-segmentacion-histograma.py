import cv2
import matplotlib.pyplot as plt

# nombre de la imagen
nombreImagen = '../AulaIA_imagenes/indurain.jpg'

# lectura de la imagen desde disco
imagen = cv2.imread(nombreImagen)

# comprobar si la imagen se ha leído bien
if imagen is None:
    print('Error leyendo imagen !!!!')
    exit(0)

# convertir la imagen a niveles de grises y mostrar
imagenGrises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagen', imagenGrises)
cv2.waitKey(10)

# obtener el histograma
tamHistograma = 256
limitesHistograma = (0, 256)  # límites de los valores del histograma
histogramaGrises = cv2.calcHist(imagenGrises, [0], None, [tamHistograma], limitesHistograma)

# mostrar el histograma
fig = plt.figure()
plt.hist(imagenGrises.reshape(-1), bins=tamHistograma)
plt.xlabel('Nivel de gris')

# umbralizar imagen
valorUmbral = 127
res, imagenUmbralizada = cv2.threshold(imagenGrises, valorUmbral, 255, cv2.THRESH_BINARY)

# mostrar imagen umbralizada
cv2.imshow('imagen umbralizada', imagenUmbralizada)
cv2.waitKey(10)

# esperar a pulsar tecla para cerrar todas las ventanas antes de terminar script
cv2.waitKey(0)
cv2.destroyAllWindows()