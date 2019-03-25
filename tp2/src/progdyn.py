import time
import sys
import numpy as np


def dynamic_programming(data):

    D = np.zeros((data['nbEmplacements'], data['capacite'] + 1))
    nodes = data['emplacements']

    for i in range(1, D.shape[0]):
        for j in range(1, D.shape[1]):
            [idx, ri, qi] = nodes[i]
            if j - qi >= 0:
                D[i][j] = max(ri + D[i - 1][j - qi], D[i - 1][j])
            else:
                D[i][j] = D[i - 1][j]

    sol = get_solution(nodes, D)

    return sol, sum([x[1] for x in sol])


def get_solution(nodes, D):

    sol = []
    i = D.shape[0] - 1
    j = D.shape[1] - 1

    while D[i][j] != 0:
        node = nodes[i]
        if i == 0:
            sol.append(node)
            return sol
        [idx, ri, qi] = node
        if j - qi < 0:
            i -= 1
        else:
            if ri + D[i-1][j-qi] >= D[i-1][j]:
                sol.append(node)
                j -= qi
            i -= 1
    return sol


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

    solution, max_revenu = dynamic_programming(data)

    execution_time = time.time() - start_time

    if '-p' in options:  # On imprime la solution
        # print('Solution avec revenu = ' + str(max_revenu))
        for idx, place in enumerate(solution):
            end = ','
            if idx == len(solution) - 1:
                end = '\n'
            print(place[0], end=end)
    if '-t' in options:  # On imprime le temps d'exécution
        print(execution_time)


if __name__ == '__main__':
    main()
