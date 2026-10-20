Geld = 1000
Inwoners = 10
tevredenheid = 75
maand = 1
huizen = 0

print("==============================")
print("          python city         ")
print("==============================")

print(f"Geld: €{Geld}")
print(f"Inwoners: {Inwoners}")
print(f"huizen: {huizen}")
print(f"Tevredenheid: {tevredenheid}%")
print(f"maand: {maand}")

print("------------------------------")

keuze = ""
while keuze != "5":
    print("wat wil je doen?")
    print("1. stad bekijken")
    print("2. stats bekijken")
    print("3. volgende maand")
    print("4. gebouw bouwen")
    print("5. stoppen")
    keuze = input("maak een keuze:")

    if keuze == "1":
        print("je hebt gekozen om je stad te bekijken.")
        
    elif keuze == "2":
        print("============ stats ===========")
        print(f"Geld: €{Geld}")
        print(f"inwoners: {Inwoners}")
        print(f"huizen: {huizen}")
        
    elif keuze == "3":
        print("------------------------------")
        print("er zijn 2 nieuwe inwoners komen wonen!")
        print("je hebt €100 belasting ontvangen!")
        print("")
        Geld = Geld + 100
        print(f"Geld: €{Geld}")
        Inwoners = Inwoners + 2
        print(f"Inwoners: {Inwoners}")
        print(f"huizen: {huizen}")
        print(f"Tevredenheid: {tevredenheid}%")
        maand = maand + 1
        print(f"Maand: {maand}")
        print("")

    elif keuze == "4":
        print("========== gebouwen ==========")
        print("1. huis     €500")
        print("2. winkel   €1000")
        print("3. park     €750")
        print("4. fabriek  €5000")
        print("------------------------------")
        gebouw_keuze = input("wat wil je bouwen?")
        if gebouw_keuze == "1":
            print("je bouwt een huis")
            print("er zijn 4 mensen in komen wonen!")
            Geld = Geld - 500
            huizen = huizen + 1
            Inwoners = Inwoners + 10
            
        elif gebouw_keuze == "2":
            print("je bouwt een winkel")
            Geld = Geld - 1000
            tevredenheid = tevredenheid + 2
            
        elif gebouw_keuze == "3":
            print("je bouwt een park")
            Geld = Geld - 750
            tevredenheid = tevredenheid + 5
            
            
        elif gebouw_keuze == "4":
            print("je bouwt een fabriek")
            Geld = Geld - 5000
            tevredenheid = tevredenheid - 10
    elif keuze == "5":
        print("je hebt gekozen om het spel te stoppen")

    else:
        print("dit is geen geldige invoer")
    