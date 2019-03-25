import sys
import time
import numpy as np


def glouton(data):

    solution = []
    emplacements_disp = data['emplacements']
    capacite = data['capacite']

    while capacite > 0:

        emplacements_disp = [x for x in emplacements_disp if x[2] <= capacite]

        if len(emplacements_disp) == 0:
            return solution

        rentabilite = np.zeros(len(emplacements_disp))
        for i in range(len(rentabilite)):
            rentabilite[i] = emplacements_disp[i][1] / emplacements_disp[i][2]
        rentabilite_sum = rentabilite.sum()
        probabilites = rentabilite / rentabilite_sum

        idx = np.random.choice(np.arange(0, len(emplacements_disp)), p=probabilites)

        capacite -= emplacements_disp[idx][2]
        solution.append(emplacements_disp[idx])
        emplacements_disp.remove(emplacements_disp[idx])

    return solution


def run(data):

    best_sol = []
    best_sum = 0

    for j in range(0, 10):

        sol = glouton(data)
        somme = sum([x[1] for x in sol])

        if best_sum < somme:
            best_sol = sol
            best_sum = somme

    return best_sol, best_sum


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

    solution, max_revenu = run(data)

    execution_time = time.time() - start_time

    if '-p' in options:  # On imprime la solution
        print('Solution avec revenu = ' + str(max_revenu))
        for idx, place in enumerate(solution):
            end = ','
            if idx == len(solution) - 1:
                end = '\n'
            print(place[0], end=end)
    if '-t' in options:  # On imprime le temps d'exécution
        print(execution_time)


if __name__ == '__main__':
    main()
