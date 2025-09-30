from typing import Optional
from models.evenement import Evenement


class Concert(Evenement):
    def __init__(
        self,
        titre: str,
        date: str,
        lieu: str,
        capacite: int,
        artiste: str,
        _id: Optional[int] = None,
        places_vendues: Optional[int] = None,
    ):
        self.artiste = artiste
        super().__init__(titre, date, lieu, capacite, _id, places_vendues)

    def __str__(self):
        return super().__str__() + f" - Artiste: {self.artiste}"
