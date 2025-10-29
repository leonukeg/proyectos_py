import random 

def number_aleatory():
    """genera un número aleatorio entre 0 y 9 incluidos"""
    return random.randint(0,9)

def reult(n1,n2,n3):
    """"determina el resultado del juego basado en tres números"""
    if n1== n2==n3:
        return "Win", 2
    elsif n1== n2 or n2==n3 or n1 == n3:
        return "Draw", 1
    else:
        return "Lost", 0

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
    
print(bet)