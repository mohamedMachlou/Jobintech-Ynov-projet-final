from evenement import Evenement

class Conference(Evenement):
    def __init__(self, id_evenement: int, titre: str, date: str, lieu: str, capacite: int, orateur_principal: str):
        super().__init__(id_evenement, titre, date, lieu, capacite)
        self.orateur_principal = orateur_principal

    def __str__(self):
        return super().__str__() + f" - Orateur: {self.orateur_principal}"
