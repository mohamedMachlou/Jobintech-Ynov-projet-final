from json import JSONDecodeError, dump, load
from datetime import datetime as DatetimeType, datetime as Datetime
from typing import Optional

from utils.logger import error


class Evenement:
    evenements = []
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
        self.places_vendues = places_vendues if places_vendues is not None else 0

        if self not in Evenement.evenements:
            Evenement.evenements.append(self)
        Evenement._id += 1
        self._sync()

    def __str__(self):
        return f"[{self.id_evenement}] {self.titre} - {self.date.isoformat()} - {self.lieu} - Prix Base: {self.prix_base}"

    @property
    def places_restantes(self):
        return self.capacite - self.places_vendues

    def delete(self):
        if self in Evenement.evenements:
            Evenement.evenements.remove(self)
            self._sync()

    @classmethod
    def _sync(cls):
        with open(cls.STORAGE_FILE, "w+", encoding="utf-8") as f:
            dump(
                [{**e.__dict__, "date": e.date.isoformat()} for e in cls.evenements],
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
