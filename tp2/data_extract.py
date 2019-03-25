from src.glouton import run
from src.local import local_heuristic
from src.progdyn import dynamic_programming

import csv
import gc
import time

premiere_ligne = ["Taille", "Serie", "Glouton", "Revenue", "Prog_dynamic", "Revenue", "heuristic_local"
                            , "Revenue"]
with open('results.csv', 'a', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(premiere_ligne)

exemplaires_size = [10000]
exemplaire_serie = [10, 100, 1000]

for size in exemplaires_size:
    for serie in exemplaire_serie:

        exec_times = {'glouton': 0, 'dyn_prog': 0, 'heuristic_local': 0}
        best_sums = {'glouton': 0, 'dyn_prog': 0, 'heuristic_local': 0}

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

            print('environnement de test: Taille: ', size, ' serie: ', serie, ' exemplaire: ', i)

            # start_time = time.time()
            # best_G_sol, best_sum = run(data)
            # exec_time = time.time() - start_time
            # print("duration glouton : {}".format(exec_time))
            # exec_times['glouton'] += exec_time
            # best_sums['glouton'] += best_sum
            #
            # start_time = time.time()
            # best_LH_sol, best_sum = local_heuristic(data)
            # exec_time = time.time() - start_time
            # print("duration local_heuristic : {}".format(exec_time))
            # exec_times['heuristic_local'] += exec_time
            # best_sums['heuristic_local'] += best_sum

            start_time = time.time()
            try:
                best_DP_sol, best_sum = dynamic_programming(data)
                print('max_revenu', best_sum)
            except MemoryError as e:
                print('(PROG_DYN)_ERROR IN: ', size, ' serie: ', serie, ' exemplaire: ', i)
                best_sum = 0
                pass
            exec_time = time.time() - start_time
            print("duration dynamic_programming : {}".format(exec_time))
            exec_times['dyn_prog'] += exec_time
            best_sums['dyn_prog'] += best_sum

            print('************************************************************')

        new_line = [size, serie, exec_times['glouton']/10, best_sums['glouton']/10, exec_times['dyn_prog']/10,
                    best_sums['dyn_prog']/10, exec_times['heuristic_local']/10, best_sums['heuristic_local']/10]

        with open('results_prog_dyn.csv', 'a', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(new_line)

        gc.collect()
