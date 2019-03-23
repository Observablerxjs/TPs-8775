import random
import time
import csv
import sys
import numpy as np
from glouton import glouton

def heuristic(array_emplacement, capacite):
    

ex_path = sys.argv[1] # Path de l'exemplaire
options = sys.argv[2:]

def startAlgo():
    file = open(ex_path, "r")
    new_array = file.read().splitlines()
    array = []
    for i in range(1, len(new_array) - 1):
        index, ri , qi = (int(s) for s in new_array[i].split())
        array.append((index, ri, qi))
    start_time = time.time()
    results = heuristic(array, int(new_array[i + 1 ]))
    execution_time  = time.time() - start_time
    return results, file, execution_time
results, file, execution_time = startAlgo()

if '-p' in options:
    for elem in results[:, 0]:
        print(int(elem))
    file.close()

if '-t' in options: # On imprime le temps d'exécution
    print(execution_time) 
file.close()