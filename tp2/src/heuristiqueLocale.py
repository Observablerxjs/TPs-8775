import random
import time
import csv
import sys
import numpy as np
from glouton import glouton

def findBestNeighbor(neighbors):
    bestNeighbor = neighbors[0]
    for voisin in neighbors:
        if (voisin[1] > bestNeighbor[1]):   
            bestNeighbor = voisin
    return bestNeighbor


def heuristicLocale(emplacements, capacite):
    gloutonChoice = glouton(emplacements, capacite)
    neighbors = []
    while 1:
        del neighbors[:]
        i=0
        while i in range (len(gloutonChoice)):
            solution = gloutonChoice[i]
            neighbor = findNeighbor(np.array(emplacements), np.array(gloutonChoice), solution[0]-1, capacite)
            if len(neighbor) !=0 :
                bestNeighbor = findBestNeighbor(neighbor)
                gloutonChoice[i] = bestNeighbor
                neighbors.append(bestNeighbor)
            i+=1
        if neighbors == []:
            break
    return gloutonChoice

def findNeighbor(emplacement, solution, i, capacite):
    neighbor = []
    elementToDelete = emplacement[i]
    somme = solution[:,2].sum()
    lastNeighbor = np.setdiff1d(emplacement[:,0], solution[:,0])
    for neigh in lastNeighbor:
        elem = emplacement[neigh-1]
        qi = somme - elementToDelete[2] + elem[2]
        if (elem[1] > elementToDelete[1]) :
            if (qi <= capacite):
                neighbor.append(elem)
    return neighbor



ex_path = sys.argv[1] # Path de l'exemplaire
options = sys.argv[2:]

def startAlgo():
    file = open(ex_path, "r")
    data = file.read().splitlines()
    array = []
    for i in range(1, len(data) - 1):
        index, ri , qi = (int(s) for s in data[i].split())
        array.append((index, ri, qi))
    start_time = time.time()
    results = heuristicLocale(array, int(data[i + 1 ]))
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