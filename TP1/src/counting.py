import sys
import numpy as np
import time

ex_path = sys.argv[1]  # Path de l'exemplaire

data = []

fread = open(ex_path, "r")

with fread:
    for line in fread:
        data.append(int(line.strip()))

# On commence a compter le temps uniquement pour le tri
start_time = time.time()

max_value = max(data)

final_result = []
result_table = np.zeros(max_value + 1).astype(int)

for i in data:
    result_table[i] += 1

for i in range(0, len(result_table)):
    for j in range(0, result_table[i]):
        final_result.append(i)

execution_time = time.time()-start_time

options = sys.argv[2:]
if '-p' in options:  # On imprime les nombres triés
    for i in range(len(final_result)):
        if i != len(final_result) - 1:
            print(final_result[i], end=' ')
        else:
            print(final_result[i])
if '-t' in options:  # On imprime le temps d'exécution
    print(execution_time)

