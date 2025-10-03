import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
from models import Evenement, Vente

def generer_rapport_financier_et_frequentation(
        save_path="storage/rapport_ventes.png"
    ):
    from services.main import main_menu

    # Charger ventes
    ventes = Vente.ventes

    # Charger événements
    evenements = Evenement.evenements

    df_ventes = pd.DataFrame([v.to_dict() for v in ventes])
    df_evenements = pd.DataFrame([
        {**e.to_dict(),
         "type": "Concert" if "artiste" in e.to_dict() and e.to_dict()["artiste"]
         else "Conference" if "orateur_principal" in e.to_dict() and e.to_dict()["orateur_principal"]
         else "Evenement"
         }
        for e in evenements
    ])

    # Jointure ventes + infos événement
    df = df_ventes.merge(
        df_evenements[["id_evenement", "titre", "type"]],
        on="id_evenement",
        how="left"
    )

    # Revenu total par type d'événement
    revenu_par_type = df.groupby("type")["prix_total"].sum().reset_index()

    # Statistiques globales
    stats = {
        "transactions": len(df),
        "total_billets": int(df["quantite"].sum()),
        "moyenne_billets_par_vente": round(float(df["quantite"].mean()), 2),
        "revenu_total": round(float(df["prix_total"].sum()), 2)
    }

    # Répartition Standard vs VIP par événement
    pivot = df.pivot_table(
        index=["id_evenement", "titre", "type"],
        columns="type_billet",
        values="quantite",
        aggfunc="sum",
        fill_value=0
    ).reset_index()

    # Géneration de Graphique empilé
    x = np.arange(len(pivot))
    fig, ax = plt.subplots(figsize=(12, 7), constrained_layout=True)

    standard = pivot["Standard"] if "Standard" in pivot else [0]*len(pivot)
    vip = pivot["VIP"] if "VIP" in pivot else [0]*len(pivot)

    ax.bar(x, standard, label="Standard")
    ax.bar(x, vip, bottom=standard, label="VIP")

    # Raccourcir les titres trop longs
    labels = [t if len(t) <= 20 else t[:17] + "..." for t in pivot["titre"].tolist()]
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45, ha="right")

    ax.set_ylabel("Billets vendus")
    ax.set_title("Répartition des ventes par événement")
    ax.legend()

    plt.savefig(save_path)
    plt.close()

    print("====== Analyse et Rapports ======")

    # Titre et revenu par type d'événement
    revenu_type = "Revenu par type d'événement"
    separator = "-" * len(revenu_type)
    print(f"\n{revenu_type}\n{separator}")
    print(tabulate(revenu_par_type, headers="keys", tablefmt="fancy_grid", stralign="left", numalign="left"))

    # Statistiques globales
    stats_title = "Statistiques globales"
    print(f"\n{stats_title}\n{'-' * len(stats_title)}")
    print(tabulate([stats], headers="keys", tablefmt="fancy_grid", stralign="left", numalign="left"))

    # Répartition billets par événement
    pivot_title = "Répartition billets par événement"
    print(f"\n{pivot_title}\n{'-' * len(pivot_title)}")
    print(tabulate(pivot, headers="keys", tablefmt="fancy_grid", stralign="left", numalign="left"))

    # Graphique
    print(f"\n• Graphique sauvegardé dans: {save_path}")
    print("=" * len(f"• Graphique sauvegardé dans: {save_path}\n"))

    return main_menu()
