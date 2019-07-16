import cv2
import numpy as np

pulsado = False
pulsadounavez = False
dife = 20

def raton(evento, x, y, flags, params):
    global pulsado,pulsadounavez,cx,cy,hmin,hmax,smin,smax
    if evento == cv2.EVENT_LBUTTONDOWN:
        print("Botón izquierdo")
        pulsado = True
        pulsadounavez = True
        cx = x
        cy = y
        # Define color a buscar
        hmin = imghsv[cy, cx, 0] - dife
        hmax = imghsv[cy, cx, 0] + dife
        smin = imghsv[cy, cx, 1] - dife
        smax = imghsv[cy, cx, 1] + dife
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

    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    if pulsadounavez == True:
        # Prueba color piel
        numFilas, numColumnas, numColores = imghsv.shape

        imgpiel = np.zeros((numFilas, numColumnas), dtype=np.uint8)
        pospiel = (hmin <= imghsv[:, :, 0]) & (imghsv[:, :, 0] <= hmax) & (smin <= imghsv[:, :, 1]) & (
                    imghsv[:, :, 1] <= smax) 
        imgpiel[pospiel] = 255
        cv2.imshow('Imagen piel', imgpiel)
        # fin prueba

    # Muestra imagen en grises
    cv2.imshow('Imagen',img)



	# Finaliza pulsando q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera al detener
cap.release()
cv2.destroyAllWindows()