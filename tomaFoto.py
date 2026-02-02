import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Inicializar la cámara
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # CAP_DSHOW evita warnings en Windows

if not cap.isOpened():
    print("Error: No se pudo acceder a la cámara.")
else:
    print("Cámara abierta. Presiona 's' para guardar una foto o 'q' para salir.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error al capturar el video.")
            break

        cv2.imshow('Presiona S para tomar foto', frame)

        key = cv2.waitKey(1)

        if key == ord('s'):
            nombre_foto = "foto_capturada2.jpg"
            cv2.imwrite(nombre_foto, frame)
            print(f"¡Foto guardada como {nombre_foto}!")
            break

        elif key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()


ruta_archivo = "foto_capturada2.jpg"

img_bgr = cv2.imread(ruta_archivo)

if img_bgr is None:
    print(f"Error: No se encontró la imagen en {ruta_archivo}")
else:
    alto, ancho, canales = img_bgr.shape
    print(f"Dimensiones: {ancho}px (ancho) x {alto}px (alto) | Canales: {canales} | dtype: {img_bgr.dtype}")

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    img_recortada = img_rgb[172:206, 283:480]

    centro = (ancho // 2, alto // 2)
    M = cv2.getRotationMatrix2D(centro, 180, 1.0)  # 180° sin zoom
    img_rotada_180 = cv2.warpAffine(img_rgb, M, (ancho, alto))

    img_reflejada = cv2.flip(img_rgb, 1)

    kernel_sharpen = np.array([[-1, -1, -1], 
                               [-1,  9, -1], 
                               [-1, -1, -1]])
    img_enfoque = cv2.filter2D(img_rgb, -1, kernel_sharpen)

    fig, axs = plt.subplots(1, 5, figsize=(20, 5))

    axs[0].imshow(img_rgb); axs[0].set_title("Original")
    axs[1].imshow(img_recortada); axs[1].set_title("Recortada [172:206, 283:480]")
    axs[2].imshow(img_rotada_180); axs[2].set_title("Rotacion 180")
    axs[3].imshow(img_reflejada); axs[3].set_title("Reflejado")
    axs[4].imshow(img_enfoque); axs[4].set_title("Enfoque")

    for ax in axs: ax.axis('off')

    #Información de la fotografía incluida en la pantalla
    plt.subplots_adjust(bottom=0.10)
    plt.figtext(
    0.5, 0.06,
    f"Dimensiones: {ancho}px x {alto}px \n"+f"Canales de color: {canales}",
    ha="center", fontsize=10,
    )
    
    plt.tight_layout()
    plt.show()
