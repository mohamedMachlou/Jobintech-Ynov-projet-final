from json import JSONDecodeError, dump, load
from typing import Optional


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
                    )
                )
        except JSONDecodeError:
            print(
                "[!] Error while trying to load json data, the program is using empty data for now"
            )

        except FileNotFoundError:
            pass


Acheteur._load()
