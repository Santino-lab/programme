### eine liste ,mit allen möglichen farben gespeichert in einer variable ###

import random

farben = ["blau", "grün", "gelb", "rot", "lila" ]

##wir machen die kombination ###
kombination = []
farbe1 = random.choice (farben)
kombination.append(farbe1)
farben.remove (farbe1)
farbe2 = random.choice (farben)
kombination.append(farbe2)
farben.remove (farbe2)
farbe3 = random.choice (farben)
kombination.append(farbe3)
farben.remove (farbe3)
farbe4 = random.choice (farben)
kombination.append(farbe4)
farben.remove (farbe4)
farbe5 = random.choice (farben)
kombination.append(farbe5)
farben.remove (farbe5)


print (kombination) 