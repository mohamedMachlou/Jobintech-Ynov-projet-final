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


MAIN_MENU_CHOICES = {
    "Gestion des événements": gestion_evenements_menu,
    "Faire des achats": lambda: print("TODO: for ventes"),
    "Quitter": lambda: exit(0),
}


GESTION_EVENEMENTS_CHOICES = {
    "Gestion des Concerts": lambda: print("TODO: for concert"),
    "Gestion des ": lambda: print("TODO: for conferences"),
    "Gestion des utilisateurs": lambda: print("Utilisateurs logic here..."),
    "Retour": main_menu,
}
