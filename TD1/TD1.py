class Tasse:
    matière : str = 'céramique'
    def __init__(self, couleur : str, contenance : float, marque : str):
        self.attributCouleur = couleur
        self.attributContenance = contenance
        self.attributMarque = marque
    
    def __str__(self) -> str:
        return f'La tasse de matière {self.matière}, de couleur {self.attributCouleur} et de marque {self.attributMarque} a une contenance de {self.attributContenance} ml'

    def remplir_la_tasse(self, contenu):
        self.contenu = contenu
        return print(f'La tasse est désormais rempli de {contenu}, miam miam miam.')
    
    def supprimer_contenu(self):
        del self.contenu
        return print(f'Le contenu de la tasse a bien été vidé')


t = Tasse('bleu', 24.3, 'channel')
print(t)

print('-------------------------------------------')

t.remplir_la_tasse('café')

print('-------------------------------------------')

t.supprimer_contenu()

print('-------------------------------------------')

    