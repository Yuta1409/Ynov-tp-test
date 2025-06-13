def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Les arguments doivent être des nombres.")
    return a + b
    pass

def divise(a, b):
    """Divise a par b."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Les arguments doivent être des nombres.")
    if b == 0:
        raise ValueError("Division par zéro.")
    return float(a) / float(b)

def power(base, exponent):
    """Élève base à la puissance exponent."""
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Les arguments doivent être des nombres.")
    return float(base ** exponent)

def power(base, exponent):
    """Élève base à la puissance exponent."""
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Les arguments doivent être des nombres.")    
    #Gérer le cas où base est 0 et exponent est négatif
    if base == 0 and exponent < 0:
        raise ValueError("0 ne peut pas être élevé à une puissance négative.")
    return base ** exponent