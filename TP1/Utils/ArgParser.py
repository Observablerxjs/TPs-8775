import argparse


class ArgParser:
    @staticmethod
    def parse():
        parser = argparse.ArgumentParser(description='Testing Algorithms')

        parser.add_argument('-a', help='Sorting mode', choices=['counting', 'quick', 'quickSeuil', 'quickRandomSeuil'], default='counting')
        parser.add_argument('-e', help='Path to used "exemplaire" ', default='./exemplaires/testset_1000_0.txt')
        parser.add_argument('-p', help='Affiche les nombres triés en ordre croissant sur une ligne, sans texte superflu')
        parser.add_argument('-t', help='Affiche le temps d’exécution en ms, sans unité ni texte superflu')
        return parser.parse_args()
