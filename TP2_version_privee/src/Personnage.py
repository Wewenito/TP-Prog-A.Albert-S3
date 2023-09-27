class Personnage:
    def __init__(self, pseudo : str, niveau : int = 1):
        self.__pseudo = pseudo
        self.__niveau = niveau
        if self.__niveau == 1:
            self.__PVS = 1
            self.__initiative = 1
        else:
            self.__PVS = niveau
            self.__initiative = niveau       

    def attaque(self, adversaire : object):  
        if self.__initiative == adversaire.get_attr("initiative"):
            print("Les deux joueurs frappent au même moment !")
            adversaire.set_attr("PVS", adversaire.get_attr("PVS") - self.__niveau)
            self.__PVS = self.__PVS - adversaire.get_attr("niveau")
            if adversaire.get_attr("PVS") <= 0:
                print(f'{adversaire.get_attr("pseudo")} a péri..')
                return 'end'
            elif self.__PVS <= 0:
                print(f'{self.__pseudo} a péri..')
                return 'end'
            else:
                print(f'{adversaire.get_attr("pseudo")} a {adversaire.get_attr("PVS")} PVs restants..')
                print(f'{self.__pseudo} a {self.__PVS} PVs restants..')
                return 'continue'
        elif self.__initiative > adversaire.get_attr("initiative"):
            print(f'{self.__pseudo} attaque ! ')
            adversaire.set_attr("PVS", adversaire.get_attr("PVS") - self.__niveau)
            if adversaire.get_attr("PVS") <= 0:
                print(f'{adversaire.get_attr("pseudo")} a péri..')
                return 'end'
            else:
                print(f'{adversaire.get_attr("pseudo")} a {adversaire.get_attr("PVS")} Pvs restants..')
                return 'continue'
        else:
            print(f'{adversaire.get_attr("pseudo")} attaque ! ')
            self.__PVS = self.__PVS - adversaire.get_attr("niveau")
            if self.__PVS <= 0:
                print(f'{self.__pseudo} a péri..')
                return 'end'
            else:
                print(f'{self.__pseudo} a {self.__PVS} Pvs restants..')
                return 'continue'

    def combat(self, adversaire : object):
        while True:
            if self.__PVS > 0 and adversaire.get_attr("PVS") > 0:
                self.attaque(adversaire)
            else:
                print("Le combat est terminé")
                break
        
    def soigner(self):
        self.__PVS = self.__niveau
        print(f'{self.__pseudo} s\'est soigné et a maintenant {self.__PVS} PVs !')

    def degats(self):
        return self.__niveau
    
    def get_attr(self, name):
        if name == "pseudo":
            return self.__pseudo
        elif name == "niveau":
            return self.__niveau
        elif name == "PVS":
            return self.__PVS
        elif name == "initiative":
            return self.__initiative
        else:
            print("L'attribut souhaité n'existe pas")

    def set_attr(self, name, value):
        if name == "pseudo":
            self.__pseudo = value
        elif name == "niveau":
            self.__niveau = value
        elif name == "PVS":
            self.__PVS = value           
        elif name == "initiative":
            self.__initiative = value
        else:
            print("L'attribut souhaité n'existe pas")   


