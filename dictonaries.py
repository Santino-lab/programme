import random 


print ("Willkommen beim präsenzunterricht")

zahl1=input ("gib mir eine erste zahl") 
zahl2=input ("gib mir eine zwiete zahl ")
zahl3 = random.randint (1,1600000)
if int (zahl1) > int (zahl2):
    print (zahl1+"ist größer als"+zahl1)

if int (zahl2) > int (zahl1) and int(zahl2) >zahl3 :
    print ("zahl1 ist die größte zahl")
