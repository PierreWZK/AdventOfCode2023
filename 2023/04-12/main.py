# Part 1: 15268
# Part 2: 6283755

import re

def star_one():
    # Ouvrir un fichier et en récupérer les lignes
    lines = (open("input.txt")).readlines()

    # Créer les variables qui vont contenir les données
    result = 0
    
    # Code here
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
    numeroLigne = 0
    liste_extension = []
    
    # Code here
    for line in lines :
        numeroLigne += 1
        if numeroLigne > 5:
            break
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
        # print(nombre_gagnant, liste)

        # Suppression des espaces vides
        nombre_gagnant = list(filter(None, nombre_gagnant))
        liste = list(filter(None, liste))

        # Comparaison des nombres gagnants et de la liste
        # Si un nombre gagnant est dans la liste, alors on ajoute 2^n à result (1, 1, 2, 4, 8, 16, 32, 64, 128, 256)
        n = 0
        for i in range(len(liste)):
            if liste[i] in nombre_gagnant:
                n += 1
                nn_gagnant = n_gagnant
                if n_gagnant == -1:
                    nn_gagnant = 0
                result += 2 ** nn_gagnant
                n_gagnant += 1
                
                # Rajouter dans la nouvelle liste liste_extension les cartes qui suive celle actuelle par nombre gagnant
                # Exemple : "Card 1" à 3 bonnes réponses, alors on rajoute "Card 2", "Card 3" et "Card 4" dans la liste
                # On fait ça pour chaque carte
                # On fera le calcul de cette liste après le for line pour ne pas avoir de problème de boucle
                liste_extension.append((open('input.txt').readlines())[numeroLigne + (n-1)])
                
    # Écrire liste_extension dans un fichier 'input2.txt'
    # with open('input2.txt', 'w') as f:
    #     for item in liste_extension:
    #         f.write("%s" % item)
                
    # On fait le calcul de la liste_extension
    for extension in liste_extension:
        # Déclaration des variables
        nombre_gagnant = []
        liste = []
        n_gagnant = -1
        
        # Mise à jour des variables
        extension = extension.replace('\n', '')
        array_lines = extension.split(': ')

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
        n = 0
        for i in range(len(liste)):
            if liste[i] in nombre_gagnant:
                n += 1
                nn_gagnant = n_gagnant
                if n_gagnant == -1:
                    nn_gagnant = 0
                result += 2 ** nn_gagnant
                n_gagnant += 1
    
    return result

# Deuxième EXO
resultat_final2 = star_two()
print("exo 2 = " + str(resultat_final2))