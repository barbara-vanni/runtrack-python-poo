'''Créer une classe Commande avec les attributs privés, numéro de commande, liste de
plats commandés et statut de la commande (en cours, terminée ou annulée). Ajouter
des méthodes permettant d’ajouter un plat à la commande , annuler une commande,
calculer le total d’une commande qui doit être en privé et afficher une commande avec
son total à payer, ainsi qu’une méthode permettant de calculer la TVA. Utiliser
l’encapsulation et l’abstraction pour créer cette classe de manière que les attributs ne
puissent pas être modifiés de l’extérieur. La liste des plats commandés doit être
représentée sous forme de dictionnaire avec les noms des plats, le prix ainsi que le
statut de la commande.
'''


class Commande:
    def __init__(self, num_commande, plat_commande, statut_commande):
        self.__num_commande = num_commande
        self.__plat_commande = plat_commande
        self.__statut_commande = statut_commande


    def get_num_commande(self):
        return self.__num_commande
    
    def set_num_commande(self, num_commande):
        self.__num_commande = num_commande

    def get_plat_commande(self):
        return self.__plat_commande
    
    def set_plat_commande(self, plat_commande):
        self.__plat_commande = plat_commande

    def get_statut_commande(self):
        return self.__statut_commande
    
    def set_statut_commande(self, statut_commande):
        self.__statut_commande = statut_commande
    
    def ajout_plat(self):
        pass

    def annuler_plat(self):
        pass

    def __total_payer(self):
        pass

    def afficher_commande(self):
        pass

    def calcul_TVA(self):
        pass