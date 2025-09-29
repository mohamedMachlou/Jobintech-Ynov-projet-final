# Classe Vente
import billet

class Vente:
    def __init__(self, id_vente, id_evenement, id_acheteur, type_billet, quantite):
        self.id_vente = id_vente
        self.id_evenement = id_evenement
        self.id_acheteur = id_acheteur
        self.type_billet = type_billet
        self.quantite = quantite
        self.prix_total = billet.Billet.getPrix(type_billet,0)*quantite
