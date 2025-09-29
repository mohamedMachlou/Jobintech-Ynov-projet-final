#Menu for billetterie
from utils import input, radio, checkbox, select
from prompt_toolkit.shortcuts import clear

def menu():
    while True:
        print(f"\n======== {'Billetterie'.upper()} =======")
        print("1. Gestion des événements")
        print("2. Gestion de billets (vente)")
        print("3. Quitter")
        print("="*28)
        choix = input("• Choisir une option: ")

        if choix == "1":
            Gestion_evenement()
        elif choix == "2":
            ajouter_acheteur()
        elif choix == "3":
            break


def Gestion_evenement():
    clear()
    while True:
        print(f"\n----- {'Gestion des événements'.upper()} -----")
        print("1. Ajouter un évenement")
        print("2. Modifier un évenement")
        print("3. Supprimer un évenement")
        print("4. Liste des évenements à venir")
        print("5. Liste des évenements passés")
        print("6. Recherche d'évenement")
        print("7. <= Reteur au liste principale ")
        print("-"*34)
        choix = input("• Choisir une option: ")

        if choix == "1":
            ajouter_evenement()
        elif choix == "2":
            ajouter_acheteur()
        elif choix == "3":
            acheter_billets()
        elif choix == "4":
            annuler_vente()
        elif choix == "5":
            lister_evenements()
        elif choix == "6":
          #  billetterie.save_data()
            break


def ajouter_evenement():
    print('ajout evenement')

def ajouter_acheteur():
    print('ajouter acheteur')

def acheter_billets():
    print('acheter_billets')

def annuler_vente():
    print('annuler vente')

def lister_evenements():
    print('lister evenements')

menu()