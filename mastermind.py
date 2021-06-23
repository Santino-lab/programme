### eine liste ,mit allen möglichen farben gespeichert in einer variable ###

import random

farben = ["blau", "grün", "gelb", "rot", "lila" ]

##wir machen die kombination ###
kombination= []
kombination.append(random.choice(farben))
kombination.append(random.choice(farben))
kombination.append(random.choice(farben))

print (kombination)