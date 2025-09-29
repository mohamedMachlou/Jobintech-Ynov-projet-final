from models import concert
Concert = concert.Concert

# l'Ajout d'un nouveau concert
def ajout_nouveau_concert(id_evenement, titre, date, lieu, capacite, artiste):
    new_concert = Concert(id_evenement, titre, date, lieu, capacite, artiste)
    Concert.toutes_concerts.append(new_concert)
    return new_concert


# Mis à jour de concert
def update_concert(id_evenement, titre, date, lieu, capacite, artiste):
    concert_to_update = next((concert for concert in Concert.toutes_concerts if concert.id_evenement == id_evenement), None)

    if concert_to_update is not None:
        concert_to_update.date = date
        concert_to_update.lieu = lieu
        return concert_to_update
    else:
        print(f'Aucun concert trouvé avec ID d\'Eveinement [{id_evenement}]!')



# Supprimer d'un concert
def delete_concert(id_evenement):
    concert_to_detele = next((concert for concert in Concert.toutes_concerts if concert.id_evenement == id_evenement), None)

    if concert_to_detele is not None:
        Concert.toutes_concerts = [concert for concert in Concert.toutes_concerts if concert.id_evenement != id_evenement]
    else:
        print(f'Aucun concert trouvé avec ID d\'Eveinement [{id_evenement}]!')