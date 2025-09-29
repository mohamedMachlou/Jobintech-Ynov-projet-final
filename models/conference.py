from evenement import Evenement


class Conference(Evenement):
    def __init__(
        self,
        id_evenement: int,
        titre: str,
        date: str,
        lieu: str,
        capacite: int,
        places_vendues: int,
        orateur: str,
    ):
        super().__init__(id_evenement, titre, date, lieu, capacite)
        self.orateur = orateur
        self.places_vendues = places_vendues
