# Classe billet
class Billet:
    prix = {
        'Standard': 50,
        'VIP':  100
    }

    def getPrix(self, type_billet):
        return self.prix.get(type_billet,0)





