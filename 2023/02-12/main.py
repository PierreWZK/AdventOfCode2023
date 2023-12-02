import re

def star_one():
    # Ouvrir un fichier et en récupérer les lignes
    lines = (open("input.txt")).readlines()

    # Créer les variables qui vont contenir les données
    result = 0
    idLine = 0
    
    for line in lines :
        idLine += 1
        
        # Intialize variables
        isPossible = True
        
        # On sépare chaque couleur de la ligne et le montant. On supprime le premier élément qui est l'id de la ligne
        game = re.split("; |: |\n", line)
        game.pop(0)
        game.pop(len(game)-1)
        # print(game)
        for round in game :
            round = re.split(", ", round)
            
            # Intialize variables
            rouge = 0
            vert = 0
            bleu = 0
            
            for l in round:
                l = re.split(' ', l)                    
                if l[1] == "red":
                    rouge += int(l[0])
                elif l[1] == "green":
                    vert += int(l[0])
                elif l[1] == "blue":
                    bleu += int(l[0])
            if rouge > 12 or vert > 13 or bleu > 14:
                isPossible = False
        if isPossible:
            result += idLine

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
    
    for line in lines :        
        # On sépare chaque couleur de la ligne et le montant. On supprime le premier élément qui est l'id de la ligne
        game = re.split("; |: |\n", line)
        game.pop(0)
        game.pop(len(game)-1)
        
        # Intialize variables
        rouge = 0
        vert = 0
        bleu = 0
        
        for round in game :
            round = re.split(", ", round)
            
            for l in round:
                l = re.split(' ', l)
                if l[1] == "red":
                    if rouge < int(l[0]):
                        rouge = int(l[0])
                elif l[1] == "green":
                    if vert < int(l[0]):
                        vert = int(l[0])
                elif l[1] == "blue":
                    if bleu < int(l[0]):
                        bleu = int(l[0])
            #End for l in round
            
        result += (rouge * vert * bleu)
        #End for round in game
    
    return result

# Deuxième EXO
resultat_final2 = star_two()
print("exo 2 = " + str(resultat_final2))