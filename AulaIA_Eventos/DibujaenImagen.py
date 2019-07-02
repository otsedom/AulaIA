import cv2
import numpy as np
import random

def raton_clic(evento, x, y, flags, params):
    if evento == cv2.EVENT_LBUTTONDOWN:
        print("Botón izquierdo")
        cv2.circle(imagen, (x, y), 20, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), cv2.FILLED)
        cv2.imshow("Imagen", imagen)


# Crea imagen negra
imagen = np.zeros((500,500,3),np.uint8)

# Ventana visualización y eventos
cv2.namedWindow("Imagen")
cv2.setMouseCallback("Imagen", raton_clic)

# Muestra imagen de partida
cv2.imshow("Imagen", imagen)

# Mientras no cortemos ejecución
while True:
    # Espera evento de teclado
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()


