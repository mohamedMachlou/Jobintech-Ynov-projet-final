import datetime
from models import Evenement
from models import Concert, Conference
from dateutil.parser import parse
from utils.inputs import select, input
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






def gestion_evenements_menu():
    from services.main import main_menu

    GESTION_EVENEMENTS_CHOICES = {
        "Recherche des Evenements": lambda: print("TODO: recherche globale"),
        "Ajouter un Evenement": ajouter_evenement_menu,
        "Mis à jour un Evenement": maj_evenement_menu,
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

    from dateutil.parser import parse

    date_event_str = input(
        "Date du concert (YYYY-MM-DD)",
        validate=lambda d: validate_date(d, future_only=True)
    )

    # Convertir en objet datetime
    date_event = parse(date_event_str)

    lieu = input("Lieu du concert", validate=validate_chaine)
    prix_base = input("Prix de base", validate=validate_float)
    capacite = input("Capacité", validate=validate_int)

    # Création de l'événement selon le type choisi
    if choix == "Concert":
        print('choix de concert')
        artiste = input("Artiste", validate=validate_chaine)
        Concert(titre, date_event, lieu, prix_base, capacite, artiste)
    elif choix == "Conférence":
        print('choix de conference')
        conférencier = input("Nom du conférencier", validate=validate_chaine)
        Conference(titre, date_event, lieu,prix_base, capacite, conférencier)

    gestion_evenements_menu()



def maj_evenement_menu():
    # Choix du mode de recherche
    mode_recherche = select("Rechercher l'événement par :", ["ID", "Titre"])

    evenement = None

    if mode_recherche == "ID":
        identifiant = int(input(
            "Saisir l'ID de l'événement : ",
            validate=lambda x: x.isdigit() or "Veuillez entrer un entier"
        ))
        evenement = next((e for e in Evenement.evenements if e.id_evenement == identifiant), None)
    else:
        while True:
            titre_recherche = input(
                "Saisir le titre de l'événement : ",
                validate=validate_chaine
            ).lower()

            # Recherche partielle insensible à la casse
            evenements_trouves = [
                e for e in Evenement.evenements if titre_recherche in e.titre.lower()
            ]

            total_trouves = len(evenements_trouves)
            if total_trouves == 0:
                print("Aucun événement trouvé avec ce titre. Veuillez réessayer.")
                continue

            print(f"{total_trouves} événement(s) trouvé(s) correspondant à '{titre_recherche}':")

            # Afficher au maximum 5 événements
            for e in evenements_trouves[:5]:
                print(f"ID {e.id_evenement} | {e.titre} | {e.date.date()} | {e.lieu}")

            if total_trouves == 1:
                evenement = evenements_trouves[0]
                break

            # Demander à l'utilisateur de préciser avec l'ID
            identifiant = int(input(
                "Plusieurs événements correspondent, tapez l'ID exact de l'événement souhaité : ",
                validate=lambda x: x.isdigit() or "Veuillez entrer un entier"
            ))
            evenement = next((e for e in evenements_trouves if e.id_evenement == identifiant), None)
            if evenement:
                break
            else:
                print("ID invalide, veuillez réessayer.")

    # Vérification
    if not evenement:
        print("Événement introuvable !")
        return

    print(f"Événement trouvé : {evenement}")

    # Saisie des nouvelles valeurs
    nouvelle_date_str = input(
        f"Nouveau date (laisser vide pour conserver {evenement.date.date()}): ",
        validate=lambda d: True if d.strip() == "" else validate_date(d, future_only=True)
    )
    nouvelle_lieu = input(
        f"Nouveau lieu (laisser vide pour conserver '{evenement.lieu}'): ",
        validate=lambda val: True if val.strip() == "" else validate_chaine(val)
    )

    # Mise à jour
    if nouvelle_date_str.strip():
        evenement.date = parse(nouvelle_date_str)
    if nouvelle_lieu.strip():
        evenement.lieu = nouvelle_lieu

    # Sauvegarde
    Evenement._sync()

    print(f"Événement '{evenement.titre}' mis à jour avec succès !")

    gestion_evenements_menu()







