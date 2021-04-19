import random 
import colored
from colored import stylize
Optionen = ["ja", "nein","jain"]
Computerwahl = random.choice (Optionen)  
print (stylize (Computerwahl,colored.fg("chartreuse_2a")))
