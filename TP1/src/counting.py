import sys
import time
import numpy as np
import platform

def countingSort(data_to_sort):
    max_value = max(data_to_sort)
    final_result = []
    result_table = np.zeros(max_value + 1, dtype='uint8')

    #change for while maybe

    for i in data_to_sort:
        result_table[i] += 1

    for i in range(0, len(result_table)):
        for j in range(0, result_table[i]):
            final_result.append(i)

    return final_result


def main():
    data = []

    ex_path = sys.argv[1]  # Path de l'exemplaire
    fread = open(ex_path, "r")

    with fread:
        for line in fread:
            data.append(int(line.strip()))

    # On commence a compter le temps uniquement pour le tri
    start_time = time.time()

    final_result = countingSort(data)

    execution_time = time.time() - start_time

    options = sys.argv[2:]
    if '-p' in options:  # On imprime les nombres triés
        for i in range(len(final_result)):
            if i != len(final_result) - 1:
                print(final_result[i], end=' ')
            else:
                print(final_result[i])
    if '-t' in options:  # On imprime le temps d'exécution
        print(execution_time)


if __name__ == '__main__':
    main()
