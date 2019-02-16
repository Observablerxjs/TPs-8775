import sys
import random
import time

sys.setrecursionlimit(10**6)


def quickSortRandomSeuil(data_to_sort):
    if len(data_to_sort) < 4:
        return bubbleSort(data_to_sort)
    else:
        pivot_idx = random.randint(0, len(data_to_sort) - 1)
        pivot = data_to_sort[pivot_idx]
        leftside = []
        rightside = []

        j = pivot_idx - 1
        while j > 0:
            if data_to_sort[j] < pivot:
                leftside.append(data_to_sort[j])
            else:
                rightside.append(data_to_sort[j])
            j -= 1

        k = len(data_to_sort) - 1
        while k > pivot_idx + 1:
            if data_to_sort[k] < pivot:
                leftside.append(data_to_sort[k])
            else:
                rightside.append(data_to_sort[k])
            k -= 1

        # for i in data_to_sort[:pivot_idx]:
        #     if i < pivot:
        #         leftside.append(i)
        #     else:
        #         rightside.append(i)
        #
        # for i in data_to_sort[pivot_idx + 1:]:
        #     if i < pivot:
        #         leftside.append(i)
        #     else:
        #         rightside.append(i)

    return quickSortRandomSeuil(leftside) + [pivot] + quickSortRandomSeuil(rightside)


def bubbleSort(data_to_sort):
    for i in range(len(data_to_sort) - 1, 0, -1):
        for j in range(i):
            if data_to_sort[j+1] < data_to_sort[j]:
                temp = data_to_sort[j]
                data_to_sort[j] = data_to_sort[j+1]
                data_to_sort[j+1] = temp
    return data_to_sort


def main():
    data = []

    ex_path = sys.argv[1]  # Path de l'exemplaire
    fread = open(ex_path, "r")

    with fread:
        for line in fread:
            data.append(int(line.strip()))

    # On commence a compter le temps uniquement pour le tri
    start_time = time.time()

    final_result = quickSortRandomSeuil(data)

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
