
# classe Conference
class Conference:
    def __init__(self, id_evenement, titre, date, lieu, capacite, places_vendues, orateur_principal):
        super().__init__(id_evenement, titre, date, lieu, capacite, places_vendues)
        self.orateur_principal = orateur_principal
