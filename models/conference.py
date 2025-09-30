from typing import Optional
from models.evenement import Evenement


class Conference(Evenement):
    def __init__(
        self,
        titre: str,
        date: str,
        lieu: str,
        capacite: int,
        orateur_principal: str,
        _id: Optional[int] = None,
        places_vendues: Optional[int] = None,
    ):
        self.orateur_principal = orateur_principal
        super().__init__(titre, date, lieu, capacite, _id, places_vendues)

    def __str__(self):
        return super().__str__() + f" - Orateur: {self.orateur_principal}"
