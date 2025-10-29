import random

def spin():
    """Gira los tres carretes y devuelve una lista con los resultados"""
    symbolos = ["🍒", "🍋", "🍉", "⭐", "🧡", "7️⃣", "💎"]
    return [random.choice(symbolos) for _ in range(3 )]   


def calculate_prize(resultado):
    """Calcula el premio segun los simbolos obtenidos."""
    pass
