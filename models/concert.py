<<<<<<< HEAD
from models import Evenement

class Concert(Evenement):

    # Fonction d'initialisation de Concert
    def __init__(self, id_evenement: int, titre: str, date: str, lieu: str, capacite: int, artiste: str):
        super().__init__(id_evenement, titre, date, lieu, capacite)
=======
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
>>>>>>> 1b98091c6d7ba2ad2f09dfc8d484efe2b4aa6c28
        self.artiste = artiste
        super().__init__(titre, date, lieu, capacite, _id, places_vendues)


    def __str__(self):
        return super().__str__() + f" - Artiste: {self.artiste}"
