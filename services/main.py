from services.acheteur_service import faire_des_achats_menu
from services.evenement_service import gestion_evenements_menu
from services.rapport_service import generer_rapport_financier_et_frequentation
from utils.clear import clear
from utils.inputs import select


def main_menu():
    MAIN_MENU_CHOICES = {
        "Gestion des événements": gestion_evenements_menu,
        "Faire des achats": faire_des_achats_menu,
        "Analyse et Rapports": generer_rapport_financier_et_frequentation,
        "Clear Screen": lambda: clear() and main_menu(),
        "Quitter": exit
    }

    choice = select(
        " ",
        choices=list(MAIN_MENU_CHOICES.keys()),
    )

    MAIN_MENU_CHOICES[choice]()
