from datetime import datetime as Datetime
from logging import error
from models.acheteur import Acheteur
from models.billet import Billet
from models.evenement import Evenement
from models import Vente
from utils import input, select
from utils.logger import error, success
from validations.vente import validate_buy_ticket_qty


def acheteur_vente_action_selection_menu(vente: Vente):
    # TODO: manage options here
    print(vente)
    pass


def make_a_vente_action_menu(acheteur: Acheteur, evenement: Evenement):
    if not evenement.places_restantes > 0:
        error("There is no available tickets, please select another event...")
        return make_a_vente_menu(acheteur)

    TICKET_TYPE_CHOICES = {
        **{
            f"{t} ({Billet.BILLET_TYPE[t] * evenement.prix_base} per ticket)": t
            for t in Billet.BILLET_TYPE.keys()
        },
    }

    type_billet_choice = select(
        "Select type of your ticket",
        choices=list(TICKET_TYPE_CHOICES.keys()),
    )

    type_billet = TICKET_TYPE_CHOICES[type_billet_choice]

    qty = input(
        "How much ticket do you want to buy",
        validate=lambda qty: validate_buy_ticket_qty(qty, evenement.places_restantes),
    )

    vente = Vente(evenement.id_evenement, acheteur.id_acheteur, type_billet, int(qty))

    success(
        f"Tickets #{vente.id_vente} bought succesffully with total of {vente.prix_total}"
    )

    return make_a_vente_menu(acheteur)


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
