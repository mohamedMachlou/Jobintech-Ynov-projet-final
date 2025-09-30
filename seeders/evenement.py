from models.evenement import Evenement
from models.concert import Concert
from models.conference import Conference


data = [
    {
        "id_evenement": 1,
        "titre": "Concert Rock",
        "date": "2025-10-10",
        "lieu": "Stade Olympique",
        "capacite": 5000,
        "places_vendues": 1200,
        "artiste": "Les Électrons",
    },
    {
        "id_evenement": 2,
        "titre": "Conférence IA",
        "date": "2025-11-05",
        "lieu": "Palais des Congrès",
        "capacite": 3,
        "places_vendues": 2,
        "orateur_principal": "Dr. Jeanne Dupont",
    },
    {
        "id_evenement": 3,
        "titre": "Salon du Livre",
        "date": "2025-12-01",
        "lieu": "Centre Culturel",
        "capacite": 1000,
        "places_vendues": 450,
    },
]


for e in data:
    (
        Concert(e["titre"], e["date"], e["lieu"], e["capacite"], e["artiste"], e["id_evenement"], e["places_vendues"])
        if "artiste" in e
        else (
            Conference(
                e["titre"], e["date"], e["lieu"], e["capacite"], e["orateur_principal"], e["id_evenement"], e["places_vendues"]
            )
            if "orateur_principal" in e
            else Evenement(
                e["titre"],
                e["date"],
                e["lieu"],
                e["capacite"],
                e["id_evenement"],
                e["places_vendues"]
            )
        )
    )
