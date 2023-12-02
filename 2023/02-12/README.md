# Jour 2 : Énigme des Cubes

## Partie Un

Vous êtes propulsé haut dans l'atmosphère ! L'apex de votre trajectoire atteint à peine la surface d'une grande île flottant dans le ciel. Vous atterrissez doucement dans une pile moelleuse de feuilles. Il fait assez froid, mais vous ne voyez pas beaucoup de neige. Un Elfe court vers vous.

L'Elfe explique que vous êtes arrivé sur l'île de la Neige et s'excuse pour le manque de neige. Il sera heureux d'expliquer la situation, mais c'est un peu de marche, donc vous avez du temps. Ils n'ont pas beaucoup de visiteurs ici; voudriez-vous jouer à un jeu en attendant?

Pendant que vous marchez, l'Elfe vous montre un petit sac et des cubes qui sont soit rouges, verts ou bleus. Chaque fois que vous jouez à ce jeu, il cachera un nombre secret de cubes de chaque couleur dans le sac, et votre objectif est de découvrir des informations sur le nombre de cubes.

Pour obtenir des informations, une fois qu'un sac a été chargé de cubes, l'Elfe plongera sa main dans le sac, saisira une poignée de cubes au hasard, vous les montrera, puis les remettra dans le sac. Il fera cela quelques fois par partie.

Vous jouez plusieurs parties et enregistrez les informations de chaque partie (votre entrée d'énigme). Chaque partie est répertoriée avec son numéro d'ID (comme le 11 dans Partie 11 : ...) suivi d'une liste séparée par des points-virgules des sous-ensembles de cubes qui ont été révélés du sac (comme 3 rouges, 5 verts, 4 bleus).

Par exemple, le compte rendu de quelques parties pourrait ressembler à ceci :

Partie 1 : 3 bleus, 4 rouges ; 1 rouge, 2 verts, 6 bleus ; 2 verts
Partie 2 : 1 bleu, 2 verts ; 3 verts, 4 bleus, 1 rouge ; 1 vert, 1 bleu
Partie 3 : 8 verts, 6 bleus, 20 rouges ; 5 bleus, 4 rouges, 13 verts ; 5 verts, 1 rouge
Partie 4 : 1 vert, 3 rouges, 6 bleus ; 3 verts, 6 rouges ; 3 verts, 15 bleus, 14 rouges
Partie 5 : 6 rouges, 1 bleu, 3 verts ; 2 bleus, 1 rouge, 2 verts

Dans le jeu 1, trois ensembles de cubes sont révélés du sac (et sont ensuite remis en place). Le premier ensemble est constitué de 3 cubes bleus et 4 cubes rouges ; le deuxième ensemble est constitué de 1 cube rouge, 2 cubes verts et 6 cubes bleus ; le troisième ensemble est constitué uniquement de 2 cubes verts.

L'Elfe aimerait d'abord savoir quels jeux auraient été possibles si le sac ne contenait que 12 cubes rouges, 13 cubes verts et 14 cubes bleus?

Dans l'exemple ci-dessus, les jeux 1, 2 et 5 auraient été possibles si le sac avait été chargé avec cette configuration. Cependant, le jeu 3 aurait été impossible car à un moment l'Elfe vous a montré 20 cubes rouges à la fois; de même, le jeu 4 aurait également été impossible car l'Elfe vous a montré 15 cubes bleus à la fois. Si vous additionnez les ID des jeux qui auraient été possibles, vous obtenez 8.

Déterminez quels jeux auraient été possibles si le sac n'avait été chargé qu'avec 12 cubes rouges, 13 cubes verts et 14 cubes bleus. Quelle est la somme des ID de ces jeux?

```markdown
Résultat: 2593
```

## Partie Deux

L'Elfe dit qu'ils ont cessé de produire de la neige parce qu'ils n'obtiennent pas d'eau ! Il n'est pas sûr pourquoi l'eau s'est arrêtée; cependant, il peut vous montrer comment accéder à la source d'eau pour vérifier par vous-même. C'est juste là devant !

Pendant que vous continuez votre promenade, l'Elfe pose une deuxième question : dans chaque jeu auquel vous avez joué, quel est le nombre minimum de cubes de chaque couleur qui aurait pu être dans le sac pour rendre le jeu possible ?

Considérez à nouveau les jeux d'exemple ci-dessus :

Partie 1 : 3 bleus, 4 rouges ; 1 rouge, 2 verts, 6 bleus ; 2 verts
Partie 2 : 1 bleu, 2 verts ; 3 verts, 4 bleus, 1 rouge ; 1 vert, 1 bleu
Partie 3 : 8 verts, 6 bleus, 20 rouges ; 5 bleus, 4 rouges, 13 verts ; 5 verts, 1 rouge
Partie 4 : 1 vert, 3 rouges, 6 bleus ; 3 verts, 6 rouges ; 3 verts, 15 bleus, 14 rouges
Partie 5 : 6 rouges, 1 bleu, 3 verts ; 2 bleus, 1 rouge, 2 verts

Dans le jeu 1, le jeu aurait pu être joué avec un minimum de 4 cubes rouges, 2 cubes verts et 6 cubes bleus. Si une couleur avait ne serait-ce qu'un cube de moins, le jeu aurait été impossible. 
Le jeu 2 aurait pu être joué avec un minimum de 1 rouge, 3 verts et 4 cubes bleus.
Le jeu 3 aurait dû être joué avec au moins 20 cubes rouges, 13 cubes verts et 6 cubes bleus.
Le jeu 4 nécessitait au moins 14 cubes rouges, 3 cubes verts et 15 cubes bleus.
Le jeu 5 n'avait besoin d'aucun moins de 6 cubes rouges, 3 cubes verts et 2 cubes bleus dans le sac.

La puissance d'un ensemble de cubes est égale au produit des nombres de cubes rouges, verts et bleus. La puissance de l'ensemble minimum de cubes dans le jeu 1 est de 48. Dans les jeux 2 à 5, elle était de 12, 1560, 630 et 36 respectivement. L'addition de ces cinq puissances donne la somme 2286

```markdown
Résultat: 54699
```