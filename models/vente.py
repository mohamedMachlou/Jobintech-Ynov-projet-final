from json import JSONDecodeError, dump, load
from datetime import datetime as Datetime, datetime as DatetimeType
from typing import Optional
from utils import find
from utils.logger import error
from models.billet import Billet


class Vente:
    ventes = []
    __unserializable__ = {"evenement", "acheteur"}
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
        self._type_billet = type_billet
        self._quantite = quantite
        self.date = Datetime.now() if date is None else date
        self.prix_total = (
            Billet.get_prix(type_billet, getattr(self.evenement, "prix_base", 0))
            * quantite
        )
        Vente._id += 1
        Vente.ventes.append(self)
        self._sync()

        if self.evenement:
            self.evenement.places_vendues += quantite
            self.evenement._sync()



    def delete(self):
        if self in Vente.ventes:
            Vente.ventes.remove(self)
            self._sync()

        if self.evenement:
            self.evenement.places_vendues += 1
            self.evenement._sync()

    @property
    def quantite(self):
        return self._quantite

    @quantite.setter
    def quantite(self, value):
        evenement = self.evenement
        if evenement is None:
            return None

        evenement.places_vendues -= self._quantite

        self._quantite = value
        self.prix_total = (
            Billet.get_prix(self.type_billet, getattr(self.evenement, "prix_base", 0))
            * value
        )
        self.prix_total += value
        evenement.places_vendues += value
        Vente._sync()

    @property
    def type_billet(self):
        return self._type_billet

    @type_billet.setter
    def type_billet(self, value):
        self._type_billet = value
        self.prix_total = (
            Billet.get_prix(value, getattr(self.evenement, "prix_base", 0))
            * self._quantite
        )
        Vente._sync()

    def __str__(self):
        return f"{self.type_billet}: {self.evenement} x {self.quantite} = {self.prix_total}"

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
                [v.to_dict() for v in cls.ventes],
                f,
                indent=4,
                ensure_ascii=True,
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

    def to_dict(self):
        data = {}

        for k, v in self.__dict__.items():
            new_key = k[1:] if k.startswith("_") else k
            data[new_key] = v

        for name, attr in vars(self.__class__).items():
            if (
                isinstance(attr, property)
                and name not in data
                and name not in self.__unserializable__
            ):
                value = getattr(self, name)
                data[name] = value

        if "date" in data and hasattr(data["date"], "isoformat"):
            data["date"] = data["date"].isoformat()

        return data
