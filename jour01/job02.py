
class Operation:
    def __init__(self, nombre1, nombre2):
        self.operation_nombre1 = nombre1
        self.operation_nombre2 = nombre2
    
    def afficher(self):
        print(f"Le nombre est {self.operation_nombre1}")
        print(f"Le nombre est {self.operation_nombre2}")
        

   

instance = Operation(12, 3)
instance.afficher()

