class Evenement:
    def __init__(self, id_evenement: int, titre: str, date: str, lieu: str, capacite: int):
        self.id_evenement = id_evenement
        self.titre = titre
        self.date = date
        self.lieu = lieu
        self.capacite = capacite
        self.places_vendues = 0

    def __str__(self):
        return f"[{self.id_evenement}] {self.titre} - {self.date} - {self.lieu} - Capacité: {self.capacite}, Vendus: {self.places_vendues}"

    def places_restantes(self):
        return self.capacite - self.places_vendues
