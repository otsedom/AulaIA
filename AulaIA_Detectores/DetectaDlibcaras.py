import cv2

from imutils import face_utils
import dlib
import cv2

# Adaptado de https://github.com/italojs/facial-landmarks-recognition-/blob/master/shape_predictor_68_face_landmarks.dat

# Detector de caras de dlib basado en HOG+SVM
detector = dlib.get_frontal_face_detector()
# Modelo detector de marcas faciales
p = "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(p)

# Captura de la cámara
cap = cv2.VideoCapture(0)

while (True):
    # Captura fotograma de la cámara
    ret, img = cap.read()

    # Conversión a grises
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecta objetos
    caras = detector(gris, 0)

    # Para cada cara detectada
    for (i, rect) in enumerate(caras):
        # Predice marcas faciales
        mascara = predictor(gris, rect)
        mascara = face_utils.shape_to_np(mascara)

        # Dibuja los puntos de la máscara
        for (x, y) in mascara:
            cv2.circle(img, (x, y), 2, (0, 255, 0), -1)

    # Show detections
    print("Localizadas {0} caras".format(len(caras)))

    # Muestra imagen
    cv2.imshow('Detectando caras', img)
    # Finaliza pulsando q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera al detener
cap.release()
cv2.destroyAllWindows()