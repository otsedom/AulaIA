import cv2
import numpy as np

# conectar con la cámara
camara = cv2.VideoCapture(0)

# comprobar que la cámara se ha conectado correctamente
if not camara.isOpened():
    print('Error abriendo cámara !!!')
    exit(0)

# Captura primer fotograma y lo convierte a grises
ret, fotogramaAnterior = camara.read()
fotogramaAnteriorGrises = cv2.cvtColor(fotogramaAnterior, cv2.COLOR_BGR2GRAY)

# realizar captura continua hasta pulsar la tecla 'q'
while True:
    # Captura fotograma y convierte a grises
    res, fotogramaActual = camara.read()
    fotogramaActualGrises = cv2.cvtColor(fotogramaActual, cv2.COLOR_BGR2GRAY)

    # Calcula la diferencia y actualiza el fotograma anterior como e actual
    imagenDiferencia = cv2.absdiff(fotogramaAnteriorGrises, fotogramaActualGrises)
    fotogramaAnteriorGrises = np.copy(fotogramaActualGrises)
    res, imagenDiferencia = cv2.threshold(imagenDiferencia, 30, 255, cv2.THRESH_BINARY)

    # Muestra imagen de grises y diferencia
    cv2.imshow('Diferencias', imagenDiferencia)
    cv2.imshow('Imagen', fotogramaActualGrises)

    # Finaliza pulsando q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cierra la cámara y la ventana al terminar
camara.release()
cv2.destroyAllWindows()



