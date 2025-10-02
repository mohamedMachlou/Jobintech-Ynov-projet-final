class Billet:
    BILLET_TYPE = {"Standard": 1.0, "VIP": 1.5}

    @staticmethod
    def get_prix(type_billet, prix_base):
        """Retourne le prix d’un billet selon son type sans créer d'objet"""
        coeff = Billet.BILLET_TYPE.get(type_billet, None)
        if coeff is None:
            raise ValueError(f"Type de billet invalide : {type_billet}.")
        return prix_base * coeff
