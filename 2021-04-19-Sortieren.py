
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

print (gröstezahl)



liste = [3,4,4,5,7,3,3,3,3,3,4567,3,3,3,45677,3,2,7546456775764,24,325,46,5,7,6,3,876,6754,4,7,7,356536567,8,9,6,8]

def minimum (liste) :
    
    min = liste [0]
    
    for zahl in liste :                                                                                                                                                                                                                                                                       
        
        if zahl <  min :
            
            min = zahl 
    
    return min

#print (minimum (liste))


def sortieren (liste) :
    
    sortierte_liste = []
    
    länge = len (liste)
    
    for i in range (länge) :
    
        min = minimum (liste)
    
        sortierte_liste . append (min)
    
        liste . remove (min)
    
    return sortierte_liste 
    
print (sortieren (liste))"""
import random

for i in range (10000):
    liste.append (random)
    liste = random.randint (1,10000)
print (liste)







