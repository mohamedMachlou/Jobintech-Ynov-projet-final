from utils.inputs import select, input
from validations.evenement import (
    validate_chaine,
    validate_date,
    validate_float,
    validate_int
)
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

    # Choix du type d'événement
    choix = select("Choisir le type d'événement :", ["Concert", "Conférence"])

    print('Ajout d\'event works ')

    # Saisie des informations avec validations correctes
    titre = input("Taper le Titre d'Evenement", validate=validate_chaine)

    date_event = input(
        "Date du concert (YYYY-MM-DD)",
        validate=lambda d: validate_date(d, future_only=True)
    )

    lieu = input("Lieu du concert", validate=validate_chaine)
    prix_base = input("Prix de base", validate=validate_float)
    capacite = input("Capacité", validate=validate_int)
    artiste = input("Artiste", validate=validate_chaine)

    # Création de l'événement selon le type choisi
    if choix == "Concert":
        ajout_nouveau_concert(titre, date_event, lieu, prix_base, capacite, artiste)
    elif choix == "Conférence":
        conférencier = input("Nom du conférencier", validate=validate_chaine)
        ajout_nouvelle_conference(titre, date_event, lieu, capacite, conférencier)









