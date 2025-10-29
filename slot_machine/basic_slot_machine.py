import random 

#genero tres numero aleatoreos
def number():
    return random.randint(0,9)

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