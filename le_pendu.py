def jeuDuPendu():    
    
    placement = 0
    print("Choisissez le mode de jeu. Avec vie: Press Q / Sans vie : Press M : ")
    mode = input()
    mot = str(input("Choisissez le mot que vous voulez faire deviner : "))
    motDeviner = []
    comparaison = []
    liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for i in range(len(mot)):
        comparaison.append(mot[i])
    
    for i in range(len(mot)):
        motDeviner.append('_')
    

    # MODE SANS VIE 
    while mode == "M":    
        while '_' in motDeviner:
            lettreChoisie = input("Choisissez une lettre pour le pendu : ")
            while lettreChoisie not in liste:
                print("Ce que vous avez saisis n'est pas une lettre minuscule, ou bien vous avez insérer plusieurs caractère ou autre...")
                lettreChoisie = input("Choisissez une lettre pour le pendu : ")
            if lettreChoisie in liste:
                liste.remove(lettreChoisie)
                for j in range(len(comparaison)):
                    if comparaison[j] == lettreChoisie:
                        motDeviner[j] = lettreChoisie
                    # motDeviner[comparaison.index(lettreChoisie)] = lettreChoisie
                    # comparaison[motDeviner.index(lettreChoisie)] = "."
                _somme = ""
                for i in motDeviner:
                    _somme = _somme + i    
                print(_somme)
        print("Mes félicitations, vous avez réussis")
        print("Choisissez le mode de jeu. Avec vie: Press Q / Sans vie : Press M : ")
        mode = input()
        break

    # MODE AVEC VIE 
    while mode == "Q":
        for loop in range(10):
            lettreChoisie = input("Choisissez une lettre pour le pendu : ")
            while lettreChoisie not in liste:
                print("Ce que vous avez saisis n'est pas une lettre minuscule, ou bien vous avez insérer plusieurs caractère ou autre...")
                lettreChoisie = input("Choisissez une lettre pour le pendu : ")
            if lettreChoisie in liste:
                liste.remove(lettreChoisie)
                for j in range(len(comparaison)):
                    if comparaison[j] == lettreChoisie:
                        motDeviner[j] = lettreChoisie
                    # motDeviner[comparaison.index(lettreChoisie)] = lettreChoisie
                    # comparaison[motDeviner.index(lettreChoisie)] = "."
                for i in motDeviner:
                    _somme = _somme + i    
                print(_somme)    

        if '_' in motDeviner : 
            print("Oh non, vous avez perdu !!")
            print("Voulez vous rejouer ?")
            mode = input("Avec vie: Press Q / Sans vie : Press M : ")
            break
        else:
            print("Mes félicitations, vous avez réussis")
            print("Choisissez le mode de jeu. Avec vie: Press Q / Sans vie : Press M : ")
            mode = input()
jeuDuPendu()