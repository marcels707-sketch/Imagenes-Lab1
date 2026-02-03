from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

imagen = "C:/Users/Marce/Documents/SenalesImagenes/Tarea1/foto_capturada.jpg"

# 1. Cargar la imagen
img = Image.open(imagen)

# 2. Enfoque inicial (Sharpen)
img_enfoque = img.filter(ImageFilter.SHARPEN)

# 3. Detección de bordes (FIND_EDGES)
img_bordes = img_enfoque.filter(ImageFilter.FIND_EDGES)

# 4. Suavizado para reducir ruido
img_gauss = img_bordes.filter(ImageFilter.GaussianBlur(radius=1))

# 5. Segundo enfoque
img_enfoque_final = img_bordes.filter(ImageFilter.SHARPEN)

# 6. Segunda detección de bordes
img_bordes_final = img_enfoque_final.filter(ImageFilter.FIND_EDGES)

# 7. Limpieza final (suavizado)
img_limpia = img_bordes_final.filter(ImageFilter.GaussianBlur(radius=1))

# Mostrar resultados en 2 filas × 3 columnas
fig, axs = plt.subplots(2, 3, figsize=(20, 5))

# Primera fila
axs[0, 0].imshow(img_enfoque)
axs[0, 0].set_title("Sharpen inicial")
axs[0, 0].axis("off")

axs[0, 1].imshow(img_bordes)
axs[0, 1].set_title("Edges 1")
axs[0, 1].axis("off")

axs[0, 2].imshow(img_gauss)
axs[0, 2].set_title("Suavizado (Gauss)")
axs[0, 2].axis("off")

# Segunda fila
axs[1, 0].imshow(img_enfoque_final)
axs[1, 0].set_title("Sharpen final")
axs[1, 0].axis("off")

axs[1, 1].imshow(img_bordes_final)
axs[1, 1].set_title("Edges 2")
axs[1, 1].axis("off")

axs[1, 2].imshow(img_limpia)
axs[1, 2].set_title("Suavizado (Gauss) final")
axs[1, 2].axis("off")

plt.tight_layout()
plt.show()