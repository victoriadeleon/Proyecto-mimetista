# Proyecto-mimetista
Colaboración de investigación y desarrollo entre el ITESM y CIV.  

## Contexto
La división de investigación y desarrollo del CIV y el CIVART han determinado que lossujetos sometidos a situaciones extraordinarias de alto estrés tanto físico como psicológico,conllevan a un aletargamiento y consecuentemente a una parálisis en sus actividades de respuesta en los momentos de respuesta a un evento catastrófico. Al observar la evolución de las tecnológicas en auge, el CIV considera oportuno el desarrollo de una herramienta con la función de disminuir el riesgo psicológico y el trauma en las personas involucradas, (población directamente afectada, cuerpos de respuesta y voluntarios) en las diferentes etapas de un desastre natural y/o antropogénico. Dicha herramienta buscará incrementar la eficiencia de los involucrados en una zona de desastre con el objetivo de agilizar la respuesta a la catástrofe. Asimismo, buscará contribuir en la disminución de futuros riesgos y vulnerabilidades en las etapas consiguientes de la recuperación frente a un desastre.

## Objetivo
* Identificar el estado parcial psicológico de las personas afectadas y en shock por medio de procedimientos no invasivos, utilizando reconocimiento de imagen para detectar emociones básicas
* Distinguir entre los distintos actores generales involucrados en el desastre, de acuerdo con el color de su uniforme:
  1. Población Civil Afectada (PCA): Azul, morado
  2. Voluntarios Civiles y Personal de Respuesta Civil (PRC): Amarillo, rojo, naranja
  3. Personal de respuesta DNIII y entidades semejantes (PRM): Verde
* Traducir ambas lecturas a un sistema de categorías Triage (nivel de estrés/shock: alto, medio, bajo).

| Nivel de estrés | Emoción asociada |
| ------------- | ------------- |
| Alto | Enojo, miedo|
| Medio | Tristeza, sorpresa, disgusto |
| Bajo | Neutralidad, Felicidad | 

Se presenta una solución utilizando visión computacional para detectar el estado parcial psicológico de diferentes individuos así como su clasificación por roles de acuerdo con el color de su uniforme. Se considera un contexto en donde se presenta una situación de desastre, en donde los sujetos están sometidos a situaciones de alto estrés. De acuerdo con la clasificación realizada, se genera una simulación que sigue un protocolo de calma y estabilización, presentando una transición de colores determinada.

## Solución
* Se realizó un sistema de detección de emociones básicas

Desarrollo de software: YOLOV8, PyGame, 
### Sistema de categorías Triage
![image](https://github.com/victoriadeleon/Proyecto-mimetista/assets/70030691/362f0184-e33e-4962-9674-821d280b4388)
### Identificación de sujetos involucrados por color de vestimenta:
![image](https://github.com/victoriadeleon/Proyecto-mimetista/assets/70030691/0f4f3011-de41-4f7f-ac38-ea06f13b5164)
