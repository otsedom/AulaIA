import cv2

pulsado = False

def raton(evento, x, y, flags, params):
    global pulsado,cx,cy
    if evento == cv2.EVENT_LBUTTONDOWN:
        print("Botón izquierdo")
        pulsado = True
        cx = x
        cy = y
    elif evento == cv2.EVENT_MOUSEMOVE:
        if pulsado == True:
            cx = x
            cy = y
    elif evento == cv2.EVENT_LBUTTONUP:
        pulsado = False

cap = cv2.VideoCapture(0)

# Ventana visualización y eventos
cv2.namedWindow("Imagen")
cv2.setMouseCallback("Imagen", raton)

while(True):
    # Captura fotograma
    ret, img = cap.read()

    imghsv=

    # Pinta si el ratón está pulsado
    if pulsado == True:
        cv2.rectangle(img, (cx - 10, cy - 10), (cx + 10, cy + 10), (128, 128, 128), cv2.FILLED)

    # Muestra imagen en grises
    cv2.imshow('Imagen',img)
	# Finaliza pulsando q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera al detener
cap.release()
cv2.destroyAllWindows()