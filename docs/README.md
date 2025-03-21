# C'est Qui?

this project is only in French, not in English

Ce projet, commencé en Octobre 2024, est un projet pour jouer à un jeu de société depuis son ordinateur. Avec le jeu C'est Qui vous n'avez même plus besoin de sortir le jeu physique. Le code source du projet est disponible librement sur https://github.com/Nocquet-Gabriel/Projet-NSI .
Ce jeu est la création de 4 personnes, Gabriel Nocquet, Elise Carrouge, Lucas Merlen et Kylian Descamps, pour les Trophées NSI 2025.

Pour l'instant, seul le Mode solo en difficulté Easy est disponible, le Multijoueur sera peut être disponible un jour, ainsi que les autres difficultés.

Le jeu est composé de 18 questions accompagnées de 24 personnages. Dans le mode solo, la personne qui vous bat est "l'ordinateur" : des fonctions se basant sur des attributs booléens permettent à l'ordinateur de comprendre la réponse à une question, poser une question qui n'a  pas été posée, et répondre à l'utilisateur, toujours en fonction du personnage à faire deviner.

Une interface épurée vous sera présentée lorsque vous lancerez le jeu. Il suffit de choisir une question, de la confirmer et l'ordi vous répondra Oui ou Non. A vous de faire les bons choix. Ensuite, c'est le tour de l'ordi. Il vous posera une question. Il agira en fonction de votre réponse. Cela jusqu'à ce que soit l'ordi, soit vous proposiez un personnage. Cela marque la fin du jeu et si le personnage est deviné correctement, le joueur ayant bien deviné gagne la partie, sinon il perd.

Vous devez installer les bibliothèques tkinter et time (normalement déjà présentes avec Python). Si elles ne sont pas présentes, installez les avec

```python
pip install -r requirements.txt
```

Si le code ne fonctionne pas correctement et vous renvoie une erreur de fichier non existant, veuillez vérifier que votre environnement est configuré (que vous avez ouvert un dossier et non un fichier).
