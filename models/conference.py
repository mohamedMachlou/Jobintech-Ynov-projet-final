from json import dump, load, JSONDecodeError
from typing import Optional
from models import Evenement


class Conference(Evenement):
    toutes_conferences = []  # Liste pour stocker toutes les conférences
    _id = 1
    STORAGE_FILE = "storage/conferences.json"

    def __init__(
        self,
        titre: str,
        date: str,
        lieu: str,
        capacite: int,
        orateur_principal: str,
        _id: Optional[int] = None,
        places_vendues: Optional[int] = None,
    ):
        # ID auto-incrémenté
        self.id_evenement = Conference._id if _id is None else _id
        super().__init__(titre, date, lieu, capacite, self.id_evenement, places_vendues)
        self.orateur_principal = orateur_principal

        # Ajouter à la liste et synchroniser JSON
        Conference.toutes_conferences.append(self)
        Conference._id += 1
        self._sync()

    def __str__(self):
        return super().__str__() + f" - Orateur: {self.orateur_principal}"

    def delete(self):
        if self in Conference.toutes_conferences:
            Conference.toutes_conferences.remove(self)
            self._sync()

    @classmethod
    def _sync(cls):
        # Écriture JSON sans création automatique du dossier
        with open(cls.STORAGE_FILE, "w+", encoding="utf-8") as f:
            dump([c.__dict__ for c in cls.toutes_conferences], f, indent=4, ensure_ascii=False)

    @classmethod
    def _load(cls):
        try:
            with open(cls.STORAGE_FILE, "r", encoding="utf-8") as f:
                data = load(f)
                cls.toutes_conferences = [
                    Conference(
                        c["titre"],
                        c["date"],
                        c["lieu"],
                        c["capacite"],
                        c["orateur_principal"],
                        c["id_evenement"],
                        c["places_vendues"],
                    )
                    for c in data
                ]
                max_id = max((c.id_evenement for c in cls.toutes_conferences), default=0)
                cls._id = max_id + 1

        except (JSONDecodeError, TypeError, KeyError):
            print("Erreur JSON, utilisation d'une liste vide pour le moment")
        except FileNotFoundError:
            pass


# Charger les conférences existantes au démarrage
Conference._load()
