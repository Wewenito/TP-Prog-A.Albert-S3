class Personnage:
    def __init__(self, pseudo : str, niveau : int = 1):
        self.pseudo = pseudo
        self.niveau = niveau
        if self.niveau == 1:
            self.PVS = 1
            self.initiative = 1
        else:
            self.PVS = niveau
            self.initiative = niveau       

    def attaque(self, adversaire : object):  
        if self.initiative == adversaire.initiative:
            print("Les deux joueurs frappent au même moment !")
            adversaire.PVS = adversaire.PVS - self.niveau
            self.PVS = self.PVS - adversaire.niveau
            if adversaire.PVS <= 0:
                print(f'{adversaire.pseudo} a péri..')
                return 'end'
            elif self.PVS <= 0:
                print(f'{self.pseudo} a péri..')
                return 'end'
            else:
                print(f'{adversaire.pseudo} a {adversaire.PVS} PVs restants..')
                print(f'{self.pseudo} a {self.PVS} PVs restants..')
                return 'continue'
        elif self.initiative > adversaire.initiative:
            print(f'{self.pseudo} attaque ! ')
            adversaire.PVS = adversaire.PVS - self.niveau
            if adversaire.PVS <= 0:
                print(f'{adversaire.pseudo} a péri..')
                return 'end'
            else:
                print(f'{adversaire.pseudo} a {adversaire.PVS} Pvs restants..')
                return 'continue'
        else:
            print(f'{adversaire.pseudo} attaque ! ')
            self.PVS = self.PVS - adversaire.niveau
            if self.PVS <= 0:
                print(f'{self.pseudo} a péri..')
                return 'end'
            else:
                print(f'{self.pseudo} a {self.PVS} Pvs restants..')
                return 'continue'

    def combat(self, adversaire : object):
        while True:
            if self.PVS > 0 and adversaire.PVS > 0:
                self.attaque(adversaire)
            else:
                print("Le combat est terminé")
                break
        
    def soigner(self):
        self.PVS = self.niveau
        print(f'{self.pseudo} s\'est soigné et a maintenant {self.PVS} PVs !')

    def degats(self):
        return self.niveau


