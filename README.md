# Proyecto Mimetista
Colaboración de investigación y desarrollo entre el ITESM y el CIV.

## Contexto
La división de investigación y desarrollo del CIV y el CIVART han determinado que los sujetos sometidos a situaciones extraordinarias de alto estrés, tanto físico como psicológico, experimentan aletargamiento y, consecuentemente, una parálisis en sus actividades de respuesta durante eventos catastróficos. Observando la evolución de las tecnologías emergentes, el CIV considera oportuno desarrollar una herramienta que disminuya el riesgo psicológico y el trauma en las personas involucradas (población directamente afectada, cuerpos de respuesta y voluntarios) en las diferentes etapas de un desastre natural y/o antropogénico. Esta herramienta busca incrementar la eficiencia de los involucrados en una zona de desastre, con el objetivo de agilizar la respuesta a la catástrofe y contribuir a disminuir futuros riesgos y vulnerabilidades en las etapas de recuperación posteriores a un desastre.

## Objetivo
* Identificar el estado psicológico parcial de las personas afectadas y en shock mediante procedimientos no invasivos, utilizando reconocimiento de imagen para detectar emociones básicas.
* Distinguir entre los distintos actores generales involucrados en el desastre, de acuerdo con el color de su uniforme:
  1. **Población Civil Afectada (PCA):** Azul, morado.
  2. **Voluntarios Civiles y Personal de Respuesta Civil (PRC):** Amarillo, rojo, naranja.
  3. **Personal de Respuesta DNIII y Entidades Semejantes (PRM):** Verde.
* Traducir ambas lecturas a un sistema de categorías Triage (nivel de estrés/shock: alto, medio, bajo).

| Nivel de Estrés | Emoción Asociada                           |
|-----------------|--------------------------------------------|
| Alto            | Enojo, miedo                               |
| Medio           | Tristeza, sorpresa, disgusto               |
| Bajo            | Neutralidad, felicidad                     |

## Solución
**Recursos de Software:** YOLOv8, OpenCV, Pygame.

Se presenta una solución utilizando visión computacional para detectar el estado psicológico parcial de diferentes individuos y su clasificación por roles, de acuerdo con el color de su uniforme. En un contexto de desastre, donde los sujetos están sometidos a situaciones de alto estrés, se genera una simulación que sigue un protocolo de calma y estabilización, presentando una transición de colores determinada.

## Etapas

### A. Detección de Emociones Básicas
* Se desarrolló un sistema de detección de emociones básicas (enojo, miedo, tristeza, sorpresa, disgusto, neutralidad, felicidad) utilizando YOLOv8.
* **Entrenamiento del Modelo:** Se entrenó el modelo con imágenes de las siguientes bases de datos:
  - [Micro-expressions](https://www.kaggle.com/datasets/kmirfan/micro-expressions/data)
  - [Emotion Detection FER](https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer)
* **Preprocesamiento de Imágenes:** Selección manual y aplicación de un algoritmo de preprocesamiento para escalar las imágenes a 80x80 y convertirlas a escala de grises para facilitar la detección de rasgos faciales.
* **Distribución del Dataset:** 800 imágenes para entrenamiento y 180 para validación para cada emoción (5600 imágenes totales de entrenamiento y 1260 de validación).

### B. Detección de Color de Uniforme
* **Procesamiento de Imagen:** Uso de técnicas de procesamiento de imagen por rangos HSV con máscaras para detectar el color del uniforme de los sujetos identificados.
* **Ajuste de Rangos HSV:** Asegurar una correcta detección para cada caso.
* **Captura de Video:** Utilización de OpenCV para capturar video en tiempo real y aplicar las máscaras de detección a cada frame.
* **Detección en Tiempo Real:** Implementación de lógica simple para imprimir en pantalla el color detectado.

### C. Sistema de Categorías Triage
* **Condiciones de Detección:** Programación de las condiciones necesarias para detectar los diferentes estados de estrés/shock, usando la tabla de referencia.
* **Máquina de Estados:** Desarrollo de una máquina de estados para determinar el protocolo necesario a seguir.
* **Simulador de Luz LED:** Uso de Pygame para generar un simulador de luz LED donde la transición de colores ocurre como se especifica en la tabla del sistema de categorías.

## Resultados

### Sistema de Categorías Triage
![Sistema de Categorías Triage](https://github.com/victoriadeleon/Proyecto-mimetista/assets/70030691/362f0184-e33e-4962-9674-821d280b4388)

### Identificación de Sujetos Involucrados por Color de Vestimenta
![Identificación de Sujetos](https://github.com/victoriadeleon/Proyecto-mimetista/assets/70030691/0f4f3011-de41-4f7f-ac38-ea06f13b5164)

## Conclusión
El Proyecto Mimetista busca proporcionar una herramienta innovadora para mejorar la respuesta en situaciones de desastre, reduciendo el impacto psicológico y aumentando la eficiencia de los equipos involucrados. A través del uso de tecnologías avanzadas de visión computacional y procesamiento de imagen, este proyecto promete ser un recurso valioso en la gestión de emergencias.
