liste = [1,2,3,9,10]                                                            
gesuchtezahl= ()
gesuchtezahl = int  (input ("Welche Zahl willst du suchen?"))
for i in (liste):
    if gesuchtezahl == i:
        print ("Diese Zahl ist in der Liste enthalten")
    if gesuchtezahl != i:
        print ("Diese Zahl ist nicht in der Liste enthalten")