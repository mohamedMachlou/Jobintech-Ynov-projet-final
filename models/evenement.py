# la classe Evenement
class Evenement:
    def __init__(self, id_evenement, titre, date, lieu, capacite):
        self.id_evenement = id_evenement
        self.titre = titre
        self.date = date
        self.lieu = lieu
        self.capacite = capacite
        self.places_vendues = 0


