# Part 1: 15268
# Part 2: 6283755

import re

def star_one():
    # Ouvrir un fichier et en récupérer les lignes
    lines = (open("input.txt")).readlines()

    # Créer les variables qui vont contenir les données
    result = 0
    
    for line in lines :
        # Déclaration des variables
        nombre_gagnant = []
        liste = []
        n_gagnant = -1
        
        # Mise à jour des variables
        line = line.replace('\n', '')
        array_lines = line.split(': ')

        # Récupération des nombres gagnants et de la liste
        AllNumbers = array_lines[1]
        nombre_gagnant = AllNumbers.split(' | ')[0]
        nombre_gagnant = nombre_gagnant.split(' ')
        liste = AllNumbers.split(' | ')[1]
        liste = liste.split(' ')

        # Suppression des espaces vides
        nombre_gagnant = list(filter(None, nombre_gagnant))
        liste = list(filter(None, liste))

        # Comparaison des nombres gagnants et de la liste
        # Si un nombre gagnant est dans la liste, alors on ajoute 2^n à result (1, 1, 2, 4, 8, 16, 32, 64, 128, 256)
        for i in range(len(liste)):
            if liste[i] in nombre_gagnant:
                nn_gagnant = n_gagnant
                if n_gagnant == -1:
                    nn_gagnant = 0
                result += 2 ** nn_gagnant
                n_gagnant += 1
    
    return result

# Premier EXO
resultat_final = star_one()
print("exo 1 = " + str(resultat_final))

#####################################################################################################

def star_two():
    # Ouvrir un fichier et en récupérer les lignes
    lines = (open("input.txt")).readlines()

    # Créer les variables qui vont contenir les données
    result = 0
    
    
    return result

# Deuxième EXO
resultat_final2 = star_two()
print("exo 2 = " + str(resultat_final2))