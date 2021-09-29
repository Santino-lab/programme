# spieler begrüßen

print ("Herrzlich willkommen zu tictactoe !")

#Spielfeld darstellen 

feld1 = "1"
feld2 = "2"
feld3 = "3"
feld4 = "4"
feld5 = "5"
feld6 = "6"
feld7 = "7"
feld8 = "8"
feld9 = "9"


zähler = 0
while zähler <= 5:
# Spiefeld ausgeben 

    reihe1 = feld1 + " | " + feld2 + " | " + feld3 

    reihe2 = feld4 + " | " + feld5 + " | " + feld6 

    reihe3 = feld7 + " | " + feld8 + " | " + feld9 

    trennreihe = "---------"

    print (reihe1)
    print (trennreihe)
    print (reihe2)
    print (trennreihe)
    print (reihe3)

    # spieler! nach seinem zug fragen 
    feld = input ("wohin möchtest du setzten ? ")


    if feld == "1" and feld1 == 1:
        feld1 = "x"
    if feld == "2" and feld2 == 2:
        feld2 = "x"
    if feld == "3" and feld3 == 3:
        feld3 = "x"
    if feld == "4" and feld4 == 4:
        feld4 = "x"
    if feld == "5" and feld5 == 5:
        feld5 = "x"
    if feld == "6" and feld6 == 6:
        feld6 = "x"
    if feld == "7" and feld7 == 7:
        feld7 = "x"
    if feld == "8" and feld8 == 8:
        feld8 = "x"
    if feld == "9" and feld9 == 9:
        feld9 = "x"
    # prüfen ob spieler 1 gewonnen hat 
    
    if (feld1 == "x" and feld2 == "x" and feld3 == "x") or (feld4 == "x" and feld5 == "x" and feld6 == "x") or (feld7 == "x " and feld8 == "x" and feld9 == "x") or (feld1 == "x" and feld4 == "x" and feld7 == "x")\
        or (feld2 == "x" and feld5 == "x" and feld8 == "x") or (feld3 == "x" and feld6 == "x" and feld9 == "x") or (feld1 == "x" and feld5 == "x" and feld9 == "x") or (feld3 == "x" and feld5 == "x" and feld7 == "x"):
            print ("glückwunsch spieler 1 du hast gewonnen")
            break
    # Spiefeld ausgeben 

    reihe1 = feld1 + " | " + feld2 + " | " + feld3 

    reihe2 = feld4 + " | " + feld5 + " | " + feld6 

    reihe3 = feld7 + " | " + feld8 + " | " + feld9 

    trennreihe = "---------"

    print (reihe1)
    print (trennreihe)
    print (reihe2)
    print (trennreihe)
    print (reihe3)


    # spieler2 nach seinem zug fragen 
    feld = input ("wohin möchtest du setzten ? ")


    if feld == "1" and feld1 == 1:
        feld1 = "o"
    if feld == "2" and feld2 == 2:
        feld2 = "o"
    if feld == "3" and feld3 == 3:
        feld3 = "o"
    if feld == "4" and feld4 == 4:
        feld4 = "o"
    if feld == "5" and feld5 == 5:
        feld5 = "o"
    if feld == "6" and feld6 == 6:
        feld6 = "o"
    if feld == "7" and feld7 == 7:
        feld7 = "o"
    if feld == "8" and feld8 == 8:
        feld8 = "o"
    if feld == "9" and feld9 == 9:
        feld9 = "o"

    zähler = zähler +1
#prüfen ob spieler 2 gewwonnen hat 

    if (feld1 == "o" and feld2 == "o" and feld3 == "o") or (feld4 == "o" and feld5 == "o" and feld6 == "o") or (feld7 == "o" and feld8 == "o" and feld9 == "o") or (feld1 == "o" and feld4 == "o" and feld7 == "o")\
        or (feld2 == "o" and feld5 == "o" and feld8 == "o") or (feld3 == "o" and feld6 == "o" and feld9 == "o") or (feld1 == "o" and feld5 == "o" and feld9 == "o") or (feld3 == "o" and feld5 == "o" and feld7 == "o"):
        print ("glückwunsch spieler 2 du hast gewonnen")
        break

















































































































































































