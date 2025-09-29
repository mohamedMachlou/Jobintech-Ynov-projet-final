from models.acheteur import Acheteur
import re


def validate_acheteur_email(email):
    existing_mails = list(map(lambda a: a.email, Acheteur.achateurs))

    if email in existing_mails:
        return "This mail is already used"

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return "This doesn't look a valid email"

    return True
