### eine liste ,mit allen möglichen farben gespeichert in einer variable ###

import random

farben = ["blau", "grün", "gelb", "rot", "lila" ]

##wir machen die kombination ###
kombination = []
farbe1 = random.choice (farben)
kombination.append (farbe1)
farben.remove (farbe1)
farbe2 = random.choice (farben)
kombination.append (farbe2)
farben.remove (farbe2)
farbe3 = random.choice (farben)
kombination.append (farbe3)
farben.remove (farbe3)
"""farbe4 = random.choice (farben)
kombination.append (farbe4)
farben.remove (farbe4)
farbe5 = random.choice (farben)
kombination.append (farbe5) 
farben.remove (farbe5)"""

schwarz = -1
while schwarz <3:    



###wir fragen den spieler nach seiner wahl ###
    benutzerwahl = input ("welche kombination von farben willst du wählen ? ")
    benutzerwahl_liste = benutzerwahl.split()
    print (benutzerwahl_liste)                     

    #### was macht split ? sie trennen einen string und stecken ihn in eine liste ###



    schwarz = 0
    weiß = 0
    if kombination[0] == benutzerwahl_liste [0]:
        schwarz += 1
    if kombination[1] == benutzerwahl_liste [0]:
        weiß += 1
    if kombination[2] == benutzerwahl_liste [0]:
        schwarz += 1
    if kombination[0] == benutzerwahl_liste [1]:
        weiß += 1
    if kombination[1] == benutzerwahl_liste [1]:
        schwarz += 1
    if kombination[2] == benutzerwahl_liste [1]:
        weiß += 1
    if kombination[0] == benutzerwahl_liste [2]:
        weiß += 1
    if kombination[1] == benutzerwahl_liste [2]:
        weiß += 1
    if kombination[2] == benutzerwahl_liste [2]:
        schwarz += 1

    print ("schwarz:",schwarz)
    print ("weiß",weiß)
