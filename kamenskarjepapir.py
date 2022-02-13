import random

uporabnik_zmage = 0
racunalnik_zmage = 0
izenačeno = 0

izbira = ["kamen", "papir", "škarje"]

while True:
    vneseni_znaki = input("Vpiši Kamen/Škarje/Papir ali k, da končaš igro: ").lower()
    if vneseni_znaki == "k":
        print("Nasvidenje!")
        break

    if vneseni_znaki not in izbira:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, schare: 2
    izbira_racunalnika = izbira[random_number]
    print("Računalnik je izbral", izbira_racunalnika + ".")

    if vneseni_znaki == "kamen" and izbira_racunalnika == "škarje":

     print("Zmagal si")
     uporabnik_zmage += 1
     print("Zmagal si", uporabnik_zmage, "krat.")
     print("Računalnik je zmagal", racunalnik_zmage, "krat.")
     print("Izenačeno je bilo", izenačeno, "krat.")
     print("--------------------------------------------------------")


    elif vneseni_znaki == "papir" and izbira_racunalnika == "kamen":
     print("Zmagal si")
     uporabnik_zmage += 1
     print("Zmagal si", uporabnik_zmage, "krat.")
     print("Računalnik je zmagal", racunalnik_zmage, "krat.")
     print("Izenačeno je bilo", izenačeno, "krat.")
     print("--------------------------------------------------------")



    elif vneseni_znaki == "škarje" and izbira_racunalnika == "papir":
     print("Zmagal si")
     uporabnik_zmage += 1
     print("Zmagal si", uporabnik_zmage, "krat.")
     print("Računalnik je zmagal", racunalnik_zmage, "krat.")
     print("Izenačeno je bilo", izenačeno, "krat.")
     print("--------------------------------------------------------")

    elif vneseni_znaki == "škarje" and izbira_racunalnika == "škarje":
     print("IZENAČENO")
     izenačeno += 1
     print("Zmagal si", uporabnik_zmage, "krat.")
     print("Računalnik je zmagal", racunalnik_zmage, "krat.")
     print("Izenačeno je bilo", izenačeno, "krat.")
     print("--------------------------------------------------------")


    elif vneseni_znaki == "papir" and izbira_racunalnika == "papir":
     print("IZENAČENO")
     izenačeno += 1
     print("Zmagal si", uporabnik_zmage, "krat.")
     print("Računalnik je zmagal", racunalnik_zmage, "krat.")
     print("Izenačeno je bilo", izenačeno, "krat.")
     print("--------------------------------------------------------")


    elif vneseni_znaki == "kamen" and izbira_racunalnika == "kamen":
     print("IZENAČENO")
     izenačeno += 1
     print("Zmagal si", uporabnik_zmage, "krat.")
     print("Računalnik je zmagal", racunalnik_zmage, "krat.")
     print("Izenačeno je bilo", izenačeno, "krat.")
     print("--------------------------------------------------------")


    else:
        print("Zgubil si!")
        racunalnik_zmage += 1
        print("Zmagal si", uporabnik_zmage, "krat.")
        print("Računalnik je zmagal", racunalnik_zmage, "krat.")
        print("Izenačeno je bilo", izenačeno, "krat.")
        print("--------------------------------------------------------")



