from models.acheteur import Acheteur
from utils.inputs import input, select
from validations.acheteur import validate_acheteur_email
from validations.common import validate_required


def acheteur_registration():
    name = input("Nom:", validate=validate_required)
    email = input("Email:", validate=validate_acheteur_email)

    # creation + forwarding to the next menu
    acheteur_action_selection(Acheteur(name, email))


def acheteur_action_selection(acheteur: Acheteur):
    from services.main_menu import main_menu

    ACHETEUR_ACTION_SELECTION_CHOICES = {
        "Buy Tickets": lambda: print("TODO: Buy"),
        "Unbuy Tickets": lambda: print("TODO: unbuy"),
        "Retour": main_menu,
    }

    choice = select(
        " ",
        choices=list(ACHETEUR_ACTION_SELECTION_CHOICES.keys()),
    )

    ACHETEUR_ACTION_SELECTION_CHOICES[choice]()
