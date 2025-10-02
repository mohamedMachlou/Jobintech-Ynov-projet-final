from utils.inputs import select


def gestion_evenements_menu():
    from services.main import main_menu

    GESTION_EVENEMENTS_CHOICES = {
        "Gestion des Concerts": lambda: print("TODO: for concert"),
        "Gestion des Conferences": lambda: print("TODO: for conferences"),
        "Retour": main_menu,
    }
    choice = select(
        " ",
        choices=list(GESTION_EVENEMENTS_CHOICES.keys()),
    )

    GESTION_EVENEMENTS_CHOICES[choice]()





