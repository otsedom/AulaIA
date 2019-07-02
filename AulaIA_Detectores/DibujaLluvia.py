import cv2
import numpy as np
import random

# Crea gotas con posición en x y velocidad aleatoria
gotas = []
vel = []
for i in range(15):
    # Obtengo posición y velocidad de las gotas de lluvia
    gotas.append( (random.randint(0, 500),0) )
    vel.append(random.randint(1, 10))

# Mientras no cortemos ejecución
while True:
    # Imagen negra
    imagen = np.zeros((500, 500, 3), np.uint8)

    # Dibuja gotas
    for i in range(len(gotas)):
        x = gotas[i][0]
        y = gotas[i][1]
        imagen = cv2.line(imagen, (x, y), (x, y + 2), (0, 255, 0), 2)
        gotas.pop(i)
        y = y + vel[i]
        if y > 500:
            gotas.append((random.randint(0, 500), 0))
            vel.pop(i)
            vel.append(random.randint(1, 10))
        else:
            gotas.append((x,y))

    # Muestra imagen de partida
    cv2.imshow("Imagen", imagen)

    # Espera evento de teclado
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()


