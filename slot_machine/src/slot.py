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

def calculate_prize(resultado, bet=1):
    """Calcula el premio segun los simbolos obtenidos."""
    """
    Recibe:
        - spin_result: lista de 3 símbolos, ej. ["🍋","🍋","⭐"]
        - bet_amount: cuánto costó la tirada (por ejemplo 1 euro)
    Devuelve:
        - ganancia (número), puede ser 0, puede ser igual a bet_amount, o múltiplos
    """
    
    #para saber cuantos iguales hay en mi spin: 
    # -1 = 3 iguales; 
    # -2 = 2 iguales; 
    # -3 = 0 iguales.
    
    igualdad = len(set(resultado)) 
    
    if igualdad ==  3:
        premio = 0
    elif igualdad == 2:
        premio = bet
    elif igualdad == 1:
        simbolo = resultado[0]
        multiplicador = multipliers[simbolo]   
        premio = bet * multiplicador
    
    print("🎰 Resultado:", " | ".join(resultado))
    print(f"💰 Apostaste {bet}€ → Ganaste {premio}€")
    
    return premio


tirada = spin()

calculate_prize(tirada,3)