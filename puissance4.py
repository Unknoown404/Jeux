def puissance4():
    liste = [
        [ " ", " ", " ", " ", " ", " ", " "],
        [ " ", " ", " ", " ", " ", " ", " "],
        [ " ", " ", " ", " ", " ", " ", " "],
        [ " ", " ", " ", " ", " ", " ", " "],
        [ " ", " ", " ", " ", " ", " ", " "],
        [ " ", " ", " ", " ", " ", " ", " "]
    ]
    coordonnée = [1, 2, 3, 4, 5, 6, 7, 8]
    i = 1
    count = 0
    for j in range(len(liste)):
        print(f"{liste[j]}")
    
    for loop in range(21):

        # JOUEUER NUMERO 1 :
        
        colonne = int(input("colonne : "))
        while colonne not in coordonnée:
            colonne = int(input("colonne : "))
        i = 1
        if liste[len(liste)-i][colonne-1] == " ":
            liste[len(liste)-i][colonne-1] = "X"
        else : 
            while liste[len(liste)-i][colonne-1] != " ":
                i +=1
            liste[len(liste)-i][colonne-1] = "X"
        
        for j in range(len(liste)):
            print(f"{liste[j]}")

        for k in range(len(liste)):
            for g in range( len(liste) + 1 ):
                if liste[k][g] != "X":
                    pass
                else:
                    count = 0
                    repaire = 1
                    for loop in range(3):
                        if liste[k - repaire][g] == "X":
                            count += 1
                            repaire += 1
                        if count == 3:
                            return print("Mes félicitations vous avez gagné")
                    for loop in range(3):
                        if liste[k ][g - repaire] == "X":
                            count += 1
                            repaire += 1
                        if count == 3:
                            return print("Mes félicitations vous avez gagné")
                    for loop in range(3):
                        if liste[k - repaire][g - repaire] == "X":
                            count += 1
                            repaire += 1
                        if count == 3:
                            return print("Mes félicitations vous avez gagné")    

        # JOUEUR NUMERO 2:
        colonne = int(input("colonne : "))
        while colonne not in coordonnée:
            colonne = int(input("colonne : "))
        i = 1
        if liste[len(liste)-i][colonne-1] == " ":
            liste[len(liste)-i][colonne-1] = "O"
        else : 
            while liste[len(liste)-i][colonne-1] != " ":
                i +=1
            liste[len(liste)-i][colonne-1] = "O"  

        for j in range(len(liste)):
            print(f"{liste[j]}")

        # VERIFICATION DE L'ETAT DE LA PARTIE

        for k in range(len(liste)):
            for g in range( len(liste) + 1 ):
                if liste[k][g] != "O":
                    pass
                else:
                    count = 0
                    repaire = 1
                    for loop in range(3):
                        if liste[k - repaire][g] == "O":
                            count += 1
                            repaire += 1
                        if count == 3:
                            return print("Mes félicitations vous avez gagné")
                    for loop in range(3):
                        if liste[k][g - repaire] == "O":
                            count += 1
                            repaire += 1
                        if count == 3:
                            return print("Mes félicitations vous avez gagné")
                    for loop in range(3):
                        if liste[k - repaire][g - repaire] == "O":
                            count += 1
                            repaire += 1
                        if count == 3:
                            return print("Mes félicitations vous avez gagné")
puissance4()