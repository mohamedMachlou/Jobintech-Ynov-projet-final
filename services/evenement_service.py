# from utils.inputs import select
from validations.evenement import (
    validate_chaine,
    validate_date,
    validate_float,
    validate_int
)


#
#
# def gestion_evenements_menu():
#     from services.main import main_menu
#
#     GESTION_EVENEMENTS_CHOICES = {
#         "Recherche des Evenements": lambda: print("TODO: for concert"),
#         "Ajouter un Evenement": lambda: print("TODO: for conferences"),
#         "Mis à jour un Evenement": lambda: print("TODO: for conferences"),
#         "Annuler un Evenement": lambda: print("TODO: for conferences"),
#         "Retour": main_menu,
#     }
#     choice = select(
#         " ",
#         choices=list(GESTION_EVENEMENTS_CHOICES.keys()),
#     )
#
#     GESTION_EVENEMENTS_CHOICES[choice]()



from utils.inputs import select
from services.concert_service import (
    ajout_nouveau_concert,
    update_concert,
    delete_concert
)
from services.conference_service import (
    ajout_nouvelle_conference,
    update_conference,
    delete_conference
)


def gestion_evenements_menu():
    from services.main import main_menu

    GESTION_EVENEMENTS_CHOICES = {
        "Recherche des Evenements": lambda: print("TODO: recherche globale"),
        "Ajouter un Evenement": ajouter_evenement_menu,
        # "Mis à jour un Evenement": maj_evenement_menu,
        # "Annuler un Evenement": annuler_evenement_menu,
        "Retour": main_menu,
    }
    choice = select(
        " ",
        choices=list(GESTION_EVENEMENTS_CHOICES.keys()),
    )
    GESTION_EVENEMENTS_CHOICES[choice]()


# sous-menus spécialisés
def ajouter_evenement_menu():


    titre = input("Taper le Titre d'Evenement",alidate=lambda titre: validate_chaine)
    date = input("Date du concert (YYYY-MM-DD)", validate=validate_date)
    lieu = input("Lieu du concert", validate=validate_chaine)
    prix_base = input("Prix de base", validate=validate_float)
    capacite = input("Capacité", validate=validate_int)
    artiste = input("Artiste", validate=validate_chaine)


    choix = select("Choisir le type d'événement :", ["Concert", "Conférence"])
    if choix == "Concert":
        ajout_nouveau_concert(titre, date, lieu, prix_base, capacite, artiste)


    elif choix == "Conférence":
        pass








