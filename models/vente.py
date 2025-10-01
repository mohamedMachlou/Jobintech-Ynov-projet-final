from json import JSONDecodeError, dump, load
from datetime import datetime as Datetime, datetime as DatetimeType
from typing import Optional
from utils import find
from utils.logger import error
from models.billet import Billet


class Vente:
    ventes = []
    STORAGE_FILE = "storage/ventes.json"
    _id = 1

    def __init__(
        self,
        id_evenement,
        id_acheteur,
        type_billet,
        quantite,
        date: Optional[DatetimeType] = None,
        id_vente: Optional[int] = None,
    ):
        self.id_vente = self._id if id_vente is None else id_vente
        self.id_evenement = id_evenement
        self.id_acheteur = id_acheteur
        self.type_billet = type_billet
        self.quantite = quantite
        self.date = Datetime.now() if date is None else date
        self.prix_total = (
            Billet.get_prix(type_billet, getattr(self.evenement, "prix_base", 0))
            * quantite
        )
        Vente._id += 1
        Vente.ventes.append(self)
        self._sync()

        if self.evenement:
            self.evenement.places_vendues += 1
            self.evenement._sync()

    def delete(self):
        if self in Vente.ventes:
            Vente.ventes.remove(self)
            self._sync()

        if self.evenement:
            self.evenement.places_vendues += 1
            self.evenement._sync()

    @property
    def evenement(self):
        from models.evenement import Evenement

        return find(Evenement.evenements, lambda e: e.id_evenement == self.id_evenement)

    @property
    def acheteur(self):
        from models.acheteur import Acheteur

        return find(Acheteur.achateurs, lambda a: a.id_acheteur == self.id_acheteur)

    @classmethod
    def _sync(cls):
        with open(cls.STORAGE_FILE, "w+", encoding="utf-8") as f:
            dump(
                [{**v.__dict__, "date": v.date.isoformat()} for v in cls.ventes],
                f,
                indent=4,
                ensure_ascii=False,
            )

    @classmethod
    def _load(cls):
        try:
            with open(cls.STORAGE_FILE, "r", encoding="utf-8") as f:
                cls.ventes = [
                    Vente(
                        v["id_evenement"],
                        v["id_acheteur"],
                        v["type_billet"],
                        v["quantite"],
                        DatetimeType.fromisoformat(v["date"]),
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
