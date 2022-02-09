from random import randint
print("bonjour et bienvenue aux juste prix")

reponse = int(input("entré un prix : "))
prix = ""
while prix != reponse:
    prix = randint(1, 100)
    if prix == reponse:
        print("bravo bien joué")
    elif prix > reponse:
        print(f"plus grande que {reponse}")
        reponse = int(input("entré un prix : "))
    elif prix < reponse:
        print(f"plus petit que {reponse}")
        reponse = int(input("entré un prix : "))
