from datetime import datetime


def validate_billet_data(titre, date_event, lieu, prix_base, type_billet):
    errors = []

    if not titre or not isinstance(titre, str):
        errors.append("Titre invalide.")

    if not isinstance(date_event, datetime):
        errors.append("Date invalide, doit être un objet datetime.")

    if not lieu or not isinstance(lieu, str):
        errors.append("Lieu invalide.")

    if not isinstance(prix_base, (int, float)) or prix_base <= 0:
        errors.append("Prix de base invalide.")

    if type_billet not in ["Standard", "VIP"]:
        errors.append(f"Type de billet invalide : {type_billet}")

    return errors
