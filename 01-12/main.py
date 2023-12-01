def star_one():
    # Ouvrir un fichier et en récupérer les lignes
    lines = (open("input.txt")).readlines()

    # Créer les variables qui vont contenir les données
    result = 0

    # Parcourir les lignes du fichier
    for line in lines:
        # On récupère le dernier chiffre de la ligne (une ligne peut-être sous cette forme : fglpbone79fourvrgcmgklbmthree)
        first_digit = ''.join(filter(str.isdigit, line))[0]
        last_digit = ''.join(filter(str.isdigit, line))[-1]

        # On combine les deux chiffres et on l'additionne au résultat
        result += int(str(first_digit) + str(last_digit))

    return result

# Premier EXO
resultat_final = star_one()
print(resultat_final)

#####################################################################################################

import re

def star_two():
    # Dictionnaire de correspondance entre les mots écrits en lettres et les chiffres
    map_table = {
        'one': 1, '1': 1,
        'two': 2, '2': 2,
        'three': 3, '3': 3,
        'four': 4, '4': 4,
        'five': 5, '5': 5,
        'six': 6, '6': 6,
        'seven': 7, '7': 7,
        'eight': 8, '8': 8,
        'nine': 9, '9': 9
    }

    # Créer un motif de recherche avec des alternatives pour chaque mot du dictionnaire
    pattern = re.compile(f'(?=({"|".join(map_table)}))')
    
    # Initialiser la variable pour stocker la somme totale
    total = 0
    
    # Parcourir chaque ligne du fichier
    for line in open('input2.txt'):
        # Extraire les valeurs correspondant aux mots écrits en lettres
        values = [map_table[v] for v in re.findall(pattern, line)]
        
        # Calculer le total en ajoutant le premier chiffre multiplié par 10 et le dernier chiffre
        total += values[0] * 10 + values[-1]
        
    # Retourner la somme totale
    return total

# Deuxième EXO
# resultat_final2 = star_two()
# print(resultat_final2)