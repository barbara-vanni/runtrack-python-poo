class Animal:
    def __init__(self, age, name):
        self.animal_age = age
        self.animal_name = name

    def afficher_age(self):
        print(f"L'âge de l'animal est : {self.animal_age} ans")

    def veillir(self):
        self.animal_age = (self.animal_age) + 1
        print(f"L'âge de l'animal est : {self.animal_age} ans")

        
    def nommer(self, name):
        self.animal_name = name
        print(f"L'animal se nomme {self.animal_name}")


chien = Animal(0, "")
chien.afficher_age()
chien.veillir()
chien.nommer("Luna")
