from models.vente import Vente

data = [
    {"id_evenement": 1, "id_acheteur": 1, "type_billet": "Standard", "quantite": 2},
    {"id_evenement": 1, "id_acheteur": 2, "type_billet": "VIP", "quantite": 1},
    {"id_evenement": 2, "id_acheteur": 3, "type_billet": "Standard", "quantite": 3},
    {"id_evenement": 2, "id_acheteur": 4, "type_billet": "VIP", "quantite": 2},
]

for v in data:
    Vente(
        id_evenement=v["id_evenement"],
        id_acheteur=v["id_acheteur"],
        type_billet=v["type_billet"],
        quantite=v["quantite"],
    )
