import cv2
import time

# Adaptado de https://www.learnopencv.com/age-gender-classification-using-opencv-deep-learning-c-python/

# Carga clasificador Viola Jones
cascada_caras = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')

# Edad y sexo
ageProto = "age_deploy.prototxt"
ageModel = "age_net.caffemodel"

genderProto = "gender_deploy.prototxt"
genderModel = "gender_net.caffemodel"

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList = ['Masculino', 'Femenino']

ageNet = cv2.dnn.readNet(ageModel, ageProto)
genderNet = cv2.dnn.readNet(genderModel, genderProto)
padding = 20

# Activa la webcam
cap = cv2.VideoCapture(0)

while (True):
    # Captura fotograma
    t = time.time()
    ret, frame = cap.read()

    # Convierte a grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta objetos
    faces = cascada_caras.detectMultiScale(gray)

    # Show detections
    print("Localizados {0}!".format(len(faces)))

    # Para cada cara detectada
    for (x, y, w, h) in faces:
        # Dibuja contenedor
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Para cada cara detectada
    for (x, y, w, h) in faces:
        # Dibuja contenedor
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Procesamiento edad y sexo
    for (x, y, w, h) in faces:
        # Agranda la detección
        face = frame[max(0, y - padding):min(y + h + padding, frame.shape[0] - 1),
               max(0, x - padding):min(x + w + padding, frame.shape[1] - 1)]

        # Procesa
        blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
        genderNet.setInput(blob)
        genderPreds = genderNet.forward()
        gender = genderList[genderPreds[0].argmax()]
        # print("Gender : {}, conf = {:.3f}".format(gender, genderPreds[0].max()))

        ageNet.setInput(blob)
        agePreds = ageNet.forward()
        age = ageList[agePreds[0].argmax()]
        # print("Age Output : {}".format(agePreds))
        # print("Age : {}, conf = {:.3f}".format(age, agePreds[0].max()))

        label = "{},{}".format(gender, age)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2,
                    cv2.LINE_AA)

    print("tiempo de procesamiento : {:.3f}".format(time.time() - t))

    # Muestra imagen en grises
    cv2.imshow('Edad y sexo', frame)
    # Finaliza pulsando q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera al detener
cap.release()
cv2.destroyAllWindows()