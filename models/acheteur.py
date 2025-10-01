from json import JSONDecodeError, dump, load
from typing import Optional

from models.vente import Vente
from utils.logger import error


class Acheteur:
    achateurs = []
    _id = 1

    def __init__(self, nom: str, email: str, _id: Optional[int] = None):
        self.id_acheteur = self._id if _id is None else _id
        self.nom = nom
        self.email = email
        Acheteur.achateurs.append(self)
        Acheteur._id += 1
        self._sync()

    def delete(self):
        Acheteur.achateurs.remove(self)
        self._sync()

    @property
    def ventes(self):
        return list(
            filter(
                lambda v: getattr(v.acheteur, "id_acheteur", None) == self.id_acheteur,
                Vente.ventes,
            )
        )

    @classmethod
    def _sync(cls):
        with open("storage/acheteurs.json", "w+") as f:
            dump(
                list(map(lambda a: a.__dict__, cls.achateurs)),
                f,
                indent=4,
                ensure_ascii=False,
            )

    @classmethod
    def _load(cls):
        try:
            with open("storage/acheteurs.json") as f:
                cls.achateurs = list(
                    map(
                        lambda a: Acheteur(a["nom"], a["email"], a["id_acheteur"]),
                        load(f),
                    ),
                )
                max_id = (
                    0
                    if (
                        max_id_element := max(
                            cls.achateurs, default=None, key=lambda a: a.id_acheteur
                        )
                    )
                    is None
                    else max_id_element.id_acheteur
                )

                cls._id = max_id + 1

        except (JSONDecodeError, TypeError, KeyError):
            error(
                "Error while trying to load json data, the program is using empty data for now"
            )

        except FileNotFoundError:
            pass
