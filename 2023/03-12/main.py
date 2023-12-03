import re

def star_one():
    # Ouvrir un fichier et en récupérer les lignes
    lines = (open("input.txt")).readlines()

    # Créer les variables qui vont contenir les données
    result = 0
    
    for line in lines: 
        1
    # Additionnez les pieces de moteurs qui ont un numéro de série
    
    return result

# Premier EXO
resultat_final = star_one()

# RESULT ATTENDU : 514969
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

# RESULT ATTENDU : 78915902
print("exo 2 = " + str(resultat_final2))

grid = open("input.txt").read().splitlines()
cs = set()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch.isdigit() or ch == ".":
            continue
        for dr in range(r - 1, r + 2):
            for dc in range(c - 1, c + 2):
                if dr < 0 or dr >= len(grid) or dc < 0 or dc >= len(grid[dr]) or not grid[dr][dc].isdigit():
                    continue
                while dc > 0 and grid[dr][dc - 1].isdigit():
                    dc -= 1
                cs.add((dr, dc))

ns = []

for r, c in cs:
    s = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        s += grid[r][c]
        c += 1
    ns.append(int(s))

print(sum(ns))