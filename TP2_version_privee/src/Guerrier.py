from Personnage import Personnage

class Guerrier(Personnage):
    def __init__(self, pseudo : str, niveau : int):
        Personnage.__init__(self,pseudo, niveau)
        self.__pseudo = pseudo   
        self.__niveau = niveau
        self.__PVS = (self.__niveau * 8) + 4
        self.__initiative = (self.__niveau * 4) + 6

    def degats(self):
        return self.__niveau * 2

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
            print("L'attribut séléctionné n'existe pas dans cette classe")
    
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
            print("L'attribut séléctionné n'existe pas dans cette classe")