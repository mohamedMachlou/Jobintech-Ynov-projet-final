from services.acheteur import faire_des_achats_menu
from services.evenements import gestion_evenements_menu
from utils.inputs import select


def main_menu():
    MAIN_MENU_CHOICES = {
        "Gestion des événements": gestion_evenements_menu,
        "Faire des achats": faire_des_achats_menu,
        "Quitter": lambda: exit(0),
    }

    choice = select(
        " ",
        choices=list(MAIN_MENU_CHOICES.keys()),
    )

    MAIN_MENU_CHOICES[choice]()
