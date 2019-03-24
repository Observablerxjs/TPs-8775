from src.glouton import run
# from src.heuristiqueLocale import heuristicLocale


import csv
import gc
import time

premiere_ligne = ["Taille", "Serie", "Exemplaire_ID", "Glouton", "Prog_dynamic","heuristic_local"]
with open('results.csv', 'a', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(premiere_ligne)

exemplaires_size = [100, 1000, 10000]
exemplaire_serie = [10, 100, 1000]

for size in exemplaires_size:
    for serie in exemplaire_serie:
        for i in range(1, 11):
            path = "exemplaires/WC-" + str(size) + "-" + str(serie) + "-" + str(i).zfill(2) + '.txt'

            print('path', path)

            data = {
                'nbEmplacements': 0,
                'emplacements': [],
                'capacite': 0
            }

            with open(path, "r") as fp:
                for j, line in enumerate(fp):
                    if j == 0:
                        data['nbEmplacements'] = int(line.strip())
                    elif j <= data['nbEmplacements']:
                        data['emplacements'].append(tuple(map(int, line.strip().split())))
                    else:
                        data['capacite'] = int(line.strip())

            new_line = [size, serie, i]

            print('environnement de test: Taille: ', size, ' serie: ', serie, ' exemplaire: ', i)

            start_time = time.time()
            run(data)
            exec_time = time.time() - start_time
            print("duration glouton : {}".format(exec_time))
            new_line.append(exec_time)

            # start_time = time.time()
            # # quickSort(data)
            # exec_time = time.time() - start_time
            # print("duration quickSort : {}".format(exec_time))
            new_line.append(0)
            #
            # start_time = time.time()
            # # quickSortSeuil(data)
            # exec_time = time.time() - start_time
            # print("duration quickSortSeuil : {}".format(exec_time))
            new_line.append(0)

            print('************************************************************')

            with open('results.csv', 'a', newline='') as myfile:
                wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
                wr.writerow(new_line)

            gc.collect()

