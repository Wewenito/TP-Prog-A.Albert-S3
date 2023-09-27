Procédure de création de doc avec Sphinx : 

1/ Dl Sphinx et ses dépendances :

sudo apt install sphinx 
sudo apt install furo
sudo apt install sphinx-autobuild

2/ Organisation des dossiers :

Placer tout les fichiers de scripts concernés par la doc dans un dossier "src".
Créer au même niveau que le dossier "src" un dossier "docs".

3/ Initialisation de la doc :

Dans un terminal (dans le dossier "docs"), executer la commande :
    - sphinx-quickstart
    - Répondre aux questions (laisser la valeur par défaut en cas de doute)

Des sous-dossiers & fichiers devraient avoir été créés au sein de "docs"

3/ Editer le fichier "conf.py" :

Dans la liste vide d'extensions, ajouter les extensions suivantes;
    - "sphinx.ext.autodoc",
    - "sphinx.ext.viewcode",

En debut de fichier, ajouter les lignes ci dessous : 

import os
import sys
sys.path.insert(0, os.path.abspath("../src"))

Modifier ensuite le thème HTML par "furo"

4/ Initialisation du dossier src :

Dans un terminal, dans le dossier "src", taper la commande :
    - sphinx-apidoc -o docs src

Dans le fichier 'index.rst' : 
    - ajouter 'modules' dans la partie "..toctree::" a la fin du bloc avec une     ligne vide avant


5/ Création de la doc :

Dans un terminal, au niveau du dossier "docs", taper la commande :
    - make html

La doc devrait maintenant être disponible dans "docs/-build/html/"