def star_one():
    # Ouvrir un fichier et en récupérer les lignes
    lines = (open("input.txt")).readlines()

    # Créer les variables qui vont contenir les données
    numLutin = 0
    result = [0]
    
    # Parcourir les lignes du fichier
    for line in lines: 
        # On calcule tout les nombres qui sont séparé avec une ligne vide
        # On regarde si la prochaine ligne est vide
        if line == "\n":
            numLutin += 1
            result.append(0)
            continue
        
        # On additionne le nombre de la ligne à la liste
        result[numLutin] += int(line)
        
    return max(result)

# Premier EXO
resultat_final = star_one()
print("exo 1 = " + str(resultat_final))

#####################################################################################################

import re

def star_two():
    # Ouvrir un fichier et en récupérer les lignes
    lines = (open("input.txt")).readlines()

    # Créer les variables qui vont contenir les données
    numLutin = 0
    tab = [0]
    result = 0
    
    
    # Parcourir les lignes du fichier
    for line in lines: 
        # On calcule tout les nombres qui sont séparé avec une ligne vide
        # On regarde si la prochaine ligne est vide
        if line == "\n":
            numLutin += 1
            tab.append(0)
            continue
        
        # On additionne le nombre de la ligne à la liste
        tab[numLutin] += int(line)
    
    # Récupérer le numéro de la ligne qui est la plus grande
    for i in range (3):
        index = tab.index(max(tab))
        result += int(tab[index])
        tab.pop(index)
    
    return result

# Deuxième EXO
resultat_final2 = star_two()
print("exo 2 = " + str(resultat_final2))