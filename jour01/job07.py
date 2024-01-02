class Personnage:
    def __init__(self, x, y):
        self.position_x = x
        self.position_y = y

    def haut(self):
        self.position_y = (self.position_y) + 1
    def bas(self):
        self.position_y = (self.position_y) - 1
    def droite(self):
        self.position_x = (self.position_x) + 1       
    def gauche(self):
        self.position_x = (self.position_x) - 1

    def position(self):
        return (self.position_x, self.position_y)



troll = Personnage(5, 6)
print(f"position initiale : {troll.position()}")
troll.gauche()
print(f"position après déplacement : {troll.position()}")
troll.droite()
print(f"position après déplacement : {troll.position()}")
troll.haut()
print(f"position après déplacement : {troll.position()}")
