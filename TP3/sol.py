import numpy as np
import sys
from random import randint
import operator
import copy


def run(data):

    best_cout = float("inf")
    best_sol = np.zeros(data['nbTypes'])

    while 1:
        try:

            modeles = copy.deepcopy(data['modeles'])
            np.random.shuffle(modeles)
            sol = np.zeros(data['nbTypes'], dtype=int)
            pieces_restantes = data['nbPieces']

            while sum([x for x in pieces_restantes if x > 0]) != 0:
                rand_idx = randint(0, data['nbModeles']-1)
                modele_choisi = modeles[rand_idx]
                pieces_restantes = list(map(operator.sub, pieces_restantes, modele_choisi))
                sol[data['modeles'].index(modele_choisi)] += 1

            cout = 0

            for idx, nombre_requis in enumerate(pieces_restantes):
                if nombre_requis < 0:
                    cout += data['prixPieces'][idx]*abs(nombre_requis)

            if best_cout > cout:
                best_sol = sol
                best_cout = cout
                print(" ".join(map(str, best_sol)))
        # to remove
        except KeyboardInterrupt:
            break


def main():

    data = {
        'nbTypes': 0,
        'nbPieces': [],
        'prixPieces': [],
        'nbModeles': 0,
        'modeles': []
    }

    # ex_path = sys.argv[1]  # Path de l'exemplaire
    ex_path = './exemplaires/LEGO_50_50_1000'

    with open(ex_path, "r") as fp:
        for i, line in enumerate(fp):
            if i == 0:
                data['nbTypes'] = int(line.strip())
            elif i == 1:
                data['nbPieces'] = list(map(int, line.strip().split()))
            elif i == 2:
                data['prixPieces'] = list(map(int, line.strip().split()))
            elif i == 3:
                data['nbModeles'] = int(line.strip())
            elif i <= data['nbModeles'] + 3:
                data['modeles'].append(list(map(int, line.strip().split())))

    run(data)


if __name__ == '__main__':
    main()
