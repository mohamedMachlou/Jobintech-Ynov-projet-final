from datetime import date

def validate_concert_data(titre, date_value, lieu, prix_base, capacite, artiste):
    errors = []

    # Vérification du titre
    if not titre or not isinstance(titre, str):
        errors.append("Le titre doit être une chaîne non vide.")

    # Vérification de la date
    if not isinstance(date_value, date):
        errors.append("La date doit être de type datetime.date.")

    # Vérification du lieu
    if not lieu or not isinstance(lieu, str):
        errors.append("Le lieu doit être une chaîne non vide.")

    # Vérification de la prix de base
    if not isinstance(prix_base, int) or prix_base <= 0:
        errors.append("Le prix base doit être un entier positif.")

    # Vérification de la capacité
    if not isinstance(capacite, int) or capacite <= 0:
        errors.append("La capacité doit être un entier positif.")


    # Vérification de l'artiste
    if not artiste or not isinstance(artiste, str):
        errors.append("L'artiste doit être une chaîne non vide.")

    return errors
