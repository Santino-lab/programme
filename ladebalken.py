import time
import random 
from tqdm import tqdm
liste = []
for i in range (100):
    liste.append(0)
for i in tqdm(range(10000000),desc="lädt....."):
    
    Zufallszahl = (random.randint(0,99))
    liste [Zufallszahl] = liste [Zufallszahl]+1
print (liste)