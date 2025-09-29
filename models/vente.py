from json import JSONDecodeError, dump, load
from typing import Optional
from utils.logger import error
from models.billet import Billet


class Vente:
    ventes = []
    _id = 1

    def __init__(
        self,
        id_evenement,
        id_acheteur,
        type_billet,
        quantite,
        id_vente: Optional[int] = None,
    ):
        self.id_vente = self._id if id_vente is None else id_vente
        self.id_evenement = id_evenement
        self.id_acheteur = id_acheteur
        self.type_billet = type_billet
        self.quantite = quantite
        self.prix_total = Billet.get_prix(type_billet, 0) * quantite
        Vente._id += 1
        Vente.ventes.append(self)
        self._sync()

    def delete(self):
        if self in Vente.ventes:
            Vente.ventes.remove(self)
            self._sync()

    @classmethod
    def _sync(cls):
        with open("storage/ventes.json", "w+", encoding="utf-8") as f:
            dump([v.__dict__ for v in cls.ventes], f, indent=4, ensure_ascii=False)

    @classmethod
    def _load(cls):
        try:
            with open("storage/ventes.json", "r", encoding="utf-8") as f:
                cls.ventes = [
                    Vente(
                        v["id_evenement"],
                        v["id_acheteur"],
                        v["type_billet"],
                        v["quantite"],
                        v["id_vente"],
                    )
                    for v in load(f)
                ]
                max_id = (
                    0
                    if (
                        max_obj := max(
                            cls.ventes, default=None, key=lambda v: v.id_vente
                        )
                    )
                    is None
                    else max_obj.id_vente
                )
                cls._id = max_id + 1
        except (JSONDecodeError, TypeError, KeyError):
            error("Error while trying to load ventes json data, using empty data")
        except FileNotFoundError:
            pass


Vente._load()
