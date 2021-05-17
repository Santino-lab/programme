import random 
import colored
from colored import stylize
Optionen = ["Schere", "Stein", "Papier"]
Zettel = input  ("Wie viele Runden möchtest du spielen ?")
Spielerpunkte = 0
Computerpunkte = 0
for Runde in range (int( Zettel )):
    Computerwahl = random.choice(Optionen)
    Spielerwahl = input (stylize("Was willst du wählen:  Schere , Stein oder Papier ? ", colored.fg("purple_1b")))

    if Computerwahl == "Schere":
        if Spielerwahl == "Schere":
            print (stylize("Der Computer hat Schere gewählt. Unentschieden!",colored.fg("dark_orange_3b")))
            
            
        if Spielerwahl == "Stein":
            print (stylize("Der Computer hat Schere gewählt. Gewonnen!",colored.fg("chartreuse_2a")))
            Spielerpunkte = Spielerpunkte+1
            
        if Spielerwahl == "Papier":
            print (stylize("Der Computer hat Schere gewählt. Verloren!",colored.fg("red_3a")))
            
            Computerpunkte = Computerpunkte+1

    if Computerwahl == "Stein":
        if Spielerwahl == "Stein":
            print (stylize("Der Computer hat Stein gewählt. Unentschieden!",colored.fg("dark_orange_3b")))
        
            
        if Spielerwahl == "Papier":
            print (stylize("Der Computer hat Stein gewählt. Gewonnen!",colored.fg("chartreuse_2a")))
            Spielerpunkte = Spielerpunkte+1
        
        if Spielerwahl == "Schere":
            print (stylize("Der Computer hat Stein gewählt. Verloren!",colored.fg("red_3a")))
            
            Computerpunkte = Computerpunkte+1

    if Computerwahl == "Papier":
        if Spielerwahl == "Papier":
            print (stylize("Der Computer hat Papier gewählt. Unentschieden!",colored.fg("dark_orange_3b")))
    
            
        if Spielerwahl == "Schere":
            print (stylize("Der Computer hat Papier gewählt. Gewwonnen!",colored.fg("chartreuse_2a")))
            Spielerpunkte = Spielerpunkte+1
            
        if Spielerwahl == "Stein":
            print (stylize("Der Computer hat Papier gewählt. Verloren!",colored.fg("red_3a")))
            
            Computerpunkte = Computerpunkte+1
if Spielerpunkte == Computerpunkte:
    print ("Unentschieden")
if Spielerpunkte >  Computerpunkte:
    print ("Gewonnen")
if Spielerpunkte < Computerpunkte:
    print ("Verloren")