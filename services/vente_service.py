from models.acheteur import Acheteur
from models.vente import Vente
from utils import select


def acheteur_vente_action_selection_menu(vente: Vente):
    # TODO: manage options here
    print(vente)
    pass


def list_achateur_ventes_menu(acheteur: Acheteur):
    from services.acheteur_service import acheteur_action_selection_menu

    print("here guys in the list ach ventes")

    ACHETEUR_VENTES_SELECTION_CHOICES = {
        **{
            v.__str__: (lambda v=v: acheteur_vente_action_selection_menu(v))
            for v in filter(lambda v: v is not None, acheteur.ventes)
        },
        "Retour": lambda: acheteur_action_selection_menu(acheteur),
    }
    print("before choosing", ACHETEUR_VENTES_SELECTION_CHOICES.keys())
    choice = select(
        f"You can see & manage your tickets here {acheteur.nom.capitalize()}",
        choices=list(ACHETEUR_VENTES_SELECTION_CHOICES.keys()),
    )

    print("you've chosen", choice)

    ACHETEUR_VENTES_SELECTION_CHOICES[choice]()
