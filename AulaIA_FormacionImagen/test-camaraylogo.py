import cv2

# conectar con la cámara
camara = cv2.VideoCapture(0)

# Imagen a mostrar con canal de transparencia
nombre_imagen = '../AulaIA_imagenes/ULPGC.png'

# lectura de la imagen desde disco con e matiz de no eliminar el canal alpha de transparencias
logo = cv2.imread(nombre_imagen, cv2.IMREAD_UNCHANGED)

# comprobar si la imagen se ha leído bien
if logo is None:
    print('Error leyendo imagen !!!!')
    exit(0)

# Dimensiones imagen del logo
alto2, ancho2, componentes2 = logo.shape

# comprobar que la cámara se ha conectado correctamente
if not camara.isOpened():
    print('Error abriendo cámara !!!')
    exit(0)

# realizar captura continua hasta pulsar la tecla 'q'
while (True):
    # Captura fotograma
    res, fotograma = camara.read()

    # dimensiones imagen cámara
    alto, ancho, componentes = fotograma.shape

    # Define coordenada de la esquina superior izquierda donde copiar el logo
    px = 0
    py = 0
    # Zona a copiar en imagen de fondo
    roi = fotograma[py:py + alto2, px: px + ancho2]

    # Separa canales y se queda con el canal de transparencia como máscara
    B, G, R, mask = cv2.split(logo)
    mask_inv = cv2.bitwise_not(mask)

    # Enmascara el fondo
    imagen_fondo = cv2.bitwise_and(roi, roi, mask=mask_inv)

    # Toma sólo la zona de la figura
    imagen2_logo = cv2.bitwise_and(logo, logo, mask=mask)

    # Combina logo con fondo
    dst = cv2.add(imagen_fondo[:, :, 0:3], imagen2_logo[:, :, 0:3])
    fotograma[py: py + alto2, px: px + ancho2] = dst[:, :, 0:3]

    # Muestra imagen
    cv2.imshow('Fotograma', fotograma)

    # Finaliza pulsando q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cierra la cámara y la ventana al terminar
camara.release()
cv2.destroyAllWindows()
