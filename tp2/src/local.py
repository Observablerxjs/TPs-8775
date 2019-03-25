import time
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.glouton import glouton


def local_heuristic(data):

    # first solution
    sol = glouton(data)
    capacite_max = data['capacite']
    optimum_local = False

    while not optimum_local:

        new_node = None

        for idx, removable in enumerate(sol):

            node_available = [x for x in data['emplacements'] if x not in sol]

            old_revenu = sum([x[1] for x in sol])

            while new_node is None and len(node_available) != 0:
                new_revenu = old_revenu - removable[1] + node_available[0][1]
                new_capacite = sum([x[2] for x in sol]) - removable[2] + node_available[0][2]
                if new_revenu > old_revenu and new_capacite <= capacite_max:
                    new_node = node_available[0]
                node_available.remove(node_available[0])

            if new_node is not None:
                sol[idx] = new_node
                new_node = None

        if new_node is None:
            optimum_local = True

    return sol, sum([x[1] for x in sol])


def main():

    data = {
        'nbEmplacements': 0,
        'emplacements': [],
        'capacite': 0
    }

    ex_path = sys.argv[1]  # Path de l'exemplaire
    options = sys.argv[2:]

    with open(ex_path, "r") as fp:
        for i, line in enumerate(fp):
            if i == 0:
                data['nbEmplacements'] = int(line.strip())
            elif i <= data['nbEmplacements']:
                data['emplacements'].append(tuple(map(int, line.strip().split())))
            else:
                data['capacite'] = int(line.strip())

    start_time = time.time()

    solution, best_sum = local_heuristic(data)

    execution_time = time.time() - start_time

    if '-p' in options:  # On imprime la solution
        # print('Solution avec revenu = ' + str(best_sum))
        for idx, place in enumerate(solution):
            end = ','
            if idx == len(solution) - 1:
                end = '\n'
            print(place[0], end=end)
    if '-t' in options:  # On imprime le temps d'exécution
        print(execution_time)


if __name__ == '__main__':
    main()
