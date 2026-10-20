import time
import os
versie = "1.0"

GROEN = "\033[32m"
ROOD = "\033[31m"
ORANJE = "\033[38;2;255;165;0m"
BLAUW = "\033[34m"
PAARS = "\033[35m"
GEEL = "\033[33m"
WIT = "\033[37m"
ZWART = "\033[30m"
RESET = "\033[0m"

def kleur_print(tekst, kleur):
    print(kleur + tekst + RESET)

import colorsys

def regenboog(tekst, snelheid=0.04):
    hue = 0

    try:
        while True:
            uitvoer = ""

            for i, letter in enumerate(tekst):
                kleur_hue = (hue + i * 0.025) % 1.0
                r, g, b = colorsys.hsv_to_rgb(kleur_hue, 1, 1)

                R = int(r * 255)
                G = int(g * 255)
                B = int(b * 255)

                uitvoer += (
                    f"\033[38;2;{R};{G};{B}m{letter}"
                )

            print("\r" + uitvoer + "\033[0m", end="", flush=True)

            hue = (hue + 0.005) % 1.0
            time.sleep(snelheid)

    except KeyboardInterrupt:
        print("\033[0m")
        print()


Geld = 1000
Inwoners = 10
tevredenheid = 75
maand = 1
huizen = 3
schulden = 0
schuldbedrag = 0
inkomsten = 0
winkels = 0
fabrieken = 0
parken = 0
pretparken = 0

os.system("cls" if os.name == "nt" else "clear")
kleur_print("==============================", GROEN)
kleur_print("          python city", GROEN)
kleur_print(f"          Version {versie}", GEEL)
kleur_print("==============================", GROEN)

tekst = "loading Game"

for i in range(4):
    print("\r" + tekst + "." * i + "\033[0m", end="", flush=True)
    time.sleep(1)

print("\r\033[30m" + tekst + "." * 5 + "\033[0m")
#--------
kleur_print("========== gegevens ==========", PAARS)
print(f"Geld: €{Geld}")
print(f"Inwoners: {Inwoners}")
print(f"Tevredenheid: {tevredenheid}%")
print(f"Schulden: €{schulden}", ROOD)
print(f"maand: {maand}")
print(f"Inkomsten: €{inkomsten}", GROEN)
print(f"huizen: {huizen}")
print(f"winkels: {winkels}")
print(f"fabrieken: {fabrieken}")
print(f"parken: {parken}")
print(f"pretparken: {pretparken}")
kleur_print("------------------------------", BLAUW)
while maand <= 24:
    keuze = ""
    while keuze != "6":
            tekst = "loading"

            for i in range(4):
                print("\r" + tekst + "." * i + "\033[0m", end="", flush=True)
                time.sleep(1)

            print("\r\033[30m" + tekst + "." * 5 + "\033[0m")
             #--------
            print("wat wil je doen?")
            print("1. stad bekijken")
            print("2. gegevens bekijken")
            print("3. volgende maand")
            print("4. gebouw bouwen")
            print("5. geld lenen")
            print("6. stoppen")
            kleur_print("------------------------------", BLAUW)
            keuze = input("maak een keuze:")

            if keuze == "1":
                os.system("cls" if os.name == "nt" else "clear")
                kleur_print("============ stad ============", PAARS)
                print(f"huizen: {huizen}")
                print(f"winkels: {winkels}")
                print(f"fabrieken: {fabrieken}")
                print(f"parken: {parken}")
                print(f"pretparken: {pretparken}")
                kleur_print("------------------------------", BLAUW)
                
            elif keuze == "2":
                os.system("cls" if os.name == "nt" else "clear")
                kleur_print("========== gegevens ==========", PAARS)
                print(f"Geld: €{Geld}")
                print(f"inwoners: {Inwoners}")
                print(f"huizen: {huizen}")
                print(f"Schulden: €{schulden}", ROOD)
                print(f"Inkomsten: €{inkomsten}", GROEN)
                print(f"Tevredenheid: {tevredenheid}%")
                print(f"maand: {maand}")
                print(f"winkels: {winkels}")
                print(f"fabrieken: {fabrieken}")
                print(f"parken: {parken}")
                print(f"pretparken: {pretparken}")
                kleur_print("------------------------------", BLAUW)
                
            elif keuze == "3":
                os.system("cls" if os.name == "nt" else "clear")
                
                kleur_print("======= volgende maand =======", PAARS)
               
                if winkels > 0:
                    print(f"je hebt {winkels} winkels, je krijgt €{winkels * 100} belasting van de winkels!")
                    
                    if fabrieken > 0:
                        print(f"je hebt {fabrieken} fabrieken, je krijgt €{fabrieken * 500} belasting van de fabrieken!")
                
                if pretparken > 0:
                     print(f"je hebt {pretparken} pretparken, je krijgt €{pretparken * 1000} belasting van de pretparken!")
                
                Inkomsten = inkomsten + (winkels * 100) + (fabrieken * 500) + (pretparken * 1000) + (Inwoners * 10)
                Geld += Inkomsten
                
                if winkels == 0 and pretparken == 0 and fabrieken == 0:
                    print("je hebt geen gebouwen die inkomsten opleveren")
                
                kleur_print("------------------------------", BLAUW)
                print(f"Geld: €{Geld}")
                print(f"Inkomsten: €{inkomsten}", GROEN)
                print(f"Inwoners: {Inwoners}")
                print(f"huizen: {huizen}")
                print(f"fabrieken: {fabrieken}")
                print(f"parken: {parken}")
                print(f"pretparken: {pretparken}")
                print(f"Tevredenheid: {tevredenheid}%")
                maand = maand + 1
                if maand > 24:
                    kleur_print("------------------------------", BLAUW)
                    regenboog("je hebt 24 maanden gespeeld, het spel is afgelopen, bedankt voor het spelen!")
                    break
                
                print(f"Maand: {maand}")
                print("")
                if schulden > 0:
                    schuldbedrag = schulden / 10
                    print(f"je hebt schulden en je moet €{schuldbedrag} afbetalen")
                    schulden = schulden - schuldbedrag
                    print(f"schulden: €{schulden}")
                    Geld = Geld - schuldbedrag

            elif keuze == "4":
                os.system("cls" if os.name == "nt" else "clear")
                tekst = "loading menu"

                for i in range(4):
                    print("\r" + tekst + "." * i + "\033[0m", end="", flush=True)
                    time.sleep(1)

                print("\r\033[30m" + tekst + "." * 5 + "\033[0m")
                #--------
                kleur_print("========== gebouwen ==========", PAARS)
                print(" 1. huis     €500")
                print(" 2. winkel   €1000")
                print(" 3. park     €750")
                print(" 4. fabriek  €5000")
                print(" 5. pretpark: €10000")
                print(" 6. terug naar hoofdmenu")
                kleur_print("------------------------------", BLAUW)
                gebouw_keuze = input("wat wil je bouwen?")
                if gebouw_keuze == "1":
                    if Geld >= 500:
                        print("je bouwt een huis")
                        import random
                        inwoners_toevoegen = random.randint(1, 4)
                        print(f"je krijgt {inwoners_toevoegen} inwoners!")
                        print("")
                        Geld = Geld - 500
                        huizen = huizen + 1
                        Inwoners = Inwoners + inwoners_toevoegen
                    else:
                        print("je hebt niet genoeg geld om een huis te bouwen")
                    
                elif gebouw_keuze == "2":
                    if Geld >= 1000:
                        print("")
                        print("je bouwt een winkel")
                        print("je krijgt €100 belasting per maand van de winkel!")
                        Geld = Geld - 1000
                        winkels = winkels + 1
                        tevredenheid = tevredenheid + 2
                    else:
                        print("je hebt niet genoeg geld om een winkel te bouwen")
                elif gebouw_keuze == "3":
                    if Geld >= 750:
                        print("")
                        print("je bouwt een park")
                        Geld = Geld - 750
                        parken = parken + 1
                        tevredenheid = tevredenheid + 5
                    else:
                        print("je hebt niet genoeg geld om een park te bouwen")
                elif gebouw_keuze == "4":
                    if Geld >= 5000:
                        print("")
                        print("je bouwt een fabriek")
                        Geld = Geld - 5000
                        fabrieken = fabrieken + 1
                        tevredenheid = tevredenheid - 10
                    else:
                        print("je hebt niet genoeg geld om een fabriek te bouwen")
                elif gebouw_keuze == "5":
                    if Geld >= 10000:
                        print("")
                        print("je bouwt een pretpark")
                        Geld = Geld - 10000
                        pretparken = pretparken + 1
                        tevredenheid = tevredenheid + 20
                    else:
                        print("je hebt niet genoeg geld om een pretpark te bouwen")
                elif gebouw_keuze == "6":
                    print("je hebt gekozen om terug te gaan naar het hoofdmenu")
                    os.system("cls" if os.name == "nt" else "clear")

            elif keuze == "5":
                os.system("cls" if os.name == "nt" else "clear")
                kleur_print("========= geld lenen =========", PAARS)
                print("je hebt gekozen om geld te lenen")
                print("schulden worden afgeschreven aan het einde van de maand")
                print("")
                Geld = Geld + 1000
                print(f"Geld: €{Geld}")
                schulden = schulden + 1000
                print(f"Schulden: €{schulden}")
                
            elif keuze == "6":
                print("je hebt gekozen om het spel te stoppen")
                break
            
            elif keuze == "1983":
                maand += 25

            else:
                kleur_print("dit is geen geldige invoer", ROOD)
                kleur_print("probeer 1, 2, 3, 4, 5 of 6 in te voeren", ROOD)
                
            if Geld <= 0:
                kleur_print("------------------------------", BLAUW)
                kleur_print("je hebt geen geld meer, je kan niet verder spelen", ORANJE)
                kleur_print("leen geld van de bank om verder te spelen", ORANJE)
                kleur_print("of ga door naar de volgende maand om inkomsten te krijgen", ORANJE)
                print("")
                