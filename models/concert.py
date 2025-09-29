from evenement import Evenement

class Concert(Evenement):
    # Fonction d'initialisation de Concert
    def __init__(self, id_evenement: int, titre: str, date: str, lieu: str, capacite: int, artiste: str):
        super().__init__(id_evenement, titre, date, lieu, capacite)
        self.artiste = artiste

    def __str__(self):
        return super().__str__() + f" - Artiste: {self.artiste}"






