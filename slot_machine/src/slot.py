import random

#disccionario de multiplicadores
multipliers = {
    "🍒": 2,
    "🍋": 3,
    "🍉": 4,
    "⭐": 5,
    "🧡": 6,
    "7️⃣": 7,
    "💎": 8,
}

def spin():
    """Gira los tres carretes y devuelve una lista con los resultados"""
    symbolos = ["🍒", "🍋", "🍉", "⭐", "🧡",  "7️⃣", "💎"]
    return [random.choice(symbolos) for _ in range(3)]   

def calculate_prize(bet=1):
    """Calcula el premio segun los simbolos obtenidos."""
    """
    Recibe:
        - spin_result: lista de 3 símbolos, ej. ["🍋","🍋","⭐"]
        - bet_amount: cuánto costó la tirada (por ejemplo 1 euro)
    Devuelve:
        - ganancia (número), puede ser 0, puede ser igual a bet_amount, o múltiplos
    """
    resultado = spin()

    #para saber cuantos iguales hay en mi spin: 
    # -1 = 3 iguales; 
    # -2 = 2 iguales; 
    # -3 = 0 iguales.
    
    igualdad = len(set(resultado)) 
    
    if igualdad ==  3:
        premio = bet * 0
    elif igualdad == 2:
        premio = bet
    elif igualdad == 1:
        simbolo = resultado[0]
        multiplicador = multipliers[simbolo]   
        premio = bet * multiplicador
        
    print(resultado)
    print(f"tu apuesta fue {bet}, y tu resultado fue {premio}")



print(calculate_prize(5))