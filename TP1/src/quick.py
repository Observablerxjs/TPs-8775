import sys
import time

sys.setrecursionlimit(10**6)


def quickSort(data_to_sort):
    if not data_to_sort:
        return []
    else:
        pivot = data_to_sort[0]
        leftside = []
        rightside = []

        j = len(data_to_sort) - 1
        while j > 0:
            if data_to_sort[j] < pivot:
                leftside.append(data_to_sort[j])
            else:
                rightside.append(data_to_sort[j])
            j -= 1

        # boucle for ne fonctionne pas pour taille :100 000_(20+) et 500 000_(20+)
        # for i in data_to_sort[1:]:
        #     if i < pivot:
        #         leftside.append(i)
        #     else:
        #         rightside.append(i)
        return quickSort(leftside) + [pivot] + quickSort(rightside)


def main():
    # print(sys.getrecursionlimit())
    data = []

    ex_path = sys.argv[1]  # Path de l'exemplaire
    fread = open(ex_path, "r")

    with fread:
        for line in fread:
            data.append(int(line.strip()))

    # On commence a compter le temps uniquement pour le tri
    start_time = time.time()
    final_result = quickSort(data)

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

