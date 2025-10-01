from models.conference import Conference
from validations.conference import validate_conference_data


# Ajout d'une nouvelle conférence
def ajout_nouvelle_conference(titre, date, lieu, prix_base, capacite, orateur_principal):
    errors = validate_conference_data(titre, date, lieu, prix_base, capacite, orateur_principal)
    if errors:
        print("Erreur de validation :", errors)
        return None

    new_conf = Conference(titre, date, lieu, prix_base, capacite, orateur_principal)
    print("Ajout de conférence réussi !")
    return new_conf


# Mise à jour d'une conférence
def update_conference(id_evenement, date=None, lieu=None, orateur_principal=None):
    conf_to_update = next(
        (conf for conf in Conference.evenements if conf.id_evenement == id_evenement),
        None
    )

    if conf_to_update is not None:
        if date:
            conf_to_update.date = date
        if lieu:
            conf_to_update.lieu = lieu
        if orateur_principal:
            conf_to_update.orateur_principal = orateur_principal
        conf_to_update._sync()
        print(f"Conférence [{id_evenement}] mise à jour avec succès !")
        return conf_to_update
    else:
        print(f"Aucune conférence trouvée avec ID [{id_evenement}] !")
        return None


# Supprimer une conférence
def delete_conference(id_evenement):
    conf_to_delete = next(
        (conf for conf in Conference.evenements if conf.id_evenement == id_evenement),
        None
    )
    if conf_to_delete:
        conf_to_delete.delete()
        print(f"Conférence d'ID [{id_evenement}] supprimée !")
        return True
    else:
        print(f"Aucune conférence trouvée avec ID [{id_evenement}] !")
        return False
