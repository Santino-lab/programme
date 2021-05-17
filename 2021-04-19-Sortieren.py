### Aufgabe 1: Erstelle eine Liste mit beliebigen zehn verschiedenen Zahlen und speichere diese in einer Variable! ###^
"""liste = [1,2,3,4,5,6,7,8,9,10]
kleinstezahl=liste[0]
for zahl in liste :
    if zahl < kleinstezahl:
        kleinstezahl = zahl
print (kleinstezahl)


liste = [1,2,3,4,5,6,7,8,9,10]
gröstezahl=liste[0]
for zahl in liste :
    if zahl > gröstezahl:
        gröstezahl = zahl

print (gröstezahl)


liste = [10,2,3,4,5,6,7,8,9,1]
zweitgröstezahl=liste[9]
gröstezahl=liste[1]
for zahl in liste :
    if zahl > gröstezahl:
        zweitgröstezahl=gröstezahl
        gröstezahl = zahl
    if zahl > zweitgröstezahl:
        zweitgröstezahl = zahl
print (zweitgröstezahl)
print (gröstezahl)"""



liste = [3,4,4,5,7,8,9,6,8]
def minimum (liste) :
    min = liste [0]
    for zahl in liste :
        if zahl <  min :
            min = zahl 
    return min
print (minimum (liste)) 