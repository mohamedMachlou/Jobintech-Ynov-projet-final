from models.billet import Billet
from validations.billet import validate_billet_data
from datetime import datetime

# Ajouter un billet
def ajout_nouveau_billet(titre, date_event, lieu, prix_base, type_billet, capacite=1):
    errors = validate_billet_data(titre, date_event, lieu, prix_base, type_billet)
    if errors:
        print("Erreur de validation :", errors)
        return None

    new_billet = Billet(titre, date_event, lieu, prix_base, type_billet, capacite)
    print("Billet ajouté avec succès !")
    return new_billet

# Mettre à jour un billet
def update_billet(id_billet, date_event=None, lieu=None):
    billet_to_update = next(
        (b for b in Billet.billets if b.id_evenement == id_billet),
        None
    )
    if billet_to_update:
        if date_event:
            billet_to_update.date = date_event
        if lieu:
            billet_to_update.lieu = lieu
        billet_to_update._sync()
        print(f"Billet ID [{id_billet}] mis à jour !")
        return billet_to_update
    else:
        print(f"Aucun billet trouvé avec ID [{id_billet}] !")
        return None

# Supprimer un billet
def delete_billet(id_billet):
    billet_to_delete = next(
        (b for b in Billet.billets if b.id_evenement == id_billet),
        None
    )
    if billet_to_delete:
        billet_to_delete.delete()
        print(f"Billet ID [{id_billet}] supprimé !")
        return True
    else:
        print(f"Aucun billet trouvé avec ID [{id_billet}] !")
        return False
