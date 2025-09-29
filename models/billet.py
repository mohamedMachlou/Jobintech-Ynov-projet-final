# Classe Billet
class Billet:
    billets = []  # liste pour stocker tous les billets créés

    # Coefficients de prix par type
    BILLET_TYPE = {
        'Standard': 1.0,   # Prix normal
        'VIP': 1.5         # +50% du prix
    }

    def __init__(self, prix_base, type_billet):
        if type_billet not in Billet.BILLET_TYPE:
            raise ValueError(f"Type de billet invalide : {type_billet}. Choisir entre {list(Billet.BILLET_TYPE.keys())}")

        self.type_billet = type_billet
        # Appliquer le coefficient de prix selon le type
        self.prix = prix_base * Billet.BILLET_TYPE[type_billet]

        # Sauvegarde dans la liste globale des billets
        Billet.billets.append(self)

    def __str__(self):
        return f"Billet {self.type_billet} - Prix : {self.prix:.2f}€"

    @staticmethod
    def get_prix(type_billet, prix_base):
        """Retourne le prix d’un billet selon son type sans créer d'objet"""
        coeff = Billet.BILLET_TYPE.get(type_billet, None)
        if coeff is None:
            raise ValueError(f"Type de billet invalide : {type_billet}.")
        return prix_base * coeff
