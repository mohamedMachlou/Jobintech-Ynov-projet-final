from datetime import datetime as Datetime
from models.evenement import Evenement
from models.concert import Concert
from models.conference import Conference


data = [
    {
        "titre": "Concert Musk",
        "date": "2025-10-10",
        "lieu": "Stade Olympique",
        "capacite": 5000,
        "places_vendues": 1200,
        "prix_base": 200,
        "artiste": "Les Électrons",
    },
    {
        "titre": "Conférence IA",
        "date": "2025-11-05",
        "lieu": "Palais des Congrès",
        "capacite": 3,
        "places_vendues": 2,
        "prix_base": 150,
        "orateur_principal": "Dr. Jeanne Dupont",
    },
    {
        "orateur_principal": "Prof Martin",
        "titre": "Salon du Livre",
        "date": "2025-12-01",
        "lieu": "Centre Culturel",
        "capacite": 1000,
        "prix_base": 250,
        "places_vendues": 450,
    },
]


for e in data:
    (
        Concert(
            e["titre"],
            Datetime.fromisoformat(e["date"]),
            e["lieu"],
            e["prix_base"],
            e["capacite"],
            e["artiste"],
            None,
            e["places_vendues"],
        )
        if "artiste" in e
        else (
            Conference(
                e["titre"],
                Datetime.fromisoformat(e["date"]),
                e["lieu"],
                e["prix_base"],
                e["capacite"],
                e["orateur_principal"],
                None,
                e["places_vendues"],
            )
            if "orateur_principal" in e
            else Evenement(
                e["titre"],
                Datetime.fromisoformat(e["date"]),
                e["lieu"],
                e["prix_base"],
                e["capacite"],
                None,
                e["places_vendues"],
            )
        )
    )
