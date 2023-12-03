import re

def star_one():
    # Ouvrir un fichier et en récupérer les lignes
    lines = open("input.txt").read().splitlines()

    # Créer les variables qui vont contenir les données
    result = 0
    
    # Obtenir la hauteur et la largeur de la grille    
    height = len(lines)
    width = len(lines[0])
    
    # Pour chaque ligne et caractère dans la grille
    for y1 in range(height):
        # Utiliser un itérateur pour parcourir les colonnes
        xIter = iter(range(width))
        for x1 in xIter:
            # Si le caractère est un chiffre
            if lines[y1][x1].isdigit():
                # x1 représente le début du nombre, endX1 représente la fin du nombre
                endX1 = next(xIter, width)
                # Trouver la fin du nombre
                while endX1 < width and lines[y1][endX1].isdigit():
                    endX1 = next(xIter, width)
                
                # Fonction pour trouver les nombres adjacents à des symboles
                def trouver_caractere():
                    for y in range(y1 - 1, min(y1 + 2, height)):
                        for x in range(x1 - 1, min(endX1 + 1, width)):
                            # Vérifier si le caractère est un symbole et non un chiffre
                            if lines[y][x] != '.' and not lines[y][x].isdigit():
                                return True
                                
                # Si des nombres adjacents sont trouvés, ajouter le nombre au résultat total
                if trouver_caractere():
                    result += int(lines[y1][x1:endX1])
    
    return result

# Premier EXO
resultat_final = star_one()

# RESULT ATTENDU : 514969
print("exo 1 = " + str(resultat_final))

#####################################################################################################

def star_two():
    # Ouvrir un fichier et en récupérer les lignes
    lines = open("input.txt").read().splitlines()

    # Variable created
    result = 0
    
    # Obtenir la hauteur et la largeur de la grille
    hauteur = len(lines)
    largeur = len(lines[0])

    # Initialiser un dictionnaire pour stocker les engrenages et leurs valeurs
    engrenages = {}

    # Pour chaque ligne et caractère dans la grille
    for y1 in range(hauteur):
        # Utiliser un itérateur pour parcourir les colonnes
        xIter = iter(range(largeur))
        for x1 in xIter:
            # Si le caractère est un chiffre
            if lines[y1][x1].isdigit():
                # x1 représente le début du nombre, x2 représente la fin du nombre
                x2 = next(xIter, largeur)
                # Trouver la fin du nombre
                while x2 < largeur and lines[y1][x2].isdigit():
                    x2 = next(xIter, largeur)

                # Trouver les engrenages adjacents
                for y in range(y1 - 1, min(y1 + 2, hauteur)):
                    for x in range(x1 - 1, min(x2 + 1, largeur)):
                        if lines[y][x] == '*':
                            # Ajouter la valeur du nombre à l'engrenage correspondant dans le dictionnaire
                            if (y, x) not in engrenages:
                                engrenages[(y, x)] = []
                            engrenages[(y, x)].append(int(lines[y1][x1:x2]))

    # Compter les engrenages incorrects
    for valeurs in engrenages.values():
        if len(valeurs) > 1:
            ratio = 1
            for valeur in valeurs:
                ratio *= valeur
            result += ratio

    return result

# Deuxième EXO
resultat_final2 = star_two()

# RESULT ATTENDU : 78915902
print("exo 2 = " + str(resultat_final2))