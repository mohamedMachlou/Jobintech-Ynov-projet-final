from dateutil.parser import parse
from datetime import datetime


def validate_date(date_str, future_only=None):
    """
    Valide une date entrée librement par l'utilisateur.

    Args:
        date_str (str): Date entrée par l'utilisateur.
        future_only (bool|None):
            - True → date future uniquement
            - False → date passée uniquement
            - None → aucune restriction

    Returns:
        True si la date est valide, sinon message d'erreur (str)
    """
    try:
        date_obj = parse(date_str, dayfirst=True)
        now = datetime.now()
        if future_only is True and date_obj < now:
            return "La date doit être dans le futur."
        if future_only is False and date_obj > now:
            return "La date doit être dans le passé."
        return True
    except Exception:
        return f"Date invalide : '{date_str}' n'est pas reconnue comme une date."


def validate_required(valeur):
    if not valeur.strip():
        return "Ce champ est obligatoire."
    return True


def validate_int(valeur):
    try:
        int(valeur)
        return True
    except ValueError:
        return "Veuillez entrer un nombre entier valide."


def validate_float(valeur):
    try:
        float(valeur)
        return True
    except ValueError:
        return "Veuillez entrer un nombre valide (décimal possible)."
