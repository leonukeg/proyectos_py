SLOT MACHINE

reglas del juego -> 
-inicia el juego 
-pregunta importe a introducir 
-notifica que cada tirada tiene un coste de X€
-pregunta si quiere hacer tirada 
**-hace la jugada 
    -aleatoria de entre 0 y 6
    -tres veces (una por carril) 
    - 🍒= 0, 🍋=1, 🍉=2, ⭐=3, 🧡=4, 7️⃣=5, 💎=6.
-dependiendo del resultado de los tres carretes se genera un porcentaje a ganar 
    - 0 iguales x0
    - 2 iguales x1 (es decir no pierde quedas tabla)
    - 3 iguales ->
        - 0 x2
        - 1 x3
        - 2 x4
        - 3 x5
        - 4 x6
        - 5 x7
        - 6 x8 (max premio)
- se calcula la ganacia o perdida 
- se informa al jugador si gano o perdio
**- se muestra saldo al jugador
- se pregunta si quiere seguir jugando o si quiere retirar
    - en caso de seguir jugando se reinicia el bucle de juego de hacer tirada desde **
    - en caso de retirada se agradece por su juego e invita a jugar nuevamente y sale del juego  