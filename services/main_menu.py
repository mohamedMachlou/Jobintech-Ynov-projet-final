from services.acheteur import acheteur_registration, acheteur_user_selection
from utils.inputs import select


def main_menu():
    choice = select(
        " ",
        choices=list(MAIN_MENU_CHOICES.keys()),
    )

    MAIN_MENU_CHOICES[choice]()


def gestion_evenements_menu():
    choice = select(
        " ",
        choices=list(GESTION_EVENEMENTS_CHOICES.keys()),
    )

    GESTION_EVENEMENTS_CHOICES[choice]()


def faire_des_achats_menu():
    choice = select(
        " ",
        choices=list(FAIRE_ACHATS_CHOICES.keys()),
    )

    FAIRE_ACHATS_CHOICES[choice]()


MAIN_MENU_CHOICES = {
    "Gestion des événements": gestion_evenements_menu,
    "Faire des achats": faire_des_achats_menu,
    "Quitter": lambda: exit(0),
}


GESTION_EVENEMENTS_CHOICES = {
    "Gestion des Concerts": lambda: print("TODO: for concert"),
    "Gestion des ": lambda: print("TODO: for conferences"),
    "Gestion des utilisateurs": lambda: print("Utilisateurs logic here..."),
    "Retour": main_menu,
}

FAIRE_ACHATS_CHOICES = {
    "Nouveau Acheteur": acheteur_registration,
    "Acheteur Existant": acheteur_user_selection,
    "Retour": main_menu,
}
