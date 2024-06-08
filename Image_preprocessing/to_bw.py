import os
import cv2

# Directorio de entrada con las imágenes originales
input_dir = 'images/val/neutral_new'
# Directorio de salida donde se guardarán las imágenes en blanco y negro
output_dir = 'images/train/neutral_elbueno'

# Crear el directorio de salida si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Inicializar el contador de imágenes
image_counter = 1

# Iterar sobre cada archivo en el directorio de entrada
for filename in os.listdir(input_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):  # Añadir más extensiones si es necesario
        # Leer la imagen
        img_path = os.path.join(input_dir, filename)
        img = cv2.imread(img_path)
        
        if img is not None:
            # Convertir la imagen a escala de grises
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Generar el nuevo nombre de archivo con el contador
            new_filename = f"neutral{image_counter}.jpg"
            image_counter += 1
            
            # Guardar la imagen en blanco y negro en el directorio de salida
            output_path = os.path.join(output_dir, new_filename)
            cv2.imwrite(output_path, gray_img)
            print(f"Imagen {new_filename} convertida a blanco y negro y guardada en {output_path}")
        else:
            print(f"No se pudo leer la imagen {filename}")

print("Conversión a blanco y negro completada.")
