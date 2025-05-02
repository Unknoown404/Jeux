import random

def jeuDeDée():
    liste = []
    for loop in range(3):    
        x = random.randint(1, 6)
        liste.append(x)
    while 6 in liste:
        liste.remove(6)
        x = random.randint(1, 6)
        liste.append(x)
    if 4 in liste and 2 in liste and 1 in liste:
        return print(f"Vous avez gagné : {liste}")
    print(f"Vous avez perdu : {liste}")
jeuDeDée()
