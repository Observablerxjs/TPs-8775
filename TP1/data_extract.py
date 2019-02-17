from src.counting import countingSort
from src.quick import quickSort
from src.quickSeuil import quickSortSeuil
from src.quickRandomSeuil import quickSortRandomSeuil
import csv
import gc
import time

# premiere_ligne = ["Taille", "Exemplaire_ID", 'Maximum value', "Counting sort", "QuickSort",
#                   "QuickSort_Seuil_Exp", "QuickSort_Rand_Pivot-Seuil_Exp"]
# with open('results.csv', 'a', newline='') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(premiere_ligne)

exemplaires_size = [1000, 5000, 10000, 50000, 100000, 500000]

for size in exemplaires_size:
    for i in range(20, 30):
        path = "exemplaires/testset_" + str(size) + "_" + str(i) + ".txt"
        data = []
        fread = open(path, "r")

        with fread:
            for line in fread:
                data.append(int(line.strip()))

        new_line = [size, i, max(data)]

        print('environnement de test: Taille: ', size, ' exemplaire: ', i)

        start_time = time.time()
        countingSort(data)
        exec_time = time.time() - start_time
        print("duration countingSort : {}".format(exec_time))
        new_line.append(exec_time)

        start_time = time.time()
        # quickSort(data)
        exec_time = time.time() - start_time
        print("duration quickSort : {}".format(exec_time))
        new_line.append(exec_time)

        start_time = time.time()
        # quickSortSeuil(data)
        exec_time = time.time() - start_time
        print("duration quickSortSeuil : {}".format(exec_time))
        new_line.append(exec_time)

        Total_exec_time = 0
        # for _ in range(0, 10):
        #     start_time = time.time()
        #     quickSortRandomSeuil(data)
        #     Total_exec_time += time.time() - start_time
        mean_exec_time = Total_exec_time / 10
        print("duration quickSortRandomSeuil : {}".format(mean_exec_time))
        new_line.append(mean_exec_time)

        print('************************************************************')

        with open('results.csv', 'a', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(new_line)

        gc.collect()

