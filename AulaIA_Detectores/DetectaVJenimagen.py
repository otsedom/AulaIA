import cv2

# Carga del clasificador para detección
cascada = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')

# Cargamos la imagen del disco
imagen = cv2.imread("worlds-largest-selfie.jpg")

# Conversión a grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detecta objetos
caras = cascada.detectMultiScale(gris)

# Show detections
print("{0} detecciones".format(len(caras)))

# Para cada cara detectada
for (x, y, w, h) in caras:
    # Dibuja contenedor
    imagen = cv2.rectangle(imagen, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Imagen", imagen)

cv2.waitKey(0)
