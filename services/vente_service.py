from datetime import datetime as Datetime
from models.acheteur import Acheteur
from models.evenement import Evenement
from models.vente import Vente
from utils import select


def acheteur_vente_action_selection_menu(vente: Vente):
    # TODO: manage options here
    print(vente)
    pass


def make_a_vente_action_menu(acheteur: Acheteur, evenement: Evenement):
    pass


def make_a_vente_menu(acheteur: Acheteur):
    from services.acheteur_service import acheteur_action_selection_menu

    future_evenements = list(
        filter(lambda e: e.date > Datetime.now(), Evenement.evenements)
    )

    FUTURE_EVENEMENTS_SELECTION_CHOICES = {
        **{
            str(e): (lambda e=e: make_a_vente_action_menu(acheteur, e))
            for e in future_evenements
        },
        "Retour": lambda: acheteur_action_selection_menu(acheteur),
    }

    choice = select(
        f"You can see & manage your tickets here {acheteur.nom.capitalize()}",
        choices=list(FUTURE_EVENEMENTS_SELECTION_CHOICES.keys()),
    )

    FUTURE_EVENEMENTS_SELECTION_CHOICES[choice]()


def list_achateur_ventes_menu(acheteur: Acheteur):
    from services.acheteur_service import acheteur_action_selection_menu

    ACHETEUR_VENTES_SELECTION_CHOICES = {
        **{
            str(v): (lambda v=v: acheteur_vente_action_selection_menu(v))
            for v in filter(lambda v: v is not None, acheteur.ventes)
        },
        "Retour": lambda: acheteur_action_selection_menu(acheteur),
    }

    choice = select(
        f"You can see & manage your tickets here {acheteur.nom.capitalize()}",
        choices=list(ACHETEUR_VENTES_SELECTION_CHOICES.keys()),
    )

    ACHETEUR_VENTES_SELECTION_CHOICES[choice]()
