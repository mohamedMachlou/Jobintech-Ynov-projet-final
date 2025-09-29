from models.acheteur import Acheteur


data = [
    {
        "nom": "Alice Dupont",
        "email": "alice.dupont@gmail.com",
    },
    {
        "nom": "Bob Martin",
        "email": "bob.martin@gmail.com",
    },
    {"nom": "Chloé Lefevre", "email": "chloe.lefevre@gmail.com"},
]

for a in data:
    Acheteur(a["nom"], a["email"])
