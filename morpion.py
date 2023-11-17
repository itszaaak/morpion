def afficherGrille(grille):
    for ligne in grille:
        print(" | ".join(ligne))
        print("-" * 9)

def jouerCoup(grille, joueur, ligne, colonne):
    if grille[ligne][colonne] == " ":
        grille[ligne][colonne] = joueur
        return True
    else:
        return False        

def verifierVictoire(grille, joueur):  #on verifie les lignes/colonnes et les diagonales
    for i in range(3):              #taille grille 3x3
        if all(grille[i][j] == joueur for j in range(3)) or \
           all(grille[j][i] == joueur for j in range(3)):
            return True
    if all(grille[i][i] == joueur for i in range(3)) or \
       all(grille[i][2 - i] == joueur for i in range(3)):
        return True
    return False

def morpion():
    joueur1 = input("initiale nom joueur 1 : ")
    joueur2 = input("initiale nom joueur 2 : ")
    scores = {joueur1: 0, joueur2: 0, "Matchs nuls": 0}
    
    while True:
        grille = [[" " for _ in range(3)] for _ in range(3)] 
        tour = 1

        while True:
            afficherGrille(grille)
            joueur = joueur1 if tour % 2 == 1 else joueur2
            print(f"{joueur}, c'est à vous.")
            ligne = int(input("Entrez le numéro de ligne (0, 1 ou 2) : "))
            colonne = int(input("Entrez le numéro de colonne (0, 1 ou 2) : "))

            if 0 <= ligne < 3 and 0 <= colonne < 3:
                if jouerCoup(grille, joueur, ligne, colonne):
                    tour += 1
                    if tour > 4:  # La victoire est possible après 5 tours
                        if verifierVictoire(grille, joueur):
                            scores[joueur] += 1
                            print(f"{joueur} gagne !")
                            break
                    if tour == 10:
                        scores["Matchs nuls"] += 1
                        print("Match nul !")
                        break
                else:
                    print("Cette case est déjà prise. Réessayez.")
            else:
                print("Ligne ou colonne invalide. Réessayez.")

        continuer = input("Voulez-vous refaire une partie ? (oui/non) : ").lower()
        if continuer != "oui":
            break

    print(f"Nombre de parties jouées : {tour // 2}")
    print(f"Nombre de parties gagnées par {joueur1} : {scores[joueur1]}")
    print(f"Nombre de parties gagnées par {joueur2} : {scores[joueur2]}")
    print(f"Nombre de matchs nuls : {scores['Matchs nuls']}")


# appel fonction
morpion()