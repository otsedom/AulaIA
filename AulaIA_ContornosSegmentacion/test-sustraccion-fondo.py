import cv2

# conectar con la cámara
camara = cv2.VideoCapture(0)

# comprobar que la cámara se ha conectado correctamente
if not camara.isOpened():
    print('Error abriendo cámara !!!')
    exit(0)

# Toma primer fotograma como fondo
for i in range(0,25):
    res, fondo = camara.read()
    cv2.waitKey(20)

fondoGris = cv2.cvtColor(fondo, cv2.COLOR_BGR2GRAY)

# Elimina detalle con filtro gausiano
fondoGris = cv2.GaussianBlur(fondoGris, (5, 5), 0)

# realizar captura continua hasta pulsar la tecla 'q'
while True:
    # Captura fotograma
    res, img = camara.read()

    # Conversión a grises
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Elimina detalle con filtro gausiano
    gris = cv2.GaussianBlur(gris, (5, 5), 0)

    # Calcula la diferencia del fotograma con el fondo
    diferencia = cv2.absdiff(fondoGris, gris)
    res, diferencia = cv2.threshold(diferencia, 25, 255, cv2.THRESH_BINARY)

    # Muestra imagen en grises
    cv2.imshow('Fotograma gris', gris)
    cv2.imshow("Fondo", fondoGris)
    cv2.imshow("Diferencia", diferencia)

    # Finaliza pulsando q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera al detener
camara.release()
cv2.destroyAllWindows()
