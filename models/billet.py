from typing import Optional
from .evenement import Evenement

class Billet(Evenement):
    BILLET_TYPE = {"Standard": 1.0, "VIP": 1.5}  # Coefficients de prix

    def __init__(
        self,
        titre: str,
        date_event,
        lieu: str,
        prix_base: int,
        type_billet: str,
        capacite: int = 1,
        _id: Optional[int] = None,
        places_vendues: Optional[int] = None,
    ):
        if type_billet not in Billet.BILLET_TYPE:
            raise ValueError(
                f"Type de billet invalide : {type_billet}. Choisir entre {list(Billet.BILLET_TYPE.keys())}"
            )

        self.type_billet = type_billet
        self.prix = prix_base * Billet.BILLET_TYPE[type_billet]
        super().__init__(titre, date_event, lieu, prix_base, capacite, _id, places_vendues)

    def __str__(self):
        return super().__str__() + f" - Type: {self.type_billet}, Prix: {self.prix}"
