from random import randint
print("bonjour et bienvenue au juste prix")
prix = randint(1, 100)
reponse = int(input("entrer un prix entre 1 et 100 : "))


while prix != reponse:

    if prix > reponse:
        print(f"plus grande que {reponse}")
        reponse = int(input("entrer un prix: "))
    else:
        print(f"plus petit que {reponse}")
        reponse = int(input("entrer un prix: "))
if prix == reponse:
    print("bravo bien joué")
