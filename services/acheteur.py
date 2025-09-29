from models.acheteur import Acheteur
from utils.inputs import input, select
from validations.acheteur import validate_acheteur_email
from validations.common import validate_required


def acheteur_registration():
    name = input("Nom:", validate=validate_required)
    email = input("Email:", validate=validate_acheteur_email)

    acheteur = Acheteur(name, email)
    # TODO: forward the achateur to a menu where they could buy billets
