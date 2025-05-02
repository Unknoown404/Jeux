def jeuDuBatonnet():
    x = 21 
    liste = [1, 2, 3]
    while x!=1:
        j1 = int(input("Combien de baton veux tu retirer, joueur 1 : "))
        while j1 not in liste:
            j1 = int(input("Combien de baton veux tu retirer joueur 1 : "))
        x -= j1
        print(x)
        if x == 1:
            print("Joueur 2 a perdu gg")
            break 
        

        j2 = int(input("Combien de baton veux tu retirer joueur 2 : "))
        while j2 not in liste:
            j2 = int(input("Combien de baton veux tu retirer joueur 2 : "))
        x -= j2
        print(x)
        if x == 1:
            print("Joueur 1 a perdu gg")
            break        
jeuDuBatonnet()  
