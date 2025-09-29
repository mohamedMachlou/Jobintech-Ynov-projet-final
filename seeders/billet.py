from models.billet import Billet

data = [
    {"prix_base": 50, "type_billet": "Standard"},
    {"prix_base": 50, "type_billet": "VIP"},
    {"prix_base": 30, "type_billet": "Standard"},
    {"prix_base": 30, "type_billet": "VIP"},
    {"prix_base": 100, "type_billet": "VIP"},
]

for b in data:
    Billet(prix_base=b["prix_base"], type_billet=b["type_billet"])
