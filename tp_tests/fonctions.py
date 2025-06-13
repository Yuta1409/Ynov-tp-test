def additionner(a, b):
    """Additionne deux nombres"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Les arguments doivent être des nombres.")
    return a + b

def diviser(a, b):
    """Divise a par b"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Les arguments doivent être des nombres.")
    if b == 0:
        raise ValueError("Division par zéro n'est pas permise.")
    return a / b

# def additionner_erreur(a, b):
#     """Additionne deux nombres"""
#     return a * b

def est_pair(nombre):
    """Vérifie si c'est un nombre est pair"""
    #si le nombre n'est pas divisible par 2, il est impair
    if nombre % 2 != 0:
        raise ValueError("Le nombre doit être pair.")
    return nombre % 2 == 0

def valider_email(email):
    """Valide un format d'email basique"""
    if "@" not in email or "." not in email:
        raise ValueError("L'email doit contenir un arobase et un point.")
    return True

def calculer_moyenne(notes):
    """Calcule la moyenne d'une liste de notes"""
    if len(notes) == 0:
        raise ValueError("La liste de notes ne peut pas être vide.")
    return sum(notes) / len(notes)

def convertir_temperature(celsius):
    """Convertit des degrés Celsius en Fahrenheit"""
    if not isinstance(celsius, (int, float)):
        raise TypeError("La température doit être un nombre.")
    return (celsius * 9/5) + 32