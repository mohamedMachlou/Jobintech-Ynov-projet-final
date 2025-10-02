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






def gestion_evenements_menu():
    from services.main import main_menu

    GESTION_EVENEMENTS_CHOICES = {
        "Ajouter un Evenement": ajouter_evenement_menu,
        "Recherche des Evenements": recherche_evenements_par_personne,
        "Lister des Evenements": lister_evenements,
        "Mis à jour un Evenement": maj_evenement_menu,
        "Annuler un Evenement": annuler_evenement_menu,
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
    while True:  # boucle jusqu'à ce qu'un événement valide soit trouvé
        # Choix du mode de recherche
        mode_recherche = select("Rechercher l'événement par :", ["ID", "Titre"])
        evenement = None

        if mode_recherche == "ID":
            while True:
                identifiant = input(
                    "Saisir l'ID de l'événement : ",
                    validate=lambda x: x.isdigit() or "Veuillez entrer un entier"
                )
                identifiant = int(identifiant)

                evenement = next((e for e in Evenement.evenements if e.id_evenement == identifiant), None)
                if evenement:
                    break
                else:
                    print(" Aucun événement trouvé avec cet ID, veuillez réessayer.")
            # fin recherche par ID

        else:  # Recherche par Titre
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
                    print(" Aucun événement trouvé avec ce titre. Veuillez réessayer.")
                    continue

                print(f"{total_trouves} événement(s) trouvé(s) correspondant à '{titre_recherche}':")

                # Afficher au maximum 5 événements
                for e in evenements_trouves[:5]:
                    print(f"ID {e.id_evenement} | {e.titre} | {e.date.date()} | {e.lieu}")

                if total_trouves == 1:
                    evenement = evenements_trouves[0]
                    break

                # Demander à l'utilisateur de préciser avec l'ID
                identifiant = input(
                    "Plusieurs événements correspondent, tapez l'ID exact de l'événement souhaité : ",
                    validate=lambda x: x.isdigit() or "Veuillez entrer un entier"
                )
                identifiant = int(identifiant)

                evenement = next((e for e in evenements_trouves if e.id_evenement == identifiant), None)
                if evenement:
                    break
                else:
                    print(" ID invalide, veuillez réessayer.")

        # Si un événement a été trouvé on sort de la boucle principale
        if evenement:
            break

    # Vérification finale
    print(f" Événement trouvé : {evenement}")

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

    print(f" Événement '{evenement.titre}' mis à jour avec succès !")

    # Retour au menu principal
    return gestion_evenements_menu()





def recherche_evenements_par_personne():
    while True:
        # Choix du type de recherche
        choix = select("Rechercher par :", ["Artiste", "Conférencier", "Retour au menu"])
        if choix == "Retour au menu":
            return gestion_evenements_menu()

        recherche_str = input(f"Saisir le nom {choix.lower()} : ", validate=validate_chaine).lower()

        # Récupération des événements correspondants
        evenements_trouves = []
        for e in Evenement.evenements:
            if choix == "Artiste" and hasattr(e, "artiste"):
                if recherche_str in e.artiste.lower():
                    evenements_trouves.append(e)
            elif choix == "Conférencier" and hasattr(e, "orateur_principal"):
                if recherche_str in e.orateur_principal.lower():
                    evenements_trouves.append(e)

        if not evenements_trouves:
            print(f"Aucun événement trouvé pour {choix.lower()} contenant '{recherche_str}'.\nVeuillez réessayer.")
            continue  # Reboucle pour redemander le type de recherche

        total_trouves = len(evenements_trouves)
        print(f"{total_trouves} événement(s) trouvé(s) correspondant à '{recherche_str}'.")

        # Pagination pour afficher 10 événements max à la fois
        page_size = 10
        page = 0

        while True:
            start = page * page_size
            end = start + page_size
            page_evenements = evenements_trouves[start:end]

            for e in page_evenements:
                pers = getattr(e, "artiste" if choix == "Artiste" else "orateur_principal")
                print(f"ID {e.id_evenement} | {e.titre} | {pers} | {e.date.date()} | {e.lieu}")

            # Vérification s'il y a plus de pages
            if end >= total_trouves:
                print("Fin des résultats.\n")
                break

            # Proposer la navigation
            action = select(
                "Que voulez-vous faire ?",
                ["Afficher les 10 prochains", "Retour au menu"]
            )
            if action == "Afficher les 10 prochains":
                page += 1
            else:
                break

        # Une fois la recherche terminée, retour automatique au menu principal
        return gestion_evenements_menu()



def lister_evenements():
    total = len(Evenement.evenements)

    if total == 0:
        print(" Aucun événement trouvé.")
        return gestion_evenements_menu()

    print(f"\n Nombre total d'événements : {total}\n")

    page = 0
    taille_page = 10

    while True:
        start = page * taille_page
        end = start + taille_page
        sous_liste = Evenement.evenements[start:end]

        # Affichage
        for e in sous_liste:
            print(f"ID {e.id_evenement} | {e.titre} | {e.date.date()} | {e.lieu}")

        # Vérifier si fin de la liste
        if end >= total:
            print("\n Fin de la liste des événements.")
            break

        # Options pour l'utilisateur
        choix = select(
            "\nQue voulez-vous faire ?",
            ["Voir les 10 suivants", "Retour au menu"]
        )

        if choix == "Voir les 10 suivants":
            page += 1
        else:
            return gestion_evenements_menu()

    # Retour auto au menu une fois tout affiché
    return gestion_evenements_menu()






def annuler_evenement_menu():
    while True:  # boucle jusqu'à ce qu'un événement valide soit trouvé
        # Choix du mode de recherche
        mode_recherche = select("Rechercher l'événement à annuler par :", ["ID", "Titre"])
        evenement = None

        if mode_recherche == "ID":
            while True:
                identifiant = input(
                    "Saisir l'ID de l'événement : ",
                    validate=lambda x: x.isdigit() or "Veuillez entrer un entier"
                )
                identifiant = int(identifiant)

                evenement = next((e for e in Evenement.evenements if e.id_evenement == identifiant), None)
                if evenement:
                    break
                else:
                    print(" Aucun événement trouvé avec cet ID, veuillez réessayer.")

        else:  # Recherche par Titre
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
                    print(" Aucun événement trouvé avec ce titre. Veuillez réessayer.")
                    continue

                print(f"{total_trouves} événement(s) trouvé(s) correspondant à '{titre_recherche}':")

                # Afficher au maximum 5 événements
                for e in evenements_trouves[:5]:
                    print(f"ID {e.id_evenement} | {e.titre} | {e.date.date()} | {e.lieu}")

                if total_trouves == 1:
                    evenement = evenements_trouves[0]
                    break

                # Demander à l'utilisateur de préciser avec l'ID
                identifiant = input(
                    "Plusieurs événements correspondent, tapez l'ID exact de l'événement souhaité : ",
                    validate=lambda x: x.isdigit() or "Veuillez entrer un entier"
                )
                identifiant = int(identifiant)

                evenement = next((e for e in evenements_trouves if e.id_evenement == identifiant), None)
                if evenement:
                    break
                else:
                    print(" ID invalide, veuillez réessayer.")

        # Si un événement a été trouvé on sort de la boucle principale
        if evenement:
            break

    # Vérification finale
    print(f"\n Événement trouvé : {evenement}\n")

    # Confirmation avant suppression
    confirmation = select(
        f"Voulez-vous vraiment annuler (supprimer) l'événement '{evenement.titre}' ?",
        ["Oui", "Non"]
    )

    if confirmation == "Oui":
        Evenement.evenements.remove(evenement)
        Evenement._sync()
        print(f" Événement '{evenement.titre}' supprimé avec succès !")
    else:
        print(" Annulation de la suppression, l'événement reste inchangé.")

    # Retour au menu principal
    return gestion_evenements_menu()





