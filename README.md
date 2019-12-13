# Rogue_Like_Python
Rogue Like game using Python, by Maxime MARE


Le jeu nécessite seulement les librairies Time and Random
Les fichiers .txt doivent être dans le dossier du projet, avec les python files.

Le jeu :
Vous vous préparez à entrer dans une tour;
votre but est d'en atteindre le sommet en parcourant les différents étages.
Changement de STAGE tous les 5 étages, avec boss et mini-boos (étages x0 et x5)
A chaque changement de stage, il y aura des nouveaux ennemies, stuff, marchands, etc, 

Pour test/debug: décommenter lines 26-27 du Main, donne au player tout les items et max stats
Il faut executer le Main.py


Bug connu :
Bien attendre avant de faire l'input, sinon "error" et exit_run
parfois le jeu bloque en boucle infinie, dans le menu de combat
