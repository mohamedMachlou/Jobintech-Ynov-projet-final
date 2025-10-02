from json import JSONDecodeError, dump, load
from datetime import datetime as DatetimeType, datetime as Datetime
from typing import Optional

from utils.datetime import format_datetime
from utils.logger import error


class Evenement:
    evenements = []
    __unserializable__ = {}
    _id = 1
    STORAGE_FILE = "storage/evenements.json"

    def __init__(
        self,
        titre: str,
        date_event: DatetimeType,
        lieu: str,
        prix_base: int,
        capacite: int,
        _id: Optional[int] = None,
        places_vendues: Optional[int] = None,
    ):
        self.id_evenement = Evenement._id if _id is None else _id
        self.titre = titre
        self.date = date_event
        self.prix_base = prix_base
        self.lieu = lieu
        self.capacite = capacite
        self._places_vendues = places_vendues if places_vendues is not None else 0

        if self not in Evenement.evenements:
            Evenement.evenements.append(self)
        Evenement._id += 1
        self._sync()

    def __str__(self):
        event_type = (
            "Concert"
            if hasattr(self, "artiste")
            else "Conference" if hasattr(self, "orateur_principal") else "Evenement"
        )

        event_by = getattr(self, "artiste", getattr(self, "orateur_principal", None))

        return f"[{event_type}] ({ '' if not event_by else (event_by + ' |')} {self.titre}, {format_datetime(self.date)} - {self.lieu} => Prix Base: {self.prix_base})"

    @property
    def places_restantes(self):
        return self.capacite - self._places_vendues

    @property
    def places_vendues(self):
        return self._places_vendues

    @places_vendues.setter
    def places_vendues(self, p: int):
        if not p <= self.capacite:
            raise ValueError(
                f"Reserved places exceeed the capacity, reservations assigned: {p} , capacity :{self.capacite}."
            )

        self._places_vendues = p
        Evenement._sync()

    def delete(self):
        if self in Evenement.evenements:
            Evenement.evenements.remove(self)
            self._sync()

    @classmethod
    def _sync(cls):
        with open(cls.STORAGE_FILE, "w+", encoding="utf-8") as f:
            dump(
                [e.to_dict() for e in cls.evenements],
                f,
                indent=4,
                ensure_ascii=False,
            )

    @classmethod
    def _load(cls):
        from models.concert import Concert
        from models.conference import Conference

        try:
            with open(cls.STORAGE_FILE) as f:
                cls.evenements = list(
                    map(
                        lambda e: (
                            Concert(
                                e["titre"],
                                Datetime.fromisoformat(e["date"]),
                                e["lieu"],
                                e["prix_base"],
                                e["capacite"],
                                e["artiste"],
                                e["id_evenement"],
                                e["places_vendues"],
                            )
                            if "artiste" in e
                            else (
                                Conference(
                                    e["titre"],
                                    Datetime.fromisoformat(e["date"]),
                                    e["lieu"],
                                    e["prix_base"],
                                    e["capacite"],
                                    e["orateur_principal"],
                                    e["id_evenement"],
                                    e["places_vendues"],
                                )
                                if "orateur_principal" in e
                                else Evenement(
                                    e["titre"],
                                    Datetime.fromisoformat(e["date"]),
                                    e["lieu"],
                                    e["prix_base"],
                                    e["capacite"],
                                    e["id_evenement"],
                                    e["places_vendues"],
                                )
                            )
                        ),
                        load(f),
                    )
                )
                max_id = (
                    0
                    if (
                        max_id_element := max(
                            cls.evenements, default=None, key=lambda e: e.id_evenement
                        )
                    )
                    is None
                    else max_id_element.id_evenement
                )
                cls._id = max_id + 1

        except (JSONDecodeError, TypeError, KeyError):
            error(
                "Error while trying to load json data, the program is using empty data for now"
            )

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
