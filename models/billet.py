from json import JSONDecodeError, dump, load
from typing import Optional

from utils.logger import error


class Billet:
    billets = []  # liste pour stocker tous les billets créés
    _id = 1

    # Coefficients de prix par type
    BILLET_TYPE = {"Standard": 1.0, "VIP": 1.5}  # Prix normal  # +50% du prix

    def __init__(self, prix_base, type_billet, _id: Optional[int] = None):
        if type_billet not in Billet.BILLET_TYPE:
            raise ValueError(
                f"Type de billet invalide : {type_billet}. Choisir entre {list(Billet.BILLET_TYPE.keys())}"
            )

        self.id_billet = self._id if _id is None else _id
        self.type_billet = type_billet
        # Appliquer le coefficient de prix selon le type
        self.prix_base = prix_base
        self.prix = prix_base * Billet.BILLET_TYPE[type_billet]
        Billet._id += 1
        # Sauvegarde dans la liste globale des billets
        Billet.billets.append(self)
        self._sync()

    @staticmethod
    def get_prix(type_billet, prix_base):
        """Retourne le prix d’un billet selon son type sans créer d'objet"""
        coeff = Billet.BILLET_TYPE.get(type_billet, None)
        if coeff is None:
            raise ValueError(f"Type de billet invalide : {type_billet}.")
        return prix_base * coeff

    def delete(self):
        Billet.billets.remove(self)
        self._sync()

    @classmethod
    def _sync(cls):
        with open("storage/billets.json", "w+") as f:
            dump(
                list(map(lambda a: a.__dict__, cls.billets)),
                f,
                indent=4,
                ensure_ascii=False,
            )

    @classmethod
    def _load(cls):
        try:
            with open("storage/billets.json") as f:
                cls.billets = list(
                    sorted(
                        map(
                            lambda b: Billet(b["prix_base"], b["type_billet"], b["id_billet"]),
                            load(f),
                        ),
                        key=lambda a: a.id_billet,
                    )
                )
                max_id = (
                    0
                    if (
                        max_id_element := max(
                            cls.billets, default=None, key=lambda a: a.id_billet
                        )
                    )
                    is None
                    else max_id_element.id_billet
                )

                cls._id = max_id + 1

        except (JSONDecodeError, TypeError, KeyError):
            error(
                "Error while trying to load json data, the program is using empty data for now"
            )

        except FileNotFoundError:
            pass


Billet._load()
