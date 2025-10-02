from typing import Optional
from .evenement import Evenement

class Billet(Evenement):
    BILLET_TYPE = {"Standard": 1.0, "VIP": 1.5}  # Coefficients de prix

    def __init__(
        self,
        titre: str,
        date_event,
        lieu: str,
        prix_base: float,
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

    @staticmethod
    def get_prix(type_billet, prix_base):
        """Retourne le prix d’un billet selon son type sans créer d'objet"""
        coeff = Billet.BILLET_TYPE.get(type_billet, None)
        if coeff is None:
            raise ValueError(f"Type de billet invalide : {type_billet}.")
        return prix_base * coeff

    def __str__(self):
        return super().__str__() + f" - Type: {self.type_billet}, Prix: {self.prix}"
