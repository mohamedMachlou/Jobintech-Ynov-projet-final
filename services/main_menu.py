from utils.inputs import select


# TODO: attach to the functions
MAIN_MENU_CHOICES = {
    "Gestion des événements": lambda: print("Événements logic here..."),
    "Gestion des utilisateurs": lambda: print("Utilisateurs logic here..."),
    "Quitter": lambda: exit(0),
}


def main_menu():
    choice = select(
        " ",
        choices=list(MAIN_MENU_CHOICES.keys()),
    )

    MAIN_MENU_CHOICES[choice]()
