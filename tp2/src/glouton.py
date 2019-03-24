import sys
import time
import numpy as np


def glouton(emplacement, capacite):

    solution = []
    disp_data = emplacement

    while capacite > 0:

        disp_data = [x for x in disp_data if x[2] <= capacite]

        if len(disp_data) == 0:
            return solution

        rentabilite = np.zeros(len(disp_data))
        data_index = np.arange(0, len(disp_data))

        for i in range(len(rentabilite)):
            rentabilite[i] = disp_data[i][1] / disp_data[i][2]

        rentabilite_sum = rentabilite.sum()
        probabilite = rentabilite / rentabilite_sum

        idx = np.random.choice(a=data_index, p=probabilite)

        capacite -= disp_data[idx][2]
        solution.append(disp_data[idx])
        disp_data.remove(disp_data[idx])

    return solution


def run(data):

    results = []
    best_sol = []
    best_sum = 0

    for j in range(0, 10):
        choice = glouton(data['emplacements'], data['capacite'])
        results.append(choice)

        somme = sum([x[1] for x in choice])
        if best_sum < somme:
            best_sol = choice
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
