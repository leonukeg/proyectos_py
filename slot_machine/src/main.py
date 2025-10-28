"""
pseudocodigo del flujo principal 

1. Mostrar mensaje de bienvenida
2. Pedir al jugador solicitar el saldo inicial
3. Mostrar el coste de la tirada.
4. Mientras el Jugador tenga saldo y quiera seguir jugando:
    4.1- Restar el coste de la tirada al saldo 
    4.2- Generar los tres simbolos (usando slot.py)
    4.3- calcular el premio segun la jugada.
    4.4- Actualizar el saldo(usando player.py)
    4.5- Mostrar resultado (gano/perdio; saldo actual).
    4.6- Preguntar si quiere segur o retirarse
5. Si el jugador se retira o el saldo = 0:
    5.1- Mostrar mensaje de despedida.
    5.2- terminar programa
    
"""