def morpion():
    
    coordonnée = [1, 2, 3]
    remake = "Q"
    while remake == "Q":
        print("Voici un Morpion : entrez les coordonnées pour placez votre coup:")
        # INITIALISATION DU PLATEAU DE MORPION
        morpion = [
        [ None, None, None],
        [ None, None, None],
        [ None, None, None]
        ]
        for i in range(len(morpion)):
                print(f"{morpion[i]}")

        try:
            for loop in range(9) :    
                
                # Tour du JOUEUR 1
                joueur1Colonne = None
                joueur1Ligne = None
                print("Tour de Joueur 1")
                while joueur1Colonne not in coordonnée and joueur1Ligne not in coordonnée:
                    joueur1Colonne = int(input("Colonne : "))
                    joueur1Ligne = int(input("Ligne : "))
                if morpion[joueur1Ligne-1][joueur1Colonne-1] == 'O' or morpion[joueur1Ligne-1][joueur1Colonne-1] == 'X':    
                    while morpion[joueur1Ligne-1][joueur1Colonne-1] == 'O' or morpion[joueur1Ligne-1][joueur1Colonne-1] == 'X':
                        joueur1Colonne = int(input("Colonne : "))
                        joueur1Ligne = int(input("Ligne : "))
                morpion[joueur1Ligne-1][joueur1Colonne-1] = 'X'
                
                # VERIFICATION SUR L'ETAT DU JEU
                if morpion[0].count("X") == 3 or morpion[1].count("X") == 3 or morpion[2].count("X") == 3:
                    for i in range(len(morpion)):
                        print(f"{morpion[i]}")
                    print("Joueur 1 a gagné la partie")
                    remake = input("Voulez vous rejouer ? Oui : Press Q si Non : Press Enter ")
                    if remake != "Q":
                        return
                
                elif (morpion[0][0] == 'X' and morpion[1][1] == 'X' and morpion[2][2] == 'X') or (morpion[2][0] == 'X' and morpion[1][1] == 'X' and morpion[0][2] == 'X'):
                    for i in range(len(morpion)):
                        print(f"{morpion[i]}")
                    print("Joueur 1 a gagné la partie")
                    remake = input("Voulez vous rejouer ? Oui : Press Q si Non : Press Enter ")
                    if remake != "Q":
                        return
                
                elif (morpion[0][0] == 'X' and morpion[1][0] == 'X' and morpion[2][0] == 'X') or (morpion[0][1] == 'X' and morpion[1][1] == 'X' and morpion[2][1] == 'X') or (morpion[0][2] == 'X' and morpion[1][2] == 'X' and morpion[2][2] == 'X'):
                    for i in range(len(morpion)):
                        print(f"{morpion[i]}")
                    print("Joueur 1 a gagné la partie")
                    remake = input("Voulez vous rejouer ? Oui : Press Q si Non : Press Enter ")
                    if remake != "Q":
                        return
                
                for i in range(len(morpion)):
                    print(f"{morpion[i]}")

                # TOUR DU JOUEUR 2
                
                print("Tour de Joueur 2")
                joueur1Colonne = None
                joueur1Ligne = None
                while joueur1Colonne not in coordonnée and joueur1Ligne not in coordonnée :
                    joueur1Colonne = int(input("Colonne : "))
                    joueur1Ligne = int(input("Ligne : "))
                if morpion[joueur1Ligne-1][joueur1Colonne-1] == 'X' or morpion[joueur1Ligne-1][joueur1Colonne-1] == 'O':    
                    while morpion[joueur1Ligne-1][joueur1Colonne-1] == 'X' or morpion[joueur1Ligne-1][joueur1Colonne-1] == 'O':
                        joueur1Colonne = int(input("Colonne : "))
                        joueur1Ligne = int(input("Ligne : "))
                morpion[joueur1Ligne-1][joueur1Colonne-1] = 'O'
                
                # VERIFICATION SUR L'ETAT DU JEU
                if morpion[0].count("O") == 3 or morpion[1].count("O") == 3 or morpion[2].count("O") == 3:
                    for i in range(len(morpion)):
                        print(f"{morpion[i]}")
                    print("Joueur 2 a gagné la partie")
                    remake = input("Voulez vous rejouer ? Oui : Press Q si Non : Press Enter ")
                    if remake != "Q":
                        return
                
                elif (morpion[0][0] == 'O' and morpion[1][1] == 'O' and morpion[2][2] == 'O') or (morpion[2][0] == 'O' and morpion[1][1] == 'O' and morpion[0][2] == 'O'):
                    for i in range(len(morpion)):
                        print(f"{morpion[i]}")
                    print("Joueur 1 a gagné la partie")
                    remake = input("Voulez vous rejouer ? Oui : Press Q si Non : Press Enter ")
                    if remake != "Q":
                        return
                
                elif (morpion[0][0] == 'O' and morpion[1][0] == 'O' and morpion[2][0] == 'O') or (morpion[0][1] == 'O' and morpion[1][1] == 'O' and morpion[2][1] == 'O') or (morpion[0][2] == 'O' and morpion[1][2] == 'O' and morpion[2][2] == 'O'):
                    for i in range(len(morpion)):
                        print(f"{morpion[i]}")
                    print("Joueur 1 a gagné la partie")
                    remake = input("Voulez vous rejouer ? Oui : Press Q si Non : Press Enter ")
                    if remake != "Q":
                        return
                
                for i in range(len(morpion)):
                    print(f"{morpion[i]}")
            
            return print("Egalité bien jouer à vous")
        except:
            print("Une erreur est survenue lors de la partie appuyer sur 'Q' pour relancer")
            remake = input("Voulez vous rejouer ? Oui : Press Q si Non : Press Enter ")
morpion()