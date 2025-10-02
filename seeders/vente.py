from models.vente import Vente

data = [
    {
        "id_evenement": 1,
        "id_acheteur": 1,
        "type_billet": "Standard",
        "quantite": 2,
        "date": "2025-11-05",
        "date": "2025-10-01T16:16:06.257122",
    },
]

for v in data:
    Vente(
        id_evenement=v["id_evenement"],
        id_acheteur=v["id_acheteur"],
        type_billet=v["type_billet"],
        quantite=v["quantite"],
    )
