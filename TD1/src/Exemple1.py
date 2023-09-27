def affiche(string):
    print(f'texte à afficher: {string}')


class Velo:
    vitesse : int = 1
    def __init__(self, marque : str, taille_pneu : float, couleur : str, nombre_vitesse : int):
        self.marque = marque
        self.taille_pneu = taille_pneu
        self.couleur = couleur
        self.nombre_vitesse = nombre_vitesse

    def gear_up(self):
        if self.nombre_vitesse == self.vitesse:
            return print('Vous n\'avez plus de vitesse dispo')
        else:
            self.vitesse = self.vitesse + 1
            return print(f'vous etes maintenant a la vitesse {self.vitesse}/{self.nombre_vitesse}')

    def gear_down(self):
        if self.vitesse == 1:
            return print('Vous etes a la vitesse minimum')
        else:
            self.vitesse = self.vitesse - 1
            return print(f'vous etes maintenant a la vitesse {self.vitesse}/{self.nombre_vitesse}')

        

def Main():
    str1 = 'LOREM IPSUM LALALALAL'

    affiche(str1)

    v1.gear_up()
    v1.gear_up()
    v1.gear_down()

    print(v1.vitesse) # == 2




v1 = Velo('Quick Silver', 12.3, 'bleu', 3)



Main()