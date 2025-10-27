Futbol_Analytics

Objetivo general

Analizar automáticamente un partido de fútbol a partir de video para extraer métricas tácticas y de rendimiento.

Metricas Finales deseadas(long vision)
-expected goals (xG)
-red de pases
-mapas de calor
-posiciones promedio
-distribución y precisión por jugador
-ubicación de tiros a puerta por jugador
-mapa de tiros

Stack inicial

-python
-openCV (para lectura y manejo de video)
-YOLOv8 (deteccion de jugadores y balon)


version0.1(primer hito practico)
.input ( un clip de video corto)
.output:
    .detectar jugadores en cada frame
    .guardar posiciones en el campo ( cordenadas pixel)
    .generar un grafico visual de por donde se movio cada jugador

NO CUBRE TODAVIA
.identificador de jugadores
.distincion de equipos
.detector de pases
.calculde de xG.

Poximos hitos
-v0.2: tracking consistente por jugador (seguir al mismo jugador entre frames).
-v0.3: estimar posición normalizada en el campo (convertir de píxeles de cámara a un plano de 105x68m).
-v0.4: eventos tipo “tiro” o “pase”.

