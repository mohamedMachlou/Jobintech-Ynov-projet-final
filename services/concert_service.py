from models.concert import Concert
from validations.concert import validate_concert_data

# Ajout d'un nouveau concert
def ajout_nouveau_concert(titre, date, lieu,prix_base, capacite, artiste):
    # errors = validate_concert_data(titre, date, lieu,prix_base, capacite, artiste)
    # if errors:
    #     print("Erreur de validation :", errors)
    #     return None

    new_concert = Concert(titre, date, lieu,prix_base, capacite, artiste)
    print("Ajout réussi !")
    return new_concert

# Mise à jour d'un concert
def update_concert(id_evenement, date, lieu):
    concert_to_update = next(
        (concert for concert in Concert.concerts if concert.id_evenement == id_evenement),
        None
    )

    if concert_to_update is not None:
        # petite validation simple pour la mise à jour
        if date:
            concert_to_update.date = date
        if lieu:
            concert_to_update.lieu = lieu
        concert_to_update._sync()
        return concert_to_update
    else:
        print(f"Aucun concert trouvé avec ID [{id_evenement}] !")
        return None

# Supprimer un concert
def delete_concert(id_evenement):
    concert_to_delete = next(
        (concert for concert in Concert.concerts if concert.id_evenement == id_evenement),
        None
    )
    if concert_to_delete:
        concert_to_delete.delete()
        print(f"Evenement d'ID [{id_evenement}] supprimé !")
        return True
    else:
        print(f"Aucun concert trouvé avec ID [{id_evenement}] !")
        return False
