import colored  
from colored import stylize
print (stylize ("Willkommen zu meinem Rechner", colored.fg( "royal_blue_1")))
erstezahl=input("Erste Rechenzahl: ")
ZweiteZahl=input("Zweite Rechenzahl: ")
Rechensymbol=input ("Was soll ich rechnen ")


if Rechensymbol== "*":
    print (int (erstezahl) * int(ZweiteZahl)) 
elif Rechensymbol== "-":
    print (int (erstezahl) - int(ZweiteZahl)) 
elif Rechensymbol == "/":
    print (int (erstezahl) / int(ZweiteZahl)) 
elif Rechensymbol == "+":
    print (int (erstezahl) + int(ZweiteZahl))  