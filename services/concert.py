from ..models.concert import Concert

# l'Ajout d'un nouveau concert
def ajout_nouveau_concert(id_evenement, titre, date, lieu, capacite, artiste):
    new_concert = Concert(id_evenement, titre, date, lieu, capacite, artiste)
    Concert.toutes_concerts.append(new_concert)
    return new_concert


# Mis à jour un concert
def update_concert(id_evenement, date, lieu):
    concert_to_update = next((concert for concert in Concert.toutes_concerts if concert.id_evenement == id_evenement), None)

    if concert_to_update is not None:
        concert_to_update.date = date
        concert_to_update.lieu = lieu
        return concert_to_update
    else:
        print(f'Aucun concert trouvé avec ID d\'Evenement [{id_evenement}]!')
        return None



# Supprimer un concert
def delete_concert(id_evenement):
    nombre_initial = len(Concert.toutes_concerts)
    Concert.toutes_concerts = [concert for concert in Concert.toutes_concerts if concert.id_evenement != id_evenement]

    if nombre_initial > len(Concert.toutes_concerts):
        print(f'l\'Evenement d\'ID: [{id_evenement}] a été supprimé!')
        return True
    else:
        print(f'Aucun concert trouvé avec ID d\'Evenement [{id_evenement}]!')
        return False