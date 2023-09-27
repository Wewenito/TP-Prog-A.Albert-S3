from Personnage import Personnage

class Joueur:
    def __init__(self, nom : str, maximum : int = 3):
        self.nom = nom
        self.maximum = maximum
        self.personnages = []

    def ajout_perso(self, perso : object):
        print(f'La liste contient actuellement {len(self.personnages)} personnages.')
        if len(self.personnages) + 1 <= self.maximum:
            self.personnages.append(perso)
            print(f'Le personnage {perso.pseudo} a été associé au joueur {self.nom}\n')
        else:
            print("Le nombre maximum de personnages associé au joueur est déjà atteinte !\n")
            pass

    def acces_perso_1(self, num : int):
        try:
            perso = self.personnages[num]
            return perso
        except Exception as e:
            print("Personnage non-existant dans la liste du joueur")

            #print(e)#Useful only in debugging

    def acces_perso_2(self, nom : str):
        for item in self.personnages:
            if item.pseudo == nom:
                print("Personnage récupéré !")
                return item
            else:
                pass
        
        print("Personnage non-existant dans la liste du joueur")
            
    def acces_perso_3(self, perso : object):
        for item in self.personnages:
            if item == perso:
                print("Personnage récupéré !")
                return item
            else:
                pass
        
        print("Personnage non-existant dans la liste du joueur")

    def del_perso_1(self, num : int):
        try:
            x = self.personnages[num].pseudo
            self.personnages.pop(num)
            print(f'Le personnage {x} a été supprimé de la liste du joueur')
        except Exception as e:
            print("Personnage à supprimer non-existant dans la liste du joueur")

            #print(e)#Useful only in debugging

    def del_perso_2(self, nom : str):
        for item in self.personnages:
            if item.pseudo == nom:
                x = item.pseudo
                self.personnages.remove(item)
                print(f'Le personnage {x} a été supprimé de la liste du joueur')
                return x
            else:
                pass
        
        print("Personnage à supprimer non-existant dans la liste du joueur")

    def del_perso_3(self, perso : object):
        for item in self.personnages:
            if item == perso:
                x = item.pseudo
                self.personnages.remove(item)
                print(f'Le personnage {x} a été supprimé de la liste du joueur')
                return x
            else:
                pass

        print("Personnage à supprimer non-existant dans la liste du joueur")

    def del_tt_les_persos(self):
        self.personnages.clear()
    