import datetime      #date
import random       #nombre aléatoire 
import os           #gestion de fichier 
import shutil       # gestion de fichier 
import statistics   # stats
import tkinter as tk  # interface graphique
from abc import ABC, abstractmethod   
### Classe principale (abstraite)
class Produit(ABC):




#Constructeur avec des arguments
    def __init__(self, name, prix, quantity,prix_unitaire=0,code_barre=None, date_ajout=None,date_expiration=None, fournisseur='', poids=None, categorie='', description=''):
        self.nom = name
        self.prix = prix
        self.quantity = quantity
        self.date_ajout=datetime.date.today()
        self.date += datetime.timedelta(days=15)
        if code_barre is None:
            self.code_barre= random.randint(10000,1000000)
        else:
            self.code_barre=id
        self.fournisseur = fournisseur
        self.poids = poids
        self.categorie = categorie
        self.description = description
   
   # Constructeur sans argument 
    def __init__(self):
         self.produit= {}

    @abstractmethod
    def afficher_details(self):
        pass


   # Getters
    def get_nom(self):
        return self._nom

    def get_prix(self):
        return self._prix

    def get_quantite(self):
        return self._quantite

    def get_date_ajout(self):
        return self.date_ajout
    
    def get_code_barre(self):
        return self.code_barre
    
    def get_fournisseur(self):
        return self.fournisseur
    
    def get_poids(self):
        return self.poids
    
    def get_categorie(self):
        return self.categorie
    
    def get_description(self):
        return self.description
    
    
    # Setters
    
    def set_nom(self, nom):
        self._nom = nom

    def set_prix(self, prix):
        self._prix = prix

    def set_quantite(self, quantite):
         self._quantite = quantite

    def set_date_ajout(self, date_ajout):
        self.date_ajout = date_ajout
    
    def set_code_barre(self, code_barre):
        self.code_barre = code_barre
    
    def set_fournisseur(self, fournisseur):
        self.fournisseur = fournisseur
    
    def set_poids(self, poids):
        self.poids = poids
    
    def set_categorie(self, categorie):
        self.categorie = categorie
    
    def set_description(self, description):
        self.description = description
        ### Méthode ajouter produit #### 

    def ajouter_produit(self, name, quantity):
        if name in self.produit:
            self.produit[name] += quantity
        else:
            self.produit[name] = quantity
        ### Méthode supprimer produit #### 
    def suppr_produit(self, name, quantity):
        if name in self.produit:
            if self.produit[name] >= quantity:
                self.produit[name] -= quantity
            else:
                print("stock insuffisante pour " + name)
        else:
            print(name + " est pas trouvé dans la stock")

                    ### Méthode modifier produit #### 
    def modif_produit(self, name, new_quantity):
        if name in self.produit:
            self.produit[name] = new_quantity
        else:
            print(name + " not found in stock")
                    ### Méthode afficher produit #### 
    def afficher_stock(self):
        for name, quantity in self.products.items():
            print(name + ": " + str(quantity))

    def calcul_stats_prix_globale(liste_produits):
    # Créer une liste de tous les prix de produits
        prix_produits = [produit.prix for produit in liste_produits]
    
    # Calculer les statistiques de prix globales
        moyenne_prix = statistics.mean(prix_produits)
        mediane_prix = statistics.median(prix_produits)
        ecart_type_prix = statistics.stdev(prix_produits)
# Retourner les statistiques de prix globales sous forme de tuple
        return (moyenne_prix, mediane_prix, ecart_type_prix)





####Fonction principale de l'application ###
def main():
    produit= Produit()
### Menu de commande ####
    while True:
        print("Stock Management System")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Product")
        print("4. Display Stock")
        print("5. Quit")
        print("**********************")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            produit.ajouter_produit(name, quantity)
            print(name + " added to stock")

        elif choice == "2":
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            produit.suppr_produit(name, quantity)
            print(name + " removed from stock")

        elif choice == "3":
            name = input("Enter product name: ")
            quantity = int(input("Enter new quantity: "))
            produit.modif_produit(name, quantity)
            print(name + " quantity updated")

        elif choice == "4":
            print("Current Stock:")
            produit.afficher_stock()

        elif choice == "5":
            print("Quitting...")
            break

        else:
            print("Invalid choice. Please try again.\n")

  
    
    
main()
# spécifier le chemin d'origine du fichier
source = "C:\Users\PC01\Desktop\Examen python"

# spécifier le répertoire de destination en disque C
destination = "C:\Hamdi"

# copier le fichier de la source vers la destination
shutil.copy(source, destination)

# Récupérer la liste de tous les fichiers dans le répertoire destination 
fichiers = os.listdir(destination)

# Afficher le nom de tous les fichiers dans le répertoire
for fichier in fichiers:
    print(fichier)


produit1 = Produit("Pommes", 2.5, 10),
produit2 = Produit("Bananes", 1.5, 20),
produit3 = Produit("Oranges", 3.0, 15),
produit4 = Produit("Poires", 2.0, 12),
produit5 = Produit("Fraises", 4.0, 8),
Liste_produits = [produit1, produit2, produit3, produit4, produit5]




# Essaie pour creer une interface graphique ( pas assez de temps )
root = tk.Tk()
gui = Produit(root)
root.mainloop()