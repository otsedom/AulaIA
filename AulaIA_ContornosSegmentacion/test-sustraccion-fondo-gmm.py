import cv2

# conectar con la cámara
camara = cv2.VideoCapture(0)

# comprobar que la cámara se ha conectado correctamente
if not camara.isOpened():
    print('Error abriendo cámara !!!')
    exit(0)

# Inicializa la sustracción del fondo con mezcla de gausianas y detección de sombras
eliminadorFondo = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

# realizar captura continua hasta pulsar la tecla 'q'
while True:
    # Captura fotograma
    res, img = camara.read()

    # Aplica sustracción
    objetosMovimiento = eliminadorFondo.apply(img)

    # Muestra imagen en grises
    cv2.imshow('Fotograma', img)
    cv2.imshow('Deteccion', objetosMovimiento)

    # Finaliza pulsando q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera al detener
camara.release()
cv2.destroyAllWindows()
