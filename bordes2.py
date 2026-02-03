import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Cargar imagen
ruta = "C:/Users/Marce/Documents/SenalesImagenes/Tarea1/foto_capturada.jpg"
img_bgr = cv2.imread(ruta)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# 2. Convertir a escala de grises
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# 3. Suavizado para eliminar ruido y detalles internos
img_blur = cv2.GaussianBlur(img_gray, (1, 3), 0)

# 4. Detector de bordes Canny (el más limpio y preciso)
edges = cv2.Canny(img_blur, 80, 160)

# 5. Morfología para cerrar huecos y unir líneas
kernel = np.ones((3, 3), np.uint8)
edges_clean = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

# 6. Mostrar resultados
fig, axs = plt.subplots(1, 4, figsize=(20, 6))

axs[0].imshow(img_rgb)
axs[0].set_title("Original")
axs[0].axis("off")

axs[1].imshow(img_gray, cmap="gray")
axs[1].set_title("Escala de grises")
axs[1].axis("off")

axs[2].imshow(img_blur, cmap="gray")
axs[2].set_title("Suavizado (GaussianBlur)")
axs[2].axis("off")

axs[3].imshow(edges, cmap="gray")
axs[3].set_title("Bordes limpios (Canny + Morph)")
axs[3].axis("off")

plt.tight_layout()
plt.show()
