from json import dump
from datetime import date
from typing import Optional

class Evenement:
    evenements = []
    _id = 1
    STORAGE_FILE = "storage/evenements.json"

    def __init__(
        self,
        titre: str,
        date_event: date,
        lieu: str,
        capacite: int,
        _id: Optional[int] = None,
        places_vendues: Optional[int] = None,
    ):
        self.id_evenement = Evenement._id if _id is None else _id
        self.titre = titre
        self.date = date_event  # stocker comme objet date
        self.lieu = lieu
        self.capacite = capacite
        self.places_vendues = places_vendues if places_vendues is not None else 0

        if self not in Evenement.evenements:
            Evenement.evenements.append(self)
        Evenement._id += 1
        self._sync()

    def __str__(self):
        return f"[{self.id_evenement}] {self.titre} - {self.date.isoformat()} - {self.lieu} - Capacité: {self.capacite}, Vendus: {self.places_vendues}"

    @property
    def places_restantes(self):
        return self.capacite - self.places_vendues

    def delete(self):
        if self in Evenement.evenements:
            Evenement.evenements.remove(self)
            self._sync()

    @classmethod
    def _sync(cls):
        # Sauvegarde en JSON, convertir date en str pour JSON
        with open(cls.STORAGE_FILE, "w+", encoding="utf-8") as f:
            dump(
                [{**e.__dict__, "date": e.date.isoformat()} for e in cls.evenements],
                f,
                indent=4,
                ensure_ascii=False
            )
