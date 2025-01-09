# Computer Vision Project
Emotion recognition and uniform color detection for enhanced decision-making in high-risk scenarios.

## Context
The research and development division of CIV and CIVART in Mexico City have determined that individuals subjected to extraordinary high-stress situations, both physical and psychological, experience lethargy and, consequently, paralysis in their response activities during catastrophic events. Observing the evolution of emerging technologies, CIV considers it timely to develop a tool that reduces psychological risk and trauma for the people involved (directly affected population, response teams, and volunteers) in the various stages of a natural and/or anthropogenic disaster. This tool seeks to increase the efficiency of those involved in a disaster zone, with the goal of accelerating the response to the catastrophe and contributing to reducing future risks and vulnerabilities during the post-disaster recovery stages.

## Goal
* Identify the partial psychological state of affected individuals in shock through non-invasive procedures, using image recognition to detect basic emotions.
* Distinguish between the different general actors involved in the disaster based on the color of their uniform:
  1. Affected Civilian Population (ACP): Blue, purple.
  2. Civil Volunteers and Civil Response Personnel (CRP): Yellow, red, orange.
  3. DNIII Response Personnel and Similar Entities (RPE): Green.
* Translate both readings into a Triage category system (stress/shock levels: high, medium, low).

| Stress Level    | Associated Emotion                         |
|-----------------|--------------------------------------------|
| High            | Anger, fear                                |
| Medium          | Sadness, surprise, disgust                 |
| Low             | Neutrality, happiness                      |

## Solution
**Software Resources:** YOLOv8, OpenCV, Pygame.

A solution is presented using computer vision to detect the partial psychological state of different individuals and classify them by roles based on the color of their uniform. In a disaster context, where individuals are subjected to high-stress situations, a simulation is generated following a protocol for calm and stabilization, presenting a determined color transition.

## Stages

### A. Elemental Emotion Detection
* A basic emotion detection system was developed (anger, fear, sadness, surprise, disgust, neutrality, happiness) using YOLOv8.
* **Model Training:** The model was trained with images from the following datasets:
  - [Micro-expressions](https://www.kaggle.com/datasets/kmirfan/micro-expressions/data)
  - [Emotion Detection FER](https://www.kaggle.com/datasets/ananthu017/emotion-detection-fer)
* **Image Preprocessing** Manual selection and application of a preprocessing algorithm to scale the images to 80x80 and convert them to grayscale to facilitate facial feature detection.
* **Dataset Distribution** 800 images for training and 180 for validation per emotion (5600 total training images and 1260 validation images).
  
### B. Uniform Color Detection
* **Image Processing:** Use of image processing techniques with HSV ranges and masks to detect the uniform color of identified subjects.
* **HSV Range Adjustment:** Ensuring correct detection for each case.
* **Video Capture:** Use of OpenCV to capture real-time video and apply detection masks to each frame.
* **Real-Time Detection:** Implementation of simple logic to display the detected color on the screen.

### C. Triage Category System
* **Detection Conditions:** Programming the necessary conditions to detect different stress/shock states using the reference table.
* **State Machine:** Development of a state machine to determine the necessary protocol to follow.
* **LED Light Simulator:** Use of Pygame to generate an LED light simulator where the color transition occurs as specified in the category system table.

### Triage Category System
![Sistema de Categorías Triage](https://github.com/victoriadeleon/Proyecto-mimetista/assets/70030691/362f0184-e33e-4962-9674-821d280b4388)

### Identification of Involved Subjects by Uniform Color
![Identificación de Sujetos](https://github.com/victoriadeleon/Proyecto-mimetista/assets/70030691/0f4f3011-de41-4f7f-ac38-ea06f13b5164)

## Project Value
This project aims to provide an innovative tool to improve disaster response by reducing psychological impact and increasing the efficiency of the teams involved. Through the use of advanced computer vision and image processing technologies, this project promises to be a valuable resource in emergency management.

<div style="display: flex; justify-content: center; align-items: center; gap: 10px;">
  <img src="https://github.com/user-attachments/assets/66e140f1-715e-4650-8429-1a89c3c878a4" alt="Image 1" width="300"/>
  <img src="https://github.com/user-attachments/assets/a3d3ffc9-9a06-4d71-9283-a32649f57a90" alt="Image 2" width="300"/>
</div>

