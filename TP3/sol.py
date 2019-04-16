import numpy as np
import sys
from random import randint
import operator
import copy


def run(data):

    best_cout = float("inf")
    best_sol = np.zeros(data['nbTypes'])

    while 1:
        modeles = copy.deepcopy(data['modeles'])
        np.random.shuffle(modeles)
        sol = np.zeros(data['nbModeles'], dtype=int)
        pieces_restantes = data['nbPieces']

        while sum([x for x in pieces_restantes if x > 0]) != 0:
            if all(x > 0 for x in pieces_restantes):
                rand_idx = randint(0, data['nbModeles'] - 1)
                modele_choisi = modeles[rand_idx]
            else:
                modele_choisi = find_best_model(data, pieces_restantes)
            pieces_restantes = list(map(operator.sub, pieces_restantes, modele_choisi))
            sol[data['modeles'].index(modele_choisi)] += 1

        cout = 0

        for idx, nombre_requis in enumerate(pieces_restantes):
            if nombre_requis < 0:
                cout += data['prixPieces'][idx]*abs(nombre_requis)

        if best_cout > cout:
            best_sol = sol
            best_cout = cout
            print('best_cout', best_cout)
            print(" ".join(map(str, best_sol)))


def find_best_model(data, piece_restantes):
    modele_choisi = []
    for modele in data['modeles']:
        good_model = True
        for idx, piece in enumerate(piece_restantes):
            if piece <= 0 and modele[idx] != 0:
                good_model = False
        if good_model:
            modele_choisi = modele
            break

    if not modele_choisi:
        modele_choisi = find_least_cost_model(data, piece_restantes)

    return modele_choisi


def find_least_cost_model(data, piece_restantes):

    cout = np.zeros(data['nbModeles'])
    max_value = piece_restantes.index(max(piece_restantes))
    valid_model = copy.deepcopy([x for x in data['modeles'] if x[max_value] != 0])

    for model in valid_model:

        temp = copy.deepcopy(piece_restantes)
        temp = list(map(operator.sub, temp, model))

        temp_cout = 0
        for idx, nombre_requis in enumerate(temp):
            if nombre_requis < 0:
                temp_cout += data['prixPieces'][idx] * abs(nombre_requis)

        cout[data['modeles'].index(model)] = temp_cout

    modele_choisi = data['modeles'][np.where(cout == min(cout[np.nonzero(cout)]))[0][0]]

    return modele_choisi


def main():

    data = {
        'nbTypes': 0,
        'nbPieces': [],
        'prixPieces': [],
        'nbModeles': 0,
        'modeles': []
    }

    ex_path = sys.argv[1]  # Path de l'exemplaire

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
