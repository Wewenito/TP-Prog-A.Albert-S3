from Personnage import Personnage

class Mage(Personnage):
    def __init__(self, pseudo: str, niveau: int):
        Personnage.__init__(self, pseudo, niveau)
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__PVS = (self.__niveau * 5) + 10
        self.__initiative = (self.__niveau * 6) + 4
        self.__mana = self.__niveau * 5

    def degats(self):
        if self.__mana >= 4:
            self.__mana = self.__mana - 4
            return self.__niveau + 3
        else:
            return self.__niveau
        
    #Accesseurs

    def get_attr(self, name):
        if name == "pseudo":
            return self.__pseudo
        elif name == "niveau":
            return self.__niveau
        elif name == "PVS":
            return self.__PVS
        elif name == "initiative":
            return self.__initiative
        elif name == "mana":
            return self.__mana
        else:
            print("L'attribut entré n'existe pas dans cette classe")

    def set_attr(self, name, value):
        if name == "pseudo":
            self.__pseudo = value
        elif name == "niveau":
            self.__niveau = value
        elif name == "PVS":
            self.__PVS = value
        elif name == "initiative":
            self.__initiative = value
        elif name == "mana":
            self.__mana = value
        else:
            print("L'attribut entré n'existe pas dans cette classe")
        