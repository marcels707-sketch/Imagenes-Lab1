import cv2
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


#----------------------------------------
# Función para mostrar operaciones
#----------------------------------------
def operacionesImagenes (img_bgr):
    while True:
            print("--------------------------------")
            print("Ingrese las siguientes opciones:")
            print("--------------------------------")
            print("Operaciones Geométricas---------")
            print("1 para Escalado")
            print("2 para Rotación")
            print("3 para Recorte")
            print("4 para Reflejo")
            print("Operaciones de punto------------")
            print("5 para Brillo")
            print("6 para Contraste")
            print("7 para Umbral")
            print("Operaciones de vecindad---------")
            print("8 para Suavizado (Gauss)")
            print("9 para Bordes (Canny)")
            print("10 para Enfoque (Sharpen)")
            print("0 para retornar")
            print("---------------")
            

            seleccion = input("Ingrese su selección: ")

            # Opcion de escalada
            if seleccion == '1':

                while True:
                    print("--------------------------------")
                    print("Ingrese las siguientes opciones:")
                    print("--------------------------------")
                    print("1 para ejemplo escalada")
                    print("2 para ingresar tamaños")
                    print("0 para retornar")
                    print("---------------")

                    seleccion = input("Ingrese su selección: ")

                    if seleccion == '1':
                        # Tamaños deseados de escalado
                        tamanos = [100, 150, 200, 250, 300]
                    elif seleccion == '2':
                        entrada = input("Ingrese los valores a escalar separados por comas: ")
                        try:
                            tamanos = [int(x.strip()) for x in entrada.split(',')]
                        except ValueError:
                            print("Error: ingrese solo números separados por comas.")
                            continue
                    else:
                        break

                    # Crear figura
                    fig, axs = plt.subplots(1, len(tamanos), figsize=(15, 5))
                    # Se realiza una adaptación para el ingreso de un solo item
                    if len(tamanos) == 1:
                        axs = [axs]
                    # Generar imágenes escaladas en un bucle
                    for ax, t in zip(axs, tamanos):
                        # Escalado de acuerdo a los tamaños
                        img_recortada = cv2.resize(img_bgr, (t, t))
                        ax.imshow(img_recortada)
                        ax.set_title(f"Escalado ({t}x{t})")
                        ax.axis("off")

                    plt.tight_layout()
                    plt.show()

                    if seleccion != '1':
                        break
            
            # Opcion de rotacion
            if seleccion == '2':

                while True:
                    print("--------------------------------")
                    print("Ingrese las siguientes opciones:")
                    print("--------------------------------")
                    print("1 para ejemplo rotacion")
                    print("2 para ingresar los valores de los angulos")
                    print("0 para retornar")
                    print("---------------")

                    seleccion = input("Ingrese su selección: ")

                    if seleccion == '1':
                        # Angulos de rotacion
                        angulo = [25, 50, 75, 100, 125]
                    elif seleccion == '2':
                        entrada = input("Ingrese los valores de los ángulos por comas: ")
                        try:
                            angulo = [int(x.strip()) for x in entrada.split(',')]
                        except ValueError:
                            print("Error: ingrese solo números separados por comas.")
                            continue
                    else:
                        break
                    
                    # Obtener información (alto, ancho, canales)
                    alto, ancho, canales = img_bgr.shape
                    # centro de la imagen
                    centro = (ancho // 2, alto // 2)
                    # Crear figura
                    fig, axs = plt.subplots(1, len(angulo), figsize=(20, 5))
                    # Se realiza una adaptación para el ingreso de un solo item
                    if len(angulo) == 1:
                        axs = [axs]
                    # Generar imágenes rotadas en un bucle
                    for ax, t in zip(axs, angulo):
                        # matriz de transformacion
                        matriz = cv2.getRotationMatrix2D(centro, t, 1.0)
                        # Rotacion de la imagen de acuerdo a los valores de los angulos
                        img_rotada = cv2.warpAffine(img_bgr, matriz, (ancho, alto))
                        ax.imshow(img_rotada)
                        ax.set_title(f"Rotacion ({t})")
                        ax.axis("off")

                    plt.tight_layout()
                    plt.show()

                    if seleccion != '1':
                        break

            # Opcion de Recorte
            if seleccion == '3':

                while True:
                    print("--------------------------------")
                    print("Ingrese las siguientes opciones:")
                    print("--------------------------------")
                    print("1 para ejemplo recorte")
                    print("2 para ingresar los valores para recortar 'alto,ancho'")
                    print("0 para retornar")
                    print("---------------")

                    seleccion = input("Ingrese su selección: ")

                    if seleccion == '1':
                        # Tamaños deseados de escalado
                        rangos = [slice(100, 200),slice(300, 400)]
                    elif seleccion == '2':
                        entrada = input("Ingrese los valores alto:ancho, alto:ancho ")
                        try:
                            # Separar por comas → ["a:b", "c:d", "e:f"]
                            partes = [p.strip() for p in entrada.split(',')]

                            # Convertir cada parte en un slice
                            rangos = []
                            for p in partes:
                                ini, fin = p.split(':')
                                rangos.append(slice(int(ini), int(fin)))

                            print("Rangos interpretados:", rangos)

                        except Exception:
                            print("Error: formato incorrecto. Ejemplo válido: 100:400, 50:200")
                            continue
                    else:
                        break
                    
                    # Crear figura
                    fig, axs = plt.subplots(1, len(rangos)+1, figsize=(20, 5))

                    print(rangos)

                    # Se realiza una adaptación para el ingreso de un solo item
                    if not isinstance(axs, (list, np.ndarray)):
                        axs = [axs]
                   # Mostrar primero la imagen original
                    axs[0].imshow(img_bgr)
                    axs[0].set_title("Original")
                    axs[0].grid(True, color='red', linestyle='-',linewidth=0.5)

                    # Mostrar los recortes a partir del subplot 1
                    for i, t in enumerate(rangos, start=1):
                        img_recortada = img_bgr[t, 400:600]
                        axs[i].imshow(img_recortada)
                        axs[i].set_title(f"Recorte [{t.start}:{t.stop}]"+",[400:600]")
                        axs[i].axis("off")

                    plt.tight_layout()
                    plt.show()

                    if seleccion != '1':
                        break            
            
            # Opcion de Reflejo
            if seleccion == '4':

                while True:
                    print("--------------------------------")
                    print("Ingrese las siguientes opciones:")
                    print("--------------------------------")
                    print("1 para ejemplo reflejo")
                    print("2 para el tipo de reflejo")
                    print("0 para retornar")
                    print("---------------")

                    seleccion = input("Ingrese su selección: ")

                    if seleccion == '1':
                        # Tamaños deseados de reflejo
                        rangos = [1,0,-1]
                    elif seleccion == '2':
                        entrada = input("Ingrese los valores de reflejo ")
                        if entrada in ('1', '0', '-1'):
                            rangos = [int(entrada)]
                        else:
                            print ("Error: valor ingresado incorrecto")
                            continue
                    else:
                        break
                    
                    # Crear figura
                    fig, axs = plt.subplots(1, len(rangos)+1, figsize=(20, 5))

                    # Se realiza una adaptación para el ingreso de un solo item
                    if not isinstance(axs, (list, np.ndarray)):
                        axs = [axs]
                    
                    # Mostrar primero la imagen original
                    axs[0].imshow(img_bgr)
                    axs[0].set_title("Original")
                    axs[0].axis("off")

                    # Mostrar los recortes a partir del subplot 1
                    for i, t in enumerate(rangos, start=1):
                        img_reflejada=cv2.flip(img_bgr, t)
                        axs[i].imshow(img_reflejada)
                        axs[i].set_title(f"Reflejo {t}")
                        axs[i].axis("off")

                    plt.tight_layout()
                    plt.show()

                    if len(rangos) != 3:
                        break
            
            # Opcion de Brillo
            if seleccion == '5':

                while True:
                    print("--------------------------------")
                    print("Ingrese las siguientes opciones:")
                    print("--------------------------------")
                    print("1 para ejemplo brillo")
                    print("2 para ingresar un valor personalizado")
                    print("0 para retornar")
                    print("---------------")

                    seleccion = input("Ingrese su selección: ")

                    if seleccion == '1':
                        # Tamaños deseados de brillo
                        rangos = [25,50,75]
                    elif seleccion == '2':
                        entrada = input("Ingrese un número entre 1 y 100: ")

                        try:
                            valor = int(entrada)
                            if 1 <= valor <= 100:
                                rangos=[valor]
                            else:
                                print("Error: el número debe estar entre 1 y 100")
                        except ValueError:
                            print("Error: debe ingresar un número entero")

                    else:
                        break
                    
                    # Crear figura
                    fig, axs = plt.subplots(1, len(rangos)+1, figsize=(20, 5))

                    # Se realiza una adaptación para el ingreso de un solo item
                    if not isinstance(axs, (list, np.ndarray)):
                        axs = [axs]
                    
                    # Mostrar primero la imagen original
                    axs[0].imshow(img_bgr)
                    axs[0].set_title("Original")
                    axs[0].axis("off")

                    # Mostrar los recortes a partir del subplot 1
                    for i, t in enumerate(rangos, start=1):
                        img_brillo = cv2.convertScaleAbs(img_bgr, alpha=1.0, beta=t)
                        axs[i].imshow(img_brillo)
                        axs[i].set_title(f"Brillo {t}")
                        axs[i].axis("off")

                    plt.tight_layout()
                    plt.show()

                    if len(rangos) != 3:
                        break
            
            # Opcion de Contraste
            if seleccion == '6':

                while True:
                    print("--------------------------------")
                    print("Ingrese las siguientes opciones:")
                    print("--------------------------------")
                    print("1 para ejemplo reflejo")
                    print("2 para el tipo de reflejo")
                    print("0 para retornar")
                    print("---------------")

                    seleccion = input("Ingrese su selección: ")

                    if seleccion == '1':
                        # Tamaños deseados de brillo
                        rangos = [25,50,75]
                    elif seleccion == '2':
                        entrada = input("Ingrese un número entre 1 y 100: ")

                        try:
                            valor = int(entrada)
                            if 1 <= valor <= 100:
                                rangos=[valor]
                            else:
                                print("Error: el número debe estar entre 1 y 100")
                        except ValueError:
                            print("Error: debe ingresar un número entero")

                    else:
                        break
                    
                    # Crear figura
                    fig, axs = plt.subplots(1, len(rangos)+1, figsize=(20, 5))

                    # Se realiza una adaptación para el ingreso de un solo item
                    if not isinstance(axs, (list, np.ndarray)):
                        axs = [axs]
                    
                    # Mostrar primero la imagen original
                    axs[0].imshow(img_bgr)
                    axs[0].set_title("Original")
                    axs[0].axis("off")

                    # Mostrar los recortes a partir del subplot 1
                    for i, t in enumerate(rangos, start=1):
                        img_contraste = cv2.convertScaleAbs(img_bgr, alpha=(t/100)+1, beta=0)
                        axs[i].imshow(img_contraste)
                        axs[i].set_title(f"Contraste {t}")
                        axs[i].axis("off")

                    plt.tight_layout()
                    plt.show()

                    if len(rangos) != 3:
                        break
            
            # Opcion de Contraste
            if seleccion == '6':

                while True:
                    print("--------------------------------")
                    print("Ingrese las siguientes opciones:")
                    print("--------------------------------")
                    print("1 para ejemplo reflejo")
                    print("2 para el tipo de reflejo")
                    print("0 para retornar")
                    print("---------------")

                    seleccion = input("Ingrese su selección: ")

                    if seleccion == '1':
                        # Tamaños deseados de brillo
                        rangos = [25,50,75]
                    elif seleccion == '2':
                        entrada = input("Ingrese un número entre 1 y 100: ")

                        try:
                            valor = int(entrada)
                            if 1 <= valor <= 100:
                                rangos=[valor]
                            else:
                                print("Error: el número debe estar entre 1 y 100")
                        except ValueError:
                            print("Error: debe ingresar un número entero")

                    else:
                        break
                    
                    # Crear figura
                    fig, axs = plt.subplots(1, len(rangos)+1, figsize=(20, 5))

                    # Se realiza una adaptación para el ingreso de un solo item
                    if not isinstance(axs, (list, np.ndarray)):
                        axs = [axs]
                    
                    # Mostrar primero la imagen original
                    axs[0].imshow(img_bgr)
                    axs[0].set_title("Original")
                    axs[0].axis("off")

                    # Mostrar los recortes a partir del subplot 1
                    for i, t in enumerate(rangos, start=1):
                        img_contraste = cv2.convertScaleAbs(img_bgr, alpha=(t/100)+1, beta=0)
                        axs[i].imshow(img_contraste)
                        axs[i].set_title(f"Contraste {t}")
                        axs[i].axis("off")

                    plt.tight_layout()
                    plt.show()

                    if len(rangos) != 3:
                        break
            
            # Opcion de Umbral (Thresholding)
            if seleccion == '7':

                while True:
                    print("--------------------------------")
                    print("Ingrese las siguientes opciones:")
                    print("--------------------------------")
                    print("1 para ejemplo reflejo")
                    print("2 para el tipo de reflejo")
                    print("0 para retornar")
                    print("---------------")

                    seleccion = input("Ingrese su selección: ")

                    if seleccion == '1':
                        # Tamaños deseados de brillo
                        rangos = [25,50,75]
                    elif seleccion == '2':
                        entrada = input("Ingrese un número entre 1 y 100: ")

                        try:
                            valor = int(entrada)
                            if 1 <= valor <= 100:
                                rangos=[valor]
                            else:
                                print("Error: el número debe estar entre 1 y 100")
                        except ValueError:
                            print("Error: debe ingresar un número entero")

                    else:
                        break

                    img_gris = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
                    
                    # Crear figura
                    fig, axs = plt.subplots(1, len(rangos)+1, figsize=(20, 5))

                    # Se realiza una adaptación para el ingreso de un solo item
                    if not isinstance(axs, (list, np.ndarray)):
                        axs = [axs]
                    
                    # Mostrar primero la imagen original
                    axs[0].imshow(img_bgr)
                    axs[0].set_title("Original")
                    axs[0].axis("off")

                    # Mostrar los recortes a partir del subplot 1
                    for i, t in enumerate(rangos, start=1):
                        _, img_umbral = cv2.threshold(img_gris, (t*255)/100, 255, cv2.THRESH_BINARY)
                        axs[i].imshow(img_umbral,cmap='gray')
                        axs[i].set_title(f"Umbral {t}")
                        axs[i].axis("off")

                    plt.tight_layout()
                    plt.show()

                    if len(rangos) != 3:
                        break
            
            # Opcion de Suavizado (Gauss)
            if seleccion == '8':

                while True:
                    print("--------------------------------")
                    print("Ingrese las siguientes opciones:")
                    print("--------------------------------")
                    print("1 para ejemplo suavizado")
                    print("2 para ingresar el valor del suavizado")
                    print("0 para retornar")
                    print("---------------")

                    seleccion = input("Ingrese su selección: ")

                    if seleccion == '1':
                        # Tamaños deseados de brillo
                        rangos = [3,7,11]
                    elif seleccion == '2':
                        entrada = input("Ingrese un número entre 1 y 15: ")

                        try:
                            valor = int(entrada)
                            if 1 <= valor <= 15 and valor % 2 != 0:
                                rangos=[valor]
                            else:
                                print("Error: el número debe estar entre 1 y 15")
                        except ValueError:
                            print("Error: debe ingresar un número entero impar")

                    else:
                        break

                    img_gris = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
                    
                    # Crear figura
                    fig, axs = plt.subplots(1, len(rangos)+1, figsize=(20, 5))

                    # Se realiza una adaptación para el ingreso de un solo item
                    if not isinstance(axs, (list, np.ndarray)):
                        axs = [axs]
                    
                    # Mostrar primero la imagen original
                    axs[0].imshow(img_bgr)
                    axs[0].set_title("Original")
                    axs[0].axis("off")

                    # Mostrar los recortes a partir del subplot 1
                    for i, t in enumerate(rangos, start=1):
                        img_gauss = cv2.GaussianBlur(img_bgr, (t, t), 0)
                        axs[i].imshow(img_gauss)
                        axs[i].set_title(f"Suavizado {t}")
                        axs[i].axis("off")

                    plt.tight_layout()
                    plt.show()

                    if len(rangos) != 3:
                        break    

            # Opcion de Border (Canny)
            if seleccion == '9':

                while True:
                    print("--------------------------------")
                    print("Ingrese las siguientes opciones:")
                    print("--------------------------------")
                    print("1 para ejemplo border")
                    print("2 para ingresar el valor del borde")
                    print("0 para retornar")
                    print("---------------")

                    seleccion = input("Ingrese su selección: ")

                    if seleccion == '1':
                        # Tipos de bordes
                        rangos = [50,100,150]
                        rangos2 = [150,200,250]
                    elif seleccion == '2':
                        print("1 border suaves mas detalles")
                        print("2 bordes equilibrados")
                        print("3 bordes limpios contornos fuertes")
                        entrada = input("Ingrese un número entre 1 y 3: ")

                        try:
                            valor = int(entrada)
                            if valor == 1:
                                rangos=[50]
                                rangos2=[150]
                            elif valor == 2:
                                rangos=[100]
                                rangos2=[200]
                            elif valor == 3:
                                rangos=[150]
                                rangos2=[250]
                            else:
                                print("Error: el número debe estar entre 1 y 3")
                        except ValueError:
                            print("Error: debe ingresar un número entero entre 1 y 3")

                    else:
                        break

                    img_gris = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
                    
                    # Crear figura
                    fig, axs = plt.subplots(1, len(rangos)+1, figsize=(20, 5))

                    # Se realiza una adaptación para el ingreso de un solo item
                    if not isinstance(axs, (list, np.ndarray)):
                        axs = [axs]
                    
                    # Mostrar primero la imagen original
                    axs[0].imshow(img_bgr)
                    axs[0].set_title("Original")
                    axs[0].axis("off")

                    img_gris = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

                    # Mostrar los recortes a partir del subplot 1
                    for i, (t ,l) in enumerate(zip(rangos, rangos2), start=1):
                        img_bordes = cv2.Canny(img_gris, t, l)
                        axs[i].imshow(img_bordes, cmap='gray')
                        axs[i].set_title(f"Suavizado ({t},{l})")
                        axs[i].axis("off")

                    plt.tight_layout()
                    plt.show()

                    if len(rangos) != 3:
                        break    
            
            # Opcion de Enfoque (Sharpen)
            if seleccion == '10':

                while True:
                    print("--------------------------------")
                    print("Ingrese las siguientes opciones:")
                    print("--------------------------------")
                    print("1 para ejemplo enfoque")
                    print("2 para ingresar el valor del enfoque")
                    print("0 para retornar")
                    print("---------------")

                    seleccion = input("Ingrese su selección: ")


                    if seleccion == '1':
                        kernels = {
                            "Suave": np.array([
                                [ 0, -1,  0],
                                [-1,  5, -1],
                                [ 0, -1,  0]]),
                            "Medio": np.array([
                                [-1, -1, -1],
                                [-1,  8, -1],
                                [-1, -1, -1]]),
                            "Fuerte": np.array([
                                [-1, -1, -1],
                                [-1,  9, -1],
                                [-1, -1, -1]]),
                            "Extremo": np.array([
                                [-1, -1, -1],
                                [-1, 10, -1],
                                [-1, -1, -1]])
                                }
                        
                    elif seleccion == '2':
                        print("1 kernel leve")
                        print("2 kernel equilibrado")
                        print("3 kernel fuerte")
                        print("3 kernel extremo")
                        entrada = input("Ingrese un número entre 1 y 4: ")

                        try:
                            valor = int(entrada)
                            if valor == 1:
                                 kernels = {
                                    "Suave": np.array([
                                        [ 0, -1,  0],
                                        [-1,  5, -1],
                                        [ 0, -1,  0]])
                                        }
                            elif valor == 2:
                                 kernels = {
                                    "Medio": np.array([
                                        [-1, -1, -1],
                                        [-1,  8, -1],
                                        [-1, -1, -1]])
                                        }
                            elif valor == 3:
                                 kernels = {
                                    "Fuerte": np.array([
                                        [-1, -1, -1],
                                        [-1,  9, -1],
                                        [-1, -1, -1]])
                                        }
                            elif valor == 4:
                                 kernels = {
                                    "Extremo": np.array([
                                        [-1, -1, -1],
                                        [-1, 10, -1],
                                        [-1, -1, -1]])
                                        }
                            else:
                                print("Error: el número debe estar entre 1 y 4")
                        except ValueError:
                            print("Error: debe ingresar un número entero entre 1 y 4")

                    else:
                        print("Error no se encuentra la opción ingresada")
                        break
                    
                    # Crear figura
                    fig, axs = plt.subplots(1, len(kernels)+1, figsize=(20, 5))

                    # Se realiza una adaptación para el ingreso de un solo item
                    if not isinstance(axs, (list, np.ndarray)):
                        axs = [axs]
                    
                    # Mostrar primero la imagen original
                    axs[0].imshow(img_bgr)
                    axs[0].set_title("Original")
                    axs[0].axis("off")

                    for i, (nombre, kernel) in enumerate(kernels.items(), start=1):
                        img_sharp = cv2.filter2D(img_bgr, -1, kernel)
                        axs[i].imshow(img_sharp)
                        axs[i].set_title(nombre)
                        axs[i].axis("off")

                    plt.tight_layout()
                    plt.show()

                    if len(kernels) != 3:
                        break                
            elif seleccion == '0':
                break
            else:
                 print("Error no se encuentra la opción ingresada "+seleccion)


#------------------------------------
# Función para cargar las imagenes
#------------------------------------
def opcionesImagenes (ruta_archivo):
    # 1. Cargar la imagen con OpenCV
    # Por defecto, cv2.imread carga la imagen en formato BGR
    img_bgr = cv2.imread(ruta_archivo)

    # Verificamos si la imagen cargó correctamente
    if img_bgr is None:
        print("No se encontró la imagen en: {ruta_archivo}")
        return 0

    # 2. CONVERSIÓN CRÍTICA: De BGR a RGB
    # Esto es necesario para que Matplotlib muestre los colores reales
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # 3. Mostrar la imagen con Matplotlib
    plt.figure(figsize=(8, 6))
    plt.imshow(img_rgb)

    # 4. Obtener información (alto, ancho, canales)
    alto, ancho, canales = img_bgr.shape

    # 5. Configurar la visualización
    plt.title("Imagen '"+Path(ruta_archivo).stem+"' cargada con OpenCV (BGR -> RGB)\n")
    plt.axis('off')  # Oculta los ejes
    # agregar un subplot y se agrega la información de la imagen
    plt.subplots_adjust(bottom=0.10)
    plt.figtext(
    0.5, 0.06,
    f"Dimensiones: {ancho}px x {alto}px \n"+f"Canales de color: {canales}",
    ha="center", fontsize=10,
    )
    plt.show()

    #Llamada a la funcion de operaciones con imagenes
    operacionesImagenes(img_rgb)


while True:
    print("--------------------------------")
    print("Ingrese las siguientes opciones:")
    print("--------------------------------")
    print("c para cargar la imagen")
    print("q para salir")

    seleccion = input("Ingrese su selección: ")

    if seleccion == 'c':
        while True:
            print("--------------------------------")
            print("Ingrese las siguientes opciones:")
            print("--------------------------------")
            print("1 para buho")
            print("2 para gato")
            print("3 para jirafa")
            print("0 para retornar")
            print("--------------------------------")

            opcion = input("Ingrese la imagen a cargar: ")

            if opcion == '0':
                break   

            elif opcion == '1':
                ruta_archivo = "C:/Users/Marce/Documents/SenalesImagenes/Tarea1/buho.jpg"
                #Llamada a la función cargar imagen
                animales = opcionesImagenes (ruta_archivo)
                

            elif opcion == '2':
                ruta_archivo = "C:/Users/Marce/Documents/SenalesImagenes/Tarea1/gato.jpg"
                #Llamada a la función cargar imagen
                animales = opcionesImagenes (ruta_archivo)

            elif opcion == '3':
                ruta_archivo = "C:/Users/Marce/Documents/SenalesImagenes/Tarea1/jirafa.jpg"
                #Llamada a la función cargar imagen
                animales = opcionesImagenes (ruta_archivo)

            else:
                print("-----------------------------------------------")
                print("Opción "+opcion+" inválida. Intente nuevamente.")
                print("-----------------------------------------------")

    elif seleccion == 'q':
        break

    else:
        print("--------------------------------------------------")
        print("Opción "+seleccion+" inválida. Intente nuevamente.")
        print("--------------------------------------------------")
