import re

def is_valid_email(email):
    if not isinstance(email, str):
        raise TypeError("L'email doit être une chaîne de caractères.")

    # TODO: Vérifier qu'il y a exactement un @
    if email.count('@') != 1:
        #raise TypeError("L'email doit contenir exactement un arobase '@'.")
        return False

    # TODO: Séparer en partie locale et domaine
    local, domaine = email.split('@')
    
    # TODO: Valider partie locale (regex: ^[a-zA-Z0-9._-]+$)
    if not re.match(r'^[a-zA-Z0-9._-]+$', local):
        #raise TypeError("La partie locale de l'email n'est pas valide.")
        return False
    
    # TODO: Valider domaine (regex: ^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$)    
    if not re.match(r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$', domaine):
        #raise TypeError("Le domaine de l'email n'est pas valide.")
        return False
    return True
