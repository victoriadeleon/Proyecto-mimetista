from ultralytics import YOLO
from PIL import Image
import torch
import cv2
import numpy as np
from facenet_pytorch import MTCNN
import time
import threading

color_ranges = {
    "Azul": [(90, 100, 100), (140, 255, 255)],
    "Morado": [(120, 50, 50), (160, 255, 255)],
    "Amarillo": [(20, 100, 100), (30, 255, 255)],
    "Rojo1": [(0, 120, 70), (10, 255, 255)],
    "Rojo2": [(170, 120, 70), (180, 255, 255)],
    "Naranja": [(10, 100, 100), (25, 255, 255)],
    "Verde": [(40, 40, 40), (90, 255, 255)]
}

def detect_colors(hsv_frame):
    color_counts = {color: 0 for color in color_ranges.keys()}
    for color, (lower, upper) in color_ranges.items():
        if color == "Rojo1" or color == "Rojo2":
            lower_bound1 = np.array(color_ranges["Rojo1"][0], dtype=np.uint8)
            upper_bound1 = np.array(color_ranges["Rojo1"][1], dtype=np.uint8)
            lower_bound2 = np.array(color_ranges["Rojo2"][0], dtype=np.uint8)
            upper_bound2 = np.array(color_ranges["Rojo2"][1], dtype=np.uint8)
            mask1 = cv2.inRange(hsv_frame, lower_bound1, upper_bound1)
            mask2 = cv2.inRange(hsv_frame, lower_bound2, upper_bound2)
            mask = cv2.bitwise_or(mask1, mask2)
        else:
            lower_bound = np.array(lower, dtype=np.uint8)
            upper_bound = np.array(upper, dtype=np.uint8)
            mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)
        
        color_counts[color] = cv2.countNonZero(mask)
    
    predominant_color = max(color_counts, key=color_counts.get)
    return predominant_color

def detect_emotion_from_frame(frame, model, mtcnn, target_size=(80, 80), resize_width=800, save_sample=False):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)  

    original_height, original_width = gray_frame.shape[:2]
    if original_width > resize_width:
        resize_height = int((resize_width / original_width) * original_height)
        gray_frame_resized = cv2.resize(gray_frame, (resize_width, resize_height))
    else:
        gray_frame_resized = gray_frame
        resize_height = original_height  

    img = Image.fromarray(cv2.cvtColor(gray_frame_resized, cv2.COLOR_BGR2RGB))  

    if save_sample:
        img.save("sample_image.jpg")

    boxes, _ = mtcnn.detect(img)

    if boxes is not None and len(boxes) > 0:
        # Asumimos que solo hay una cara en la imagen
        x1, y1, x2, y2 = boxes[0]

        # Recortar la región de la cara
        face_cropped = img.crop((x1, y1, x2, y2))

        # Redimensionar la imagen recortada de la cara
        img_resized = face_cropped.resize(target_size)

        # Hacer la predicción
        results = model.predict(np.array(img_resized), device=model.device)

        if results[0].boxes is not None and len(results[0].boxes) > 0:
            predictions = results[0].boxes
            # Encontrar la predicción con la confianza más alta
            highest_confidence_prediction = max(predictions, key=lambda p: p.conf.item())
            class_id = int(highest_confidence_prediction.cls.item())
            class_name = model.names[class_id]
            box = highest_confidence_prediction.xyxy[0].cpu().numpy()  # Mover el tensor a la CPU antes de convertirlo a numpy

            # Ajustar las coordenadas de la caja al tamaño de la imagen redimensionada
            scale_x = (x2 - x1) / target_size[0]
            scale_y = (y2 - y1) / target_size[1]
            x1_new, y1_new, x2_new, y2_new = box * [scale_x, scale_y, scale_x, scale_y]

            # Ajustar las coordenadas de la caja al tamaño original de la imagen
            x1_final = x1 + x1_new * (resize_width / original_width)
            y1_final = y1 + y1_new * (resize_height / original_height)
            x2_final = x1 + x2_new * (resize_width / original_width)
            y2_final = y1 + y2_new * (resize_height / original_height)

            # Dibujar la caja y la etiqueta en el frame original
            cv2.rectangle(frame, (int(x1_final), int(y1_final)), (int(x2_final), int(y2_final)), (255, 0, 0), 2)
            return frame, class_name
        else:
            return frame, "No se detectó ninguna emoción"
    else:
        return frame, "No se detectó ninguna cara"

def control_lights(predominant_color, emotion_text):
    pygame_thread = threading.Thread(target=pygame_process, args=(predominant_color, emotion_text))
    pygame_thread.start()
    pygame_thread.join()  # Esperar a que el hilo de Pygame termine antes de continuar

# Funciones de Pygame
def pygame_process(predominant_color, emotion_text):
    import pygame
    import sys
    import time

    # Inicializar Pygame
    pygame.init()

    # Configuración de la pantalla
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Simulación de Luz Relajante")

    # Colores
    black = (0, 0, 0)
    blue = (0, 0, 255)
    dark_blue = (0, 0, 85)
    green = (0, 255, 0)
    dark_green = (0, 85, 0)
    red = (255, 0, 0)
    dark_red = (85, 0, 0)

    # Configuración de la luz
    light_radius = 300
    center_x = 400
    center_y = 300

    # Función para crear un gradiente circular
    def draw_gradient(screen, color, center, radius):
        for i in range(radius, 0, -1):
            alpha = int(255 * (1 - (i / radius)))
            s = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            s.set_alpha(alpha)
            pygame.draw.circle(s, color, (radius, radius), i)
            screen.blit(s, (center[0] - radius, center[1] - radius))

    # Función para simular el parpadeo con efecto de gradiente
    def blink_light(color, dark_color, on_duration, off_duration, total_duration):
        end_time = time.time() + total_duration
        while time.time() < end_time:
            # Encender la luz
            screen.fill(black)
            draw_gradient(screen, color, (center_x, center_y), light_radius)
            pygame.display.flip()
            time.sleep(on_duration)
            # Apagar la luz a un color oscuro
            screen.fill(black)
            draw_gradient(screen, dark_color, (center_x, center_y), light_radius)
            pygame.display.flip()
            time.sleep(off_duration)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    # Función para realizar transiciones lentas entre múltiples colores sin repetir
    def slow_transition_colors(colors, dark_colors, duration):
        start_time = time.time()
        num_colors = len(colors)
        index = 0
        while time.time() - start_time < duration:
            color = colors[index]
            dark_color = dark_colors[index]
            blink_light(color, dark_color, 1, 1, 2)  # Transición lenta durante 10 segundos para cada color
            index = (index + 1) % num_colors

    if predominant_color in ["Azul", "Morado"]: # Grupo 1 (PCA). Protocolo 1 (experimental TRL2 de calma y estabilización)
        if emotion_text in ["anger", "fear"]:
            blink_light(blue, dark_blue, 0.1, 0.1, 30)
            blink_light(green, dark_green, 0.5, 0.5, 30)
            slow_transition_colors([red, green, blue], [dark_red, dark_green, dark_blue], 30)
        elif emotion_text in ["sadness", "surprise", "disgust"]:
            blink_light(blue, dark_blue, 1, 1, 30)
            slow_transition_colors([red, green, blue], [dark_red, dark_green, dark_blue], 30)
            slow_transition_colors([red, green, blue], [dark_red, dark_green, dark_blue], 30)
        elif emotion_text in ["neutral", "happiness"]:
            blink_light(red, dark_red, 0.1, 0.1, 30)
            blink_light(green, dark_green, 0.5, 0.5, 30)
            blink_light(blue, dark_blue, 1, 1, 30)
    elif predominant_color in ["Amarillo", "Rojo1", "Rojo2", "Naranja"]: # Grupo 1 (PCA). Protocolo 1 (experimental TRL2 de calma y estabilización)
        if emotion_text in ["anger", "fear"]:
            blink_light(blue, dark_blue, 0.1, 0.1, 30)
            blink_light(red, dark_red, 0.5, 0.5, 30)
            slow_transition_colors([red, green, blue], [dark_red, dark_green, dark_blue], 30)
        elif emotion_text in ["sadness", "surprise", "disgust"]:
            blink_light(blue, dark_blue, 1, 1, 30)
            slow_transition_colors([red, green, blue], [dark_red, dark_green, dark_blue], 30)
            blink_light(blue, dark_blue, 1, 1, 30)
        elif emotion_text in ["neutral", "happiness"]:
            blink_light(red, dark_red, 0.1, 0.1, 30)
            blink_light(green, dark_green, 0.5, 0.5, 30)
            blink_light(blue, dark_blue, 1, 1, 30)
    elif predominant_color == "Verde":
        if emotion_text in ["anger", "fear"]:
            blink_light(red, dark_red, 0.1, 0.1, 30)
            blink_light(red, dark_red, 0.5, 0.5, 30)
            slow_transition_colors([red, green, blue], [dark_red, dark_green, dark_blue], 30)
        elif emotion_text in ["sadness", "surprise", "disgust"]:
            blink_light(blue, dark_blue, 1, 1, 30)
            slow_transition_colors([red, green, blue], [dark_red, dark_green, dark_blue], 30)
            blink_light(blue, dark_blue, 1, 1, 30)
        elif emotion_text in ["neutral", "happiness"]:
            blink_light(red, dark_red, 0.1, 0.1, 30)
            blink_light(green, dark_green, 0.5, 0.5, 30)
            blink_light(blue, dark_blue, 1, 1, 30)

def main():
    # Verificar si CUDA está disponible y seleccionar el dispositivo
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    if torch.cuda.is_available():
        print("CUDA está disponible. Detalles de la GPU:")
        for i in range(torch.cuda.device_count()):
            print(f"Nombre de la GPU {i}: {torch.cuda.get_device_name(i)}")
    else:
        print("CUDA no está disponible. Usando CPU.")

    # Cargar el modelo entrenado y moverlo al dispositivo
    model = YOLO('runs/detect/train2/weights/best.pt').to(device)

    # Inicializar el detector de caras MTCNN
    mtcnn = MTCNN(keep_all=False, device=device)

    # Capturar video desde la cámara web
    cap = cv2.VideoCapture(0)

    last_update_time = time.time()
    emotion_text = ""
    sample_saved = False

    emotion_counter = 0
    previous_emotion = ""
    predominant_color = "Desconocido"  # Inicializar la variable con un valor predeterminado

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        current_time = time.time()
        if current_time - last_update_time >= 1:  
            frame, detected_emotion = detect_emotion_from_frame(frame, model, mtcnn, save_sample=not sample_saved)
            last_update_time = current_time
            sample_saved = True
        else:
            frame, detected_emotion = detect_emotion_from_frame(frame, model, mtcnn)

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        predominant_color = detect_colors(hsv_frame)

        cv2.putText(frame, detected_emotion, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(frame, f"Color: {predominant_color}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Emotion and Color Detection', frame)

        if detected_emotion == previous_emotion:
            emotion_counter += 1
        else:
            emotion_counter = 1
            previous_emotion = detected_emotion

        if emotion_counter >= 50:
            print(f"Color predominante detectado: {predominant_color}")

            # Pausar la captura de video
            cap.release()

            # Ejecutar control de luces y esperar a que termine
            control_lights(predominant_color, detected_emotion)

            # Reanudar la captura de video
            cap = cv2.VideoCapture(0)

            # Resetear el contador y la emoción previa para evitar repeticiones constantes
            emotion_counter = 0
            previous_emotion = ""

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
