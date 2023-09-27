from Personnage import Personnage

class Mage(Personnage):
    def __init__(self, pseudo: str, niveau: int):
        Personnage.__init__(self, pseudo, niveau)
        self.pseudo = pseudo
        self.niveau = niveau
        self.PVS = (self.niveau * 5) + 10
        self.initiative = (self.niveau * 6) + 4
        self.mana = self.niveau * 5

    def degats(self):
        if self.mana >= 4:
            self.mana = self.mana - 4
            return self.niveau + 3
        else:
            return self.niveau
        