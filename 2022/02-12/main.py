import re

def star_one():
    # Ouvrir un fichier et en récupérer les lignes
    lines = (open("input.txt")).readlines()

    # Créer les variables qui vont contenir les données
    result = 0
    
    # Pattern pour calculer combien on gagne ou on perd
    # A->Pierre, B->Feuille, C->Ciseaux
    # X->Pierre, Y->Feuille, Z->Ciseaux
    # Nous les X, Y et Z
    # Pierre vaux 1 point, Feuille vaux 2 points, Ciseaux vaux 3 points
    # Si on perd on gagne 0 point, si on a égalité on gagne 3 points et si on gagne on gagne 6 point
    # On additionne ce qu'on gagne et ce la valeur de ce qu'on joue
    map_table = {
        'A X': 4, # Pierre vs Pierre
        'B X': 1, # Feuille vs Pierre
        'C X': 7, # Ciseaux vs Pierre
        'A Y': 8, # Pierre vs Feuille
        'B Y': 5, # Feuille vs Feuille
        'C Y': 2, # Ciseaux vs Feuille
        'A Z': 3, # Pierre vs Ciseaux
        'B Z': 9, # Feuille vs Ciseaux
        'C Z': 6, # Ciseaux vs Ciseaux
    }
    
    for line in lines:
        # Tu compile le pattern pour récupérer les deux lettres
        pattern = re.compile(r'([A-Z])')
        letters = pattern.findall(line)
        letters = ' '.join(letters)
        result += map_table[letters]
    
    return result

# Premier EXO
resultat_final = star_one()
print("exo 1 = " + str(resultat_final))

#####################################################################################################

import re

def star_two():
    # Ouvrir un fichier et en récupérer les lignes
    lines = (open("input.txt")).readlines()

    # Créer les variables qui vont contenir les données
    result = 0
    
    # Pattern pour calculer combien on gagne ou on perd
    # A->Pierre, B->Feuille, C->Ciseaux
    # X->perdre, Y->nul, Z->gagner
    # Pierre vaux 1 point, Feuille vaux 2 points, Ciseaux vaux 3 points
    # Si on perd on gagne 0 point, si on a égalité on gagne 3 points et si on gagne on gagne 6 point
    # On additionne ce qu'on gagne et ce la valeur de ce qu'on joue
    map_table = {
        'A X': 3, # Pierre -> perdu (ciseaux)
        'B X': 1, # Feuille -> perdu (pierre)
        'C X': 2, # Ciseaux -> perdu (feuille)
        'A Y': 4, # Pierre -> nul (pierre)
        'B Y': 5, # Feuille -> nul (feuille)
        'C Y': 6, # Ciseaux -> nul (ciseaux)
        'A Z': 8, # Pierre -> gagner (feuille)
        'B Z': 9, # Feuille -> gagner (ciseaux)
        'C Z': 7, # Ciseaux -> gagner (pierre)
    }
    
    for line in lines:
        # Tu compile le pattern pour récupérer les deux lettres
        pattern = re.compile(r'([A-Z])')
        letters = pattern.findall(line)
        letters = ' '.join(letters)
        result += map_table[letters]
    
    return result

# Deuxième EXO
resultat_final2 = star_two()
print("exo 2 = " + str(resultat_final2))