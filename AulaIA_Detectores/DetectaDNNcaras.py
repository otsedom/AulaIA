import cv2

# Carga red para detección
faceProto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"
faceNet = cv2.dnn.readNet(faceModel, faceProto)
conf_threshold = 0.7

# Captura de la webcam
cap = cv2.VideoCapture(0)

while (True):
    # Captura fotograma
    ret, frame = cap.read()

    # Convierte a grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta objetos
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), [104, 117, 123], True, False)

    faceNet.setInput(blob)
    detections = faceNet.forward()
    faces = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            faces.append([x1, y1, x2 - x1, y2 - y1])
            # faces.append([x1, y1, x2, y2])
            # Dibuja contenedor
            # cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight / 150)), 8)

    # Show detections
    print("Localizados {0}!".format(len(faces)))

    # Para cada cara detectada
    for (x, y, w, h) in faces:
        # Dibuj contenedor
        container = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Muestra imagen en grises
    cv2.imshow('Detectando caras', frame)
    # Finaliza pulsando q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera al detener
cap.release()
cv2.destroyAllWindows()