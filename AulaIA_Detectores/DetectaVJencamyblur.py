import cv2

# Carga del clasificador para detección
cascada_caras = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')

# Captura de la cámara
cap = cv2.VideoCapture(0)

while (True):
    # Captura fotograma de la cámara
    ret, img = cap.read()

    # Conversión a grises
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecta objetos
    caras = cascada_caras.detectMultiScale(gris)

    # Show detections
    print("Localizadas {0} caras".format(len(caras)))

    # Para cada cara detectada
    for (x, y, w, h) in caras:
        img[y:y + h, x:x + w] = cv2.blur(img[y:y + h, x:x + w], (23, 23))
        # Dibuja contenedor
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Muestra imagen
    cv2.imshow('Detectando caras', img)
    # Finaliza pulsando q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera al detener
cap.release()
cv2.destroyAllWindows()