class Personne:
    def __init__(self, nom, prenom):
        self.user_name = nom
        self.user_surname = prenom
    
    def SePresenter(self):
        print(f"Je suis {self.user_surname} {self.user_name}")
        

   

Personne1 = Personne("Doe", "John")
Personne1.SePresenter()

Personne2 = Personne("Dupond", "Jean")
Personne2.SePresenter()