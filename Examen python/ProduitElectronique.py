
class ProduitElectronique(Produit):
    def __init__(self, nom, prix, quantite, garantie):
        super().__init__(nom, prix, quantite)
        self.garantie = garantie

    def afficher_details(self):
        print(f"Nom: {self.nom}")
        print(f"Prix: {self.prix}")
        print(f"Quantite: {self.quantite}")
        print(f"Garantie: {self.garantie}")