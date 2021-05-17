def meineerstefunktion():
    print ("die funktion funktioniert")

meineerstefunktion() 

def meinezweitefunktion(meinerstesargument):
    print(meinerstesargument)

meinezweitefunktion("diese funktion funktioniert auch")






def welchezahlistgrößer(zahl1,zahl2):
    if (zahl1) > (zahl2):
        print("zahl1 ist größer als zahl2")
    if (zahl1) < (zahl2):
        print ("zahl1 ist kleiner als zahl2")

welchezahlistgrößer(12,1)

def welchezahlistgrößer2(zahl1,zahl2,zahl3):
    if type(zahl1) != int:
        print ("die erste eingabe ist leider keine zahl")

    if type(zahl2) != int:
        print ("die zweite eingabe ist leider keine zahl")

    if type(zahl3) != int:
        print ("die dritte eingabe ist leider keine zahl")

    if zahl1 > zahl2 and zahl1 > zahl3: 
        print ("zahl1 ist die gröste zahl")
    if zahl2 > zahl1 and zahl2 > zahl3: 
        print ("zahl2 ist die gröste zahl")
    if zahl3 > zahl2 and zahl3 > zahl1: 
        print ("zahl3 ist die gröste zahl")

welchezahlistgrößer2(12,13,14)



def quadratzahlen (zahl):
    antwort = zahl * zahl
    return  antwort

quadratzahlen(20)
x=quadratzahlen(20
print(x)