class ProduitAlimentaire(Produit):
    def __init__(self, nom, prix, quantite, date_expiration):
        super().__init__(nom, prix, quantite)
        self.date_expiration = date_expiration

    def afficher_details(self):
        print(f"Nom: {self.nom}")
        print(f"Prix: {self.prix}")
        print(f"Quantite: {self.quantite}")
        print(f"Date d'expiration: {self.date_expiration}")