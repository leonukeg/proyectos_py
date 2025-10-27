Futbol_Analytics

objetivos
"realizar la analitica automatica de un partido de futbol mediante a visualicion de un video del partido"

-Meterle un video de un partido.
-Detectar jugadores, pelota, sus posiciones a lo largo del tiempo.
-A partir de eso, construir métricas avanzadas tipo analista profesional.

    -expected goals
    -red de pases
    -mapas de calor 
    -posiciones promedio
    -distribucion y precision por jugador
    -ubicacion de tiros a puerta por jugador
    -mapa de tiros

Tecnologias a usar (hasta loS momentos)
-PYTHON
-yolo8
-openCV

segun GPT
dividir en modulo  ya que es complejo el proyecto 

MODULO A. PROCESAMIENTO DE VIDEO.
funcion: abrir un video y leer frame por frame 
    -Tec: openCV
    
MODULO B. DETECCION DE OBJETOS
Funcion: en cada frame, detectar cosas como:
    -jugadores (de un equipo y de otro)
    -balon
    -arbitro
    -porteria

    -Tec: YOLOv8 (deteccion de objetos en cada frame)

    salida:
    .jugador #X en coordenadas(x1,y1,x2,y2)
    -balon en coordenadas(x1,y1,x2,y2)

MODULO C. SEGUIMIENTO (TRACKING)
Funcion: ya no solo es caja en cada frame si no algo consecutivo de frames

    -jugador_7 :(x=120,y=300) en el segundo 10
    -jugador_7 :(x=138,y=310) en el segundo 10.4
    -etc.

    esto permite que -> 
        -mapa de calor
        -posicionamiento promedio
        -red de pases
        -distribucion y presicion del jugador

        "el trackin es mas complicado que A y B ya que se tiene que lidear  con IDs, pero hay tecnicas 

MODULO C. ANALISIS TECTICO / METRICAS 

    -mapas de calor → dónde se mueve cada jugador.
    -posiciones promedio → media de coordenadas por jugador para un intervalo.
    -red de pases → quién pasa a quién, cuántas veces, en qué zona del campo.
    -distribución y precisión por jugador → acierto de pases, tiros, etc.
    -ubicación de tiros a puerta por jugador → dónde chuta cada uno.
    -mapa de tiros → puntos desde donde se chutó.

Esto ya son analíticas de fútbol como las de la TV y en análisis pro.

Ojo importante: estas métricas dependen de información estructurada (eventos de pase, tiro, etc.) que no sale sola del video.
Extraer eventos automáticamente (detectar “esto fue un pase completo”, “esto fue un tiro”) es MUY avanzado. A nivel investigación seria.

No es imposible… pero no es el primer paso.

<span style="color:red; font-weight: bold;">
MODULO E. expected goals (xG)   OJO CON ESTE MODULO

xG = probabilidad de que un tiro termine en gol en base a distancia, ángulo, tipo de tiro, etc.

Para calcular xG de verdad, normalmente necesitas:

posición del tiro

contexto del tiro (presión, pie, cabeza, tipo de centro…)

un modelo entrenado con miles de tiros reales.

Eso está ya en la liga profesional y en empresas de datos. Hacer tu propio xG casero 100% automático desde video es un objetivo a largo plazo, nivel tesis.

Te digo esto para que no te castigues pensando “por qué no me sale el xG si es solo una fórmula”. No, xG es un modelo estadístico entrenado
</span>

