import cv2

# Carga del clasificador para detección
cascada_caras = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
cascada_ojos = cv2.CascadeClassifier('./haarcascade_mcs_lefteye.xml')

# Captura de la cámara
cap = cv2.VideoCapture(0)

while (True):
    # Captura fotograma de la cámara
    ret, img = cap.read()

    # Conversión a grises
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecta caras
    caras = cascada_caras.detectMultiScale(gris)

    # Show detections
    print("Localizada(s) {0} cara(s)".format(len(caras)))

    # Para cada cara detectada
    for (x, y, w, h) in caras:

        # Define zona para buscar los ojos
        roi_gris = gris[y + (int)(h * 0.2):y + (int)(h * 0.6), x:x + w]
        # Busca ojos y dibuja el contenedor
        ojos = cascada_ojos.detectMultiScale(roi_gris)
        for (ox, oy, ow, oh) in ojos:
            # Con este clasificador ow y oh parecen estar al revés
            cv2.rectangle(img, (x + ox, y + (int)(h * 0.2) + oy), (x + ox + oh, y + (int)(h * 0.2) + oy + ow),
                          (0, 255, 0), 2)

        # Dibuja contenedor cara
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Muestra imagen
    cv2.imshow('Detectando caras y ojos', img)
    # Finaliza pulsando q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera al detener
cap.release()
cv2.destroyAllWindows()