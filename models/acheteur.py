class Acheteur:
    achateurs = []
    _id = 1

    def __init__(self, nom: str, email: str):
        self.id_acheteur = self._id
        self.nom = nom
        self.email = email
        Acheteur.achateurs.append(self)
        Acheteur._id += 1
