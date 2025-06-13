def additionner(a, b):
    """Additionne deux nombres"""
    return a + b

def est_pair(nombre):
    """Vérifie si un nombre est pair"""
    return nombre % 2 == 0

def valider_email(email):
    """Valide un format d'email basique"""
    if "@" in email and "." in email:
        return True
    return False

def calculer_moyenne(notes):
    """Calcule la moyenne d'une liste de notes"""
    if len(notes) == 0:
        return 0
    return sum(notes) / len(notes)

def convertir_temperature(celsius):
    """Convertit des degrés Celsius en Fahrenheit"""
    return (celsius * 9/5) + 32