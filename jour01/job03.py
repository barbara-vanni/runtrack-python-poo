class Operation:
    def __init__(self, nombre1, nombre2):
        self.operation_nombre1 = nombre1
        self.operation_nombre2 = nombre2
    
    def addition(self):
        resultat = self.operation_nombre1+ self.operation_nombre2
        print(f"Le nombre {self.operation_nombre1} + {self.operation_nombre2} est égal à {resultat}")
        
        

   

instance = Operation(12, 3)
instance.addition()