import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def generer_rapport_financier_et_frequentation(
        ventes_path="storage/ventes.json",
        evenements_path="storage/evenements.json",
        save_path="storage/rapport_ventes.png"
    ):

    # Charger ventes
    with open(ventes_path, "r", encoding="utf-8") as f:
        ventes = json.load(f)

    # Charger événements
    with open(evenements_path, "r", encoding="utf-8") as f:
        evenements = json.load(f)

    df_ventes = pd.DataFrame(ventes)
    df_evenements = pd.DataFrame(evenements)

    # Déterminer type (Concert / Conférence)
    def infer_type(row):
        if "artiste" in row and row["artiste"]:
            return "Concert"
        if "orateur_principal" in row and row["orateur_principal"]:
            return "Conference"
        return "Autre"

    df_evenements["type"] = df_evenements.apply(infer_type, axis=1)

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

    # Graphique empilé
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

    print("====== Rapport généré ======")
    print(f"• Revenu par type d'événement:\n{'-'*28}\n", revenu_par_type)
    print(f"\n• Statistiques globales:\n{'-'*30}\n", stats)
    print(f"\n• Répartition billets par événement:\n{'-'*30}\n", pivot)
    print(f"\n• Graphique sauvegardé dans: {save_path}")
    print('='*24)

    return {
        "revenu_par_type": revenu_par_type,
        "stats": stats,
        "pivot": pivot,
        "graph_path": save_path
    }
