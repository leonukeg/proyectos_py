import random

def spin():
    """Gira los tres carretes y devuelve una lista con los resultados"""
    symbolos = ["🍒", "🍋", "🍉", "⭐", "🧡", "7️⃣", "💎"]
    return [random.choice(symbolos) for _ in range(3 )]   


def calculate_prize(resultado):
    """Calcula el premio segun los simbolos obtenidos."""
    """
    Recibe:
        - spin_result: lista de 3 símbolos, ej. ["🍋","🍋","⭐"]
        - bet_amount: cuánto costó la tirada (por ejemplo 1 euro)
    Devuelve:
        - ganancia (número), puede ser 0, puede ser igual a bet_amount, o múltiplos
    """
    pass
