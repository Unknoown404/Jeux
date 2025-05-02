import time

def jeuDeLogique():
    mapOriginel = [
    ["█", "█", "█", "█", "█", "█", "█", "█"],
    ["█", " ", " ", " ", " ", " ", " ", "█"],
    ["█", " ","😊", " ", " ",'🎁', " ","█"],
    ["█", " ","🗄️", " ", " ", " ", " ","█"],
    ["█", " ","🗄️", " ", " ", " ", " ","█"],
    ["█", " ", " ", " ", " ",'🎁', " ","█"],
    ["█", " ", " ", " ", " ", " ", " ","█"],
    ["█", "█", "█", "█", "█", "█", "█","█"],
    ]
    
    mapSecondaire = [
    ["█", "█", "█", "█", "█", "█", "█", "█"],
    ["█", " ", " ", " ", " ", " ", " ", "█"],
    ["█", " ","😊", " ", " ",'🎁', " ","█"],
    ["█", " ","🗄️", " ", " ", " ", " ","█"],
    ["█", " ","🗄️", " ", " ", " ", " ","█"],
    ["█", " ", " ", " ", " ",'🎁', " ","█"],
    ["█", " ", " ", " ", " ", " ", " ","█"],
    ["█", "█", "█", "█", "█", "█", "█","█"],
    ]
    x = 2
    y = 2
    print("Les règles du jeu sont assez simple: vous devez déplacer les blocks à l'endroit où sont les cadeaux. ")
    print("Les touches pour se déplacer est au nombre de 4 : \n 'A' pour la gauche \n 'D' pour la droite \n 'S' pour le bas \n 'W' pour le haut" ) 
    time.sleep(10)
    for i in mapOriginel:
        print(i)
    
    liste =["😊", "🗄️", "🎁", "█", " "]
    total = 0
    for i in range(len(mapOriginel)):
        total += mapOriginel[i].count("🎁")
    
    while total !=0:
        total = 0
        
        #  POUR SE DEPLACER A DROITE
        deplacement = input()
        listeDeplacement = ["a", "d", "s", "w"]
        while deplacement not in listeDeplacement:
            deplacement = input()
        
        if "d" == deplacement and mapSecondaire[x][y+1] != liste[3]:
            if mapSecondaire[x][y+1] == liste[4]:
                y += 1
                mapSecondaire[x][y] = liste[0]
                mapSecondaire[x][y-1] = liste[4]
            elif mapSecondaire[x][y+1] == liste[1] :
                if mapSecondaire[x][y+2] == liste[3] or mapSecondaire[x][y+2] == liste[1]:
                    pass    
                else:    
                    y += 1
                    mapSecondaire[x][y] = liste[0]
                    mapSecondaire[x][y-1] = liste[4]
                    mapSecondaire[x][y+1] = liste[1]
                    
        #POUR SE DEPLACER A GAUCHE

        if "a" == deplacement and mapSecondaire[x][y-1] != liste[3]:
            if mapSecondaire[x][y-1] == liste[4]:
                y -= 1
                mapSecondaire[x][y] = liste[0]
                mapSecondaire[x][y+1] = liste[4]
            elif mapSecondaire[x][y-1] == liste[1]:
                if mapSecondaire[x][y-2] == liste[3] or mapSecondaire[x][y-2] == liste[1]:
                    pass
                else:
                    y -= 1
                    mapSecondaire[x][y] = liste[0]
                    mapSecondaire[x][y+1] = liste[4]
                    mapSecondaire[x][y-1] = liste[1]
                       
        # POUR SE DEPLACER EN HAUT
        
        if "w" == deplacement and mapSecondaire[x-1][y] != liste[3]:
            if mapSecondaire[x-1][y] == liste[4]:    
                x -= 1
                mapSecondaire[x][y] = liste[0]
                mapSecondaire[x+1][y] = liste[4]
            elif mapSecondaire[x-1][y] == liste[1]:
                if mapSecondaire[x-2][y] == liste[3] or mapSecondaire[x-2][y] == liste[1]:
                    pass
                else:
                    x -= 1
                    mapSecondaire[x][y] = liste[0]
                    mapSecondaire[x+1][y] = liste[4]
                    mapSecondaire[x-1][y] = liste[1]

        # POUR SE DEPLACER EN BAS
        
        if "s" == deplacement and mapSecondaire[x+1][y] != liste[3]:
            if mapSecondaire[x+1][y] == liste[4]:
                x += 1
                mapSecondaire[x][y] = liste[0]
                mapSecondaire[x-1][y] = liste[4]
            elif mapSecondaire[x+1][y] == liste[1] :
                if mapSecondaire[x+2][y] == liste[3] or mapSecondaire[x+2][y] == liste[1]:
                    pass    
                else:    
                    x += 1
                    mapSecondaire[x][y] = liste[0]
                    mapSecondaire[x-1][y] = liste[4]
                    mapSecondaire[x+1][y] = liste[1]

        for i in mapSecondaire:
            print(i) 

        for i in range(len(mapOriginel)):
            total += mapSecondaire[i].count("🎁")
    return print("Vous avez finis le jeu.")    
jeuDeLogique()