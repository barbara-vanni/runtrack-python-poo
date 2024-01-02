class Point:
    def __init__(self, x, y):
        self.coordinate_x = x
        self.coordinate_y = y
    

    def afficherX(self):
        print(f"Coordonnées X : {self.coordinate_x}")

    def changerX(self, new_x):
        self.coordinate_x = new_x

    def afficherY(self):
        print(f"Coordonnées Y : {self.coordinate_y}")

    def changerY(self, new_y):
        self.coordinate_y = new_y
        
    def afficherLesPoints(self):
        self.afficherX() 
        self.afficherY()


coordinate_XY = Point(50, 12)
coordinate_XY.afficherLesPoints()

coordinate_XY.changerX(65)
coordinate_XY.changerY(-15)
coordinate_XY.afficherLesPoints()

