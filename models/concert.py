from typing import Optional
from .evenement import Evenement
from datetime import datetime as DatetimeType


class Concert(Evenement):
    def __init__(
        self,
        titre: str,
        date_event: DatetimeType,
        lieu: str,
        prix_base: int,
        capacite: int,
        artiste: str,
        _id: Optional[int] = None,
        places_vendues: Optional[int] = None,
    ):
        self.artiste = artiste
        super().__init__(titre, date_event, lieu, prix_base, capacite, _id, places_vendues)

    def __str__(self):
        return super().__str__() + f" - Artiste: {self.artiste}"

