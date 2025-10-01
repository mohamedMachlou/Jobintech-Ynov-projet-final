def validate_conference_data(titre, date, lieu, prix_base, capacite, orateur_principal):
    errors = []

    if not titre or len(titre) < 3:
        errors.append("Le titre doit contenir au moins 3 caractères.")
    if not lieu:
        errors.append("Le lieu est obligatoire.")
    if prix_base <= 0:
        errors.append("Le prix de base doit être supérieur à 0.")
    if capacite <= 0:
        errors.append("La capacité doit être positive.")
    if not orateur_principal:
        errors.append("L’orateur principal est obligatoire.")

    return errors
