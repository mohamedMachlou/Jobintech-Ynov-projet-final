# Classe billet
class Billet:
    billets = []

    BILLET_TYPE = {
        'Standard': .50,
        'VIP':  .75
    }
    billets = []
    def __init__(self, prix, type_billet):
        self.type_billet = type_billet
        self.prix += prix * Billet.BILLET_TYPE[type_billet]
        Billet.billets.append(self)


    def getPrix(self, type_billet):
        return self.prix.get(type_billet,0)





