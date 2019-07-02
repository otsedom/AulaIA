import cv2

# conectar con la cámara
camara = cv2.VideoCapture(0)

# comprobar que la cámara se ha conectado correctamente
if not camara.isOpened():
    print('Error abriendo cámara !!!')
    exit(0)

# realizar captura continua hasta pulsar la tecla 'q'
while (True):
    # Captura fotograma
    res, fotograma = camara.read()

    # Muestra imagen en grises
    cv2.imshow('Fotograma', fotograma)

    # Finaliza pulsando q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cierra la cámara y la ventana al terminar
camara.release()
cv2.destroyAllWindows()
