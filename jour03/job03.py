class Tache:

    def __init__(self, titre, description, statut = "à faire"):
        self.__titre = titre
        self.__description = description
        self.__statut = statut

    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre
        
    def get_descritpion(self):
        return self.__descritpion
    
    def set_descritpion(self, descritpion):
        self.__descritpion = descritpion

    def get_statut(self):
        return self.__statut
    
    def set_statut(self, statut):
        self.__statut = statut