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
    # Liste pour stocker les cartes (chaque carte est représentée par un dictionnaire)
    cards = []

    # Ouvre le fichier 'input.txt' en mode lecture
    with open('input.txt', 'r') as file:
        # Parcours chaque ligne du fichier
        for line in file:
            # Divise la ligne en utilisant le séparateur '|' et récupère les parties
            parts = line.split('|')
            
            # Extrait les numéros gagnants et les numéros du joueur à partir des parties
            winning_numbers = list(map(int, parts[0].split()[2:]))
            your_numbers = list(map(int, parts[1].split()))

            # Ajoute la carte (sous forme de dictionnaire) à la liste
            cards.append({"winning_numbers": winning_numbers, "your_numbers": your_numbers})

    # Liste pour stocker le nombre de copies de chaque carte
    card_copies = [1] * len(cards)

    # Parcours chaque carte
    for i in range(len(cards)):
        # Compte le nombre de correspondances entre les numéros gagnants et les numéros du joueur
        matches = len(set(cards[i]["winning_numbers"]) & set(cards[i]["your_numbers"]))

        # Parcours les cartes suivantes qui ont une correspondance et met à jour le nombre de copies
        for j in range(i + 1, min(i + 1 + matches, len(cards))):
            card_copies[j] += card_copies[i]

    # Retourne la somme des copies de toutes les cartes
    return sum(card_copies)

# Deuxième EXO
resultat_final2 = star_two()
print("exo 2 = " + str(resultat_final2))