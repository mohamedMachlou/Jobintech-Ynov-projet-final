from models.acheteur import Acheteur
from utils.inputs import input
from validations.acheteur import validate_acheteur_email


def acheteur_registration():
    name = input("Nom:")
    email = input("Email:", validate=validate_acheteur_email)

    acheteur = Acheteur(name, email)
    # TODO: forward the achateur to a menu where they could buy billets
