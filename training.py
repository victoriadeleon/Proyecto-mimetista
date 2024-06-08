from ultralytics import YOLO
import torch

def main():
    # Verifica si CUDA está disponible y selecciona el dispositivo
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    if torch.cuda.is_available():
        print("CUDA está disponible. Detalles de la GPU:")
        for i in range(torch.cuda.device_count()):
            print(f"Nombre de la GPU {i}: {torch.cuda.get_device_name(i)}")
    else:
        print("CUDA no está disponible. Usando CPU.")

    # Cargar el modelo YOLOv8 preentrenado y moverlo al dispositivo
    model = YOLO('yolov8n.pt').to(device) 
    # Entrenar el modelo
    model.train(data='C:/Users/victo/OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey/Computer backup/6 sem/Computer-vision/YOLO_blackandwhite/dataset.yaml', epochs=80, imgsz=80)

if __name__ == "__main__":
    main()
