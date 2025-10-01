from models.acheteur import Acheteur
from services.vente_service import list_achateur_ventes_menu, make_a_vente_menu
from utils.inputs import input, select
from validations.acheteur import validate_acheteur_email
from validations.common import validate_required


def faire_des_achats_menu():
    from services.main import main_menu

    FAIRE_ACHATS_CHOICES = {
        "Nouveau Acheteur": acheteur_registration,
        "Acheteur Existant": acheteur_user_selection,
        "Retour": main_menu,
    }

    choice = select(
        " ",
        choices=list(FAIRE_ACHATS_CHOICES.keys()),
    )

    FAIRE_ACHATS_CHOICES[choice]()


def acheteur_registration():
    name = input("Nom:", validate=validate_required)
    email = input("Email:", validate=validate_acheteur_email)

    # creation + forwarding to the next menu
    acheteur_action_selection_menu(Acheteur(name, email))


def acheteur_action_selection_menu(acheteur: Acheteur):
    from services.main import main_menu

    ACHETEUR_ACTION_SELECTION_CHOICES = {
        "Lister & Manage Mes Ventes/Tickets": lambda: list_achateur_ventes_menu(
            acheteur
        ),
        "Buy Ticket": lambda: make_a_vente_menu(acheteur),
        "Retour": main_menu,
    }

    choice = select(
        f"Hi {acheteur.nom.capitalize()}, What would you like to do ?",
        choices=list(ACHETEUR_ACTION_SELECTION_CHOICES.keys()),
    )

    ACHETEUR_ACTION_SELECTION_CHOICES[choice]()


def acheteur_user_selection():
    ACHETEUR_USER_SELECTION_CHOICES = {
        # spread existing acheteurs as a choice
        **{
            a.nom: (lambda a=a: acheteur_action_selection_menu(a))
            for a in Acheteur.achateurs
        },
        "Retour": faire_des_achats_menu,
    }

    choice = select(
        f"",
        choices=list(ACHETEUR_USER_SELECTION_CHOICES.keys()),
    )

    ACHETEUR_USER_SELECTION_CHOICES[choice]()
