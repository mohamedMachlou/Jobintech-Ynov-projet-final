
import re
from dateutil.parser import parse
from datetime import datetime

# -----------------------------
# Validation obligatoire
# -----------------------------
def validate_required(valeur: str):
    if not valeur.strip():
        return "Ce champ est obligatoire."
    return True

# -----------------------------
# Validation alphanumérique (lettres, chiffres, espaces)
# -----------------------------
def validate_alphanumeric(valeur: str):
    if not valeur.strip():
        return "Ce champ est obligatoire."
    if not re.match(r'^[\w\s]+$', valeur):
        return "Veuillez entrer uniquement des lettres, chiffres ou espaces."
    return True

# -----------------------------
# Validation nombre entier
# -----------------------------
def validate_int(valeur: str):
    if valeur.isdigit():
        return True
    return "Veuillez entrer un nombre entier valide."

# -----------------------------
# Validation nombre décimal / float
# -----------------------------
def validate_float(valeur: str):
    try:
        float(valeur)
        return True
    except ValueError:
        return "Veuillez entrer un nombre valide (décimal possible)."

# -----------------------------
# Validation supérieure à une valeur
# -----------------------------
def validate_gt(valeur, target: int):
    if isinstance(v := validate_int(valeur), str):
        return v
    _valeur = int(valeur)
    return True if _valeur > target else f"Veuillez entrer un nombre supérieur à {target}"

# -----------------------------
# Validation inférieure ou égale à une valeur
# -----------------------------
def validate_lte(valeur, target: int):
    if isinstance(v := validate_int(valeur), str):
        return v
    _valeur = int(valeur)
    return True if _valeur <= target else f"Veuillez entrer un nombre inférieur ou égal à {target}"

# -----------------------------
# Validation de date
# -----------------------------
def validate_date(date_str: str, future_only=None):
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

