import random 
"""VERSION 0.1
number1, number2, number3  = number(), number(), number()

bet = 1

print(number1, number2, number3)

if number1 == number2 == number3 :
    print("Win")
    bet *= 2
elif number1 == number2 or number1 == number3 or number2 == number3:
    print("Draw")
    bet = bet
else:
    print("Lost")
    
    bet -= bet
    
print(bet)"""

#VERSION 1.0
def number_random():
    """Genera un número aleatorio entre 0 y 9 incluidos"""
    return random.randint(0,9)

def result(n1,n2,n3):
    """"Determina el resultado del juego basado en tres números"""
    if n1== n2==n3:
        return "Win", 2
    elif n1== n2 or n2==n3 or n1 == n3:
        return "Draw", 1
    else:
        return "Lost", 0

def main():
    #generamos 3 numero aleatoreos 
    num1, num2, num3 = number_random(), number_random(), number_random()
    
    #apuesta inicial
    bet = 1
    
    print(num1,num2,num3)
    
    #determinamos resultado y calculamos nueva apuesta
    resultado, multiplicador = result(num1, num2, num3)
    print(resultado)
    
    bet += multiplicador
    
    print(bet)


main()
