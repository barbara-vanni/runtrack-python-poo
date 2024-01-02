from math import *

class Cercle:
    def __init__(self, r):
        self.rayon = r

    def changerRayon(self, new_rayon):
        self.rayon = self.new_rayon

    def afficherInfos(self):
        print(f"rayon : {self.rayon} \ndiamètre : {self.diametre()} \ncirconference : {self.circonference()} \naire : {self.aire()}")
        pass

    def diametre (self):
        diametre = self.rayon * 2 
        return diametre
    
    def circonference(self):
        circonference = self.diametre() * pi
        return circonference

    def aire (self):
        aire = (self.rayon**2) * pi 
        return aire 



cercle1 = Cercle(4)
print("Cercle 1 ")
cercle1.afficherInfos()
cercle2 = Cercle(7)
print("\nCercle 2 ")
cercle2.afficherInfos()
