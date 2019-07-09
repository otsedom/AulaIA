import cv2
import numpy as np
import random
npuntos = 0

def raton_clic(evento, x, y, flags, params):
    global npuntos, px, py
    if evento == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen, (x, y), 5, (255,255,255), cv2.FILLED)
        npuntos = npuntos + 1
        if npuntos == 2:
            cv2.rectangle(imagen, (px, py), (x, y), (255, 255, 255), 3)
            text_file = open("Recuadro.txt", "w")
            text_file.write("%d %d %d %d" % (px,py,x,y) )
            text_file.close()
        elif npuntos == 1:
            px = x
            py = y

        cv2.imshow("Imagen", imagen)


# Crea imagen negra
imagen = np.zeros((500,500,3),np.uint8)

# Ventana visualización y eventos
cv2.namedWindow("Imagen")
cv2.setMouseCallback("Imagen", raton_clic)

# Muestra imagen de partida
cv2.imshow("Imagen", imagen)

# Mientras no cortemos ejecución
while npuntos<2:
    # Espera evento de teclado
    key = cv2.waitKey(1)
    if key == 27:
        break

# Espera pulsado de tecla
cv2.waitKey(0)
cv2.destroyAllWindows()


