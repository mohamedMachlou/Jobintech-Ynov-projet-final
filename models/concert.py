# classe Concert
from evenement import Evenement


class Concert(Evenement):
    def __init__(self, id_evenement, titre, date, lieu, capacite, places_vendues, artiste):
        super().__init__(id_evenement, titre, date, lieu, capacite, places_vendues)
        self.artiste = artiste