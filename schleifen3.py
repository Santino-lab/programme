import tqdm
import time
import os 
import random 
import colored
from colored import stylize


zahl=0
while zahl < 255:
    zahl1 =0
    while zahl1<255: 
        zahl1=zahl1+1
        os.system("cls")
        print (stylize(" "*10, colored.fg (zahl1)+colored.bg(zahl1)))
        time.sleep (0.5)          