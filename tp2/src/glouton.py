import random
import time
import csv
import sys
import numpy as np

def glouton(emplacement, capacite):
    solution = []
    data = emplacement.copy()
    while capacite > 0:
        data = chooseEmplacement(data, capacite)
        if (len(data) <= 0):
            return np.array(solution)
        rentabilite = np.zeros(len(data))
        data_index = np.arange(0,len(data))
        for i in range (len(rentabilite)):
            rentabilite[i] = data[i][1] / data[i][2]
        rentabiliteSum = rentabilite.sum()
        probabilite = rentabilite / rentabiliteSum
        a = np.random.choice(a=data_index,p=probabilite)
        capacite -= data[a][2]
        solution.append(data[a])
        data.remove(data[a])
    return np.array(solution)

def chooseEmplacement(emplacement, capacite):
    result = []  
    for tempEmplacement in emplacement:
        if tempEmplacement[2] <= capacite:
            result.append(tempEmplacement)
    return result



def startAlgo():
    new_data = fread.read().splitlines()
    data = []
    for i in range(1, len(new_data) - 1):
        index, ri , qi = (int(s) for s in new_data[i].split())
        data.append((index, ri, qi))
    results = []
    bestChoice = []
    sommeMax = 0
    j=0
    while j in range (0, 10):
        start_time = time.time() 
        choice = glouton(data, int(new_data[i + 1 ]))
        execution_time = time.time() - start_time
        results.append(choice)
        somme = choice[:,1].sum()
        if sommeMax < somme:
            bestChoice = choice
            sommeMax = somme
        j+=1
    return bestChoice, execution_time

if __name__ == "__main__":
    ex_path = sys.argv[1] # Path de l'exemplaire
    options = sys.argv[2:]
    start_time =time.time()
    fread = open(ex_path, "r")
    solution,execution_time = startAlgo()
    if '-p' in options: # On imprime les nombres triés
        for elem in solution[:, 0]:
            print(int(elem))
        fread.close()
    if '-t' in options: # On imprime le temps d'exécution
        #start =time.time()
        fread.close()
        print(execution_time)
