from json import dump, load, JSONDecodeError
from typing import Optional
from models.evenement import Evenement


class Concert(Evenement):
    tous_concerts = []  # Liste pour stocker tous les concerts
    _id = 1
    STORAGE_FILE = "storage/concerts.json"

    def __init__(
        self,
        titre: str,
        date: str,
        lieu: str,
        capacite: int,
        artiste: str,
        _id: Optional[int] = None,
        places_vendues: Optional[int] = None,
    ):
        # ID auto-incrémenté
        self.id_evenement = Concert._id if _id is None else _id
        super().__init__(titre, date, lieu, capacite, self.id_evenement, places_vendues)
        self.artiste = artiste

        # Ajouter à la liste et synchroniser JSON
        Concert.tous_concerts.append(self)
        Concert._id += 1
        self._sync()

    def __str__(self):
        return super().__str__() + f" - Artiste: {self.artiste}"

    def delete(self):
        if self in Concert.tous_concerts:
            Concert.tous_concerts.remove(self)
            self._sync()

    @classmethod
    def _sync(cls):
        # Écriture JSON sans créer le dossier automatiquement
        with open(cls.STORAGE_FILE, "w+", encoding="utf-8") as f:
            dump([c.__dict__ for c in cls.tous_concerts], f, indent=4, ensure_ascii=False)

    @classmethod
    def _load(cls):
        try:
            with open(cls.STORAGE_FILE, "r", encoding="utf-8") as f:
                data = load(f)
                cls.tous_concerts = [
                    Concert(
                        c["titre"],
                        c["date"],
                        c["lieu"],
                        c["capacite"],
                        c["artiste"],
                        c["id_evenement"],
                        c["places_vendues"],
                    )
                    for c in data
                ]
                max_id = max((c.id_evenement for c in cls.tous_concerts), default=0)
                cls._id = max_id + 1

        except (JSONDecodeError, TypeError, KeyError):
            print("Erreur JSON, utilisation d'une liste vide pour le moment")
        except FileNotFoundError:
            pass


# Charger les concerts existants au démarrage
Concert._load()
