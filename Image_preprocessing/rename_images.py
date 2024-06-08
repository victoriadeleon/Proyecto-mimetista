import os
import cv2

# Directorio de entrada con las imágenes originales
input_dir = 'images/val/neutral'
# Directorio de salida donde se guardarán las imágenes redimensionadas
output_dir = 'images/val/neutral_elbueno'

# Crear el directorio de salida si no existe
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Inicializar el contador
counter = 1

# Iterar sobre cada archivo en el directorio de entrada
for filename in os.listdir(input_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):  # Añadir más extensiones si es necesario
        # Leer la imagen
        img_path = os.path.join(input_dir, filename)
        img = cv2.imread(img_path)
        
        if img is not None:            
            # Construir el nuevo nombre del archivo
            new_filename = f"disgust{counter}.jpg"
            output_path = os.path.join(output_dir, new_filename)
            
            # Guardar la imagen redimensionada en el directorio de salida
            cv2.imwrite(output_path, img)
            
            # Incrementar el contador
            counter += 1
        else:
            print(f"No se pudo leer la imagen {filename}")

print(" completado.")
