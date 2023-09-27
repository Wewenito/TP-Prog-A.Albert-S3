from Personnage import Personnage

class Guerrier(Personnage):
    def __init__(self, pseudo : str, niveau : int):
        Personnage.__init__(self,pseudo, niveau)
        self.pseudo = pseudo   
        self.niveau = niveau
        self.PVS = (self.niveau * 8) + 4
        self.initiative = (self.niveau * 4) + 6

    def degats(self):
        return self.niveau * 2