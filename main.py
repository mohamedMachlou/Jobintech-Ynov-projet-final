# from services.main_menu import main_menu
from services import concert_service
# import seeders.main as _
#
#
# def main():
#     try:
#         main_menu()
#     except:
#         pass
#
#
# if __name__ == "__main__":
#     main()


from services import ajout_nouveau_concert, update_concert, delete_concert
from models import Concert

# Ajout de concerts
c1 = ajout_nouveau_concert("Rock Night", "2025-12-20", "Casablanca", 500, "Coldplay")
c2 = ajout_nouveau_concert("Jazz Evening", "2025-11-10", "Rabat", 300, "Norah Jones")

# Afficher les concerts
for c in Concert.concerts:
    print(c)

# Mise à jour
update_concert(1, "2025-12-25", "Marrakech")

# Suppression
delete_concert(2)

# Affichage final
for c in Concert.concerts:
    print(c)