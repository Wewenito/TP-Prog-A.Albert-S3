import Personnage as P
import Guerrier as G
import Mage as M
import Joueur as J


def Test_complet_du_script():
#    +==========================================================================================+
#    |                                                                                          |
#    |                       TEST PERSOS DE BASES ET LEURS METHODES                             |
#    |                                                                                          |
#    +==========================================================================================+
    print('\n')
    print("+==========================================================================================+")
    print("|                       TEST PERSOS DE BASES ET LEURS METHODES                             |")
    print("+==========================================================================================+")

    print("Création de deux personnages de base : \n")
    
    Perso1 = P.Personnage('John', 5)
    Perso1.set_attr("initiative", 19)
    Perso2 = P.Personnage('Bryan', 18)

    print("P1 :")
    print(f'Pseudo P1 : {Perso1.get_attr("pseudo")}')
    print(f'niveau P1 : {Perso1.get_attr("niveau")}')
    print(f'Pv P1 : {Perso1.get_attr("PVS")}')
    print(f'initiative P1 : {Perso1.get_attr("initiative")}\n')

    print("P2 :")
    print(f'Pseudo P2 : {Perso2.get_attr("pseudo")}')
    print(f'niveau P2 : {Perso2.get_attr("niveau")}')
    print(f'Pv P2 : {Perso2.get_attr("PVS")}')
    print(f'initiative P2 : {Perso2.get_attr("initiative")}\n\n')

    print("Attaque entre deux persos de bases : \n")
    Perso1.attaque(Perso2)

    print("\n\nUtilisation de soins par le joueur 2 : \n")
    Perso2.soigner()

    print("\n\nTest pour voir combien de dégats peut potentiellement infliger Joueur 1 : \n")
    print(f"{Perso1.get_attr('pseudo')} peut infliger {Perso1.degats()} de degats à {Perso2.get_attr('pseudo')}. \n\n")

    print("Lancement d'un combat entre deux personnages : \n")
    Perso1.combat(Perso2)

#    +==========================================================================================+
#    |                                                                                          |
#    |                           TESTS GUERRIERS & MAGES + COMBAT                               |
#    |                                                                                          |
#    +==========================================================================================+
    print('\n')
    print("+==========================================================================================+")
    print("|                           TESTS GUERRIERS & MAGES + COMBAT                               |")
    print("+==========================================================================================+")

    print("Création d'un Guerrier puis d'un mage : \n")
    Perso3 = G.Guerrier('Ragnar', 3)
    Perso4 = M.Mage('Merlin', 3)

    print("P3 (Guerrier) :")
    print(f'Pseudo P3 : {Perso3.get_attr("pseudo")}')
    print(f'niveau P3 : {Perso3.get_attr("niveau")}')
    print(f'Pv P3 : {Perso3.get_attr("PVS")}')
    print(f'init P3 : {Perso3.get_attr("initiative")}\n\n')

    print("P4 (Mage) :")
    print(f'Pseudo P4 : {Perso4.get_attr("pseudo")}')
    print(f'niveau P4 : {Perso4.get_attr("niveau")}')
    print(f'Pv P4 : {Perso4.get_attr("PVS")}')
    print(f'Mana P4 : {Perso4.get_attr("mana")}')
    print(f'init P4 : {Perso4.get_attr("initiative")}\n\n')

    print("Lancement d'un combat entre les deux personnages de différentes classes : \n")
    Perso3.combat(Perso4)

#    +==========================================================================================+
#    |                                                                                          |
#    |                      TEST DEGATS EN FONCTION DU TYPE DE PERSOS                           |
#    |                                                                                          |
#    +==========================================================================================+
    print('\n')
    print("+==========================================================================================+")
    print("|                      TEST DEGATS EN FONCTION DU TYPE DE PERSOS                           |")
    print("+==========================================================================================+")

    print("\n\nVérification du type de dégats en fonction du type de personnage : \n")
    print(f"Degats occasionnés par un Perso de base de niveau 5 : {Perso1.degats()}")

    print(f"\nDegats occasionnés par un Perso de base de niveau 18 : {Perso2.degats()}")

    print(f"\nDegats occasionnés par un guerrier de niveau 3 : {Perso3.degats()}")

    print(f"\nDegats occasionnés par un mage de niveau 3 : {Perso4.degats()}")

#    +==========================================================================================+
#    |                                                                                          |
#    |                      TEST JOUEURS ET MANIPS DES PERSOS ASSOCIES                          |
#    |                                                                                          |
#    +==========================================================================================+
    print('\n')
    print("+==========================================================================================+")
    print("|                      TEST JOUEURS ET MANIPS DES PERSOS ASSOCIES                          |")
    print("+==========================================================================================+")

    print("\n\nCréation d'un joueur (Hugo), avec taille max de liste de 3 : \n")
    Joueur1 = J.Joueur('Hugo', 3)

    print("Ajout de Perso1 & Perso 3 à la liste du joueur : \n")  

    Joueur1.ajout_perso(Perso1)
    Joueur1.ajout_perso(Perso3)

    print("\n\nImpression du nom de perso 3 via la liste du joueur et l'id du perso : ")
    print(Joueur1.acces_perso_1(1).get_attr("pseudo"))
    print("\n\nImpression du nom de perso 3 via la liste du joueur et le pseudo du perso : ")
    print(Joueur1.acces_perso_2('Ragnar').get_attr("pseudo"))
    print("\n\nImpression du nom de perso 3 via la liste du joueur et l'objet du perso : ")
    print(Joueur1.acces_perso_3(Perso3).get_attr("pseudo"))

    print("\n\nSuppression du perso 3 via son id : ")
    Joueur1.del_perso_1(1)

    print("\nSuppression du perso 1 via son pseudo : ")
    Joueur1.del_perso_2('John')

    print("Script done, error raised during execution : 0")


if __name__ =="__main__":
    Test_complet_du_script()
    

