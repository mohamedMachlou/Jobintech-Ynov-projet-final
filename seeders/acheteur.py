from models.acheteur import Acheteur


data = [
    {
        "nom": "Alice Dupont",
        "email": "alice.dupont@gmail.com",
    },
    {
        "nom": "Alice Dupont",
        "email": "bob.martin@gmail.com",
    },
    {
        "nom": "Alice Dupont",
        "email": "bob.martin@gmail.com",
    },
    {"nom": "Chloé Lefevre", "email": "chloe.lefevre@gmail.com"},
]

print("\t[+] Seeding Acheteur with:")
for a in data:
    print(f"\t\t- name: {a['nom']}, email: {a['email']}")
    Acheteur(a["nom"], a["email"])
