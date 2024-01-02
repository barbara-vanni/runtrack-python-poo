
class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom_produit = nom
        self.prix_produit = prixHT
        self.TVA_produit = TVA

    def CalculerPrixTTC(self):
        prix_TTC = self. prix_produit + self.Calcule_TVA()
        return prix_TTC

    def Calcule_TVA(self):
        montant_TVA = self.prix_produit * (self.TVA_produit/100) 
        return montant_TVA

    def afficher(self):
        return f"{self.nom_produit} \nPrix HT: {self.prix_produit} € , TVA: {self.TVA_produit}% \nPrix TTC: {self.CalculerPrixTTC()} € \n"

    def modifierNom(self, nouveauNom):
        self.nom_produit = nouveauNom

    def modifierPrixHT(self, nouveauPrixHT):
        self.prix_produit = nouveauPrixHT

    def obtenirNom(self):
        return self.nom_produit

    def obtenirPrixHT(self):
        return self.prix_produit

    def obtenirTVA(self):
        return self.TVA_produit
    

produit1 = Produit("Pomme", 5, 20)
produit2 = Produit("Buche", 30, 10)

print(produit1.afficher())
print(produit2.afficher())

print(produit1.obtenirPrixHT())
produit1.modifierNom("Carrelage")
produit1.modifierPrixHT(60)

produit2.modifierNom("Booster")
produit2.modifierPrixHT(400)

print(produit1.afficher())
print(produit2.afficher())

print(produit1.obtenirTVA())
print(produit1.obtenirPrixHT())