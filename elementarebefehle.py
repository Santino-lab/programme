korrekteeingabe = False 

while korrekteeingabe== False:

    try:
        einwohnerbarcelona = int (input ("wie viele einwohner hat barcelona"))
        korrekteeingabe = True
    except:
        print ("BITTE GIB EINE ZAHL EIN !!!!")

korrekteeingabe = False

while korrekteeingabe == False:


    try:
        einwohnerParis = int(input ("wie viele einwohner hat Paris "))
        korrekteeingabe = True
    except:
        print ("BITTE GIB EINE ZAHL EIN !!!!!")
if einwohnerbarcelona < einwohnerParis:
    print ("paris hat mehr einwohner als barcelona!")
if  einwohnerbarcelona > einwohnerParis:
    print ("barcelona hat mehr einwohner als Paris")

korrekteeingabe = False

while korrekteeingabe == False:

    try:
        einwohnerlondon = int (input("wie viele einwohner hat london "))
        korrekteeingabe = True
    except: 
        print ("BITTE GIB EINE ZAHL EIN !!!!")




if einwohnerbarcelona > einwohnerParis and einwohnerlondon < einwohnerParis: 
    print ("paris hat mehr  einwohner als barcelona und london")
elif einwohnerbarcelona > einwohnerParis and einwohnerlondon > einwohnerlondon:
    print ("barcelona hat mehr einwohner als paris und london")

elif einwohnerlondon > einwohnerbarcelona and einwohnerlondon > einwohnerParis:

    print ("london hat mehr einwohner als paris und barcelona")
elif einwohnerlondon == einwohnerbarcelona and einwohnerlondon == einwohnerParis:
    print ("paris , barcelonaund london haben gleich viel einwohner")

