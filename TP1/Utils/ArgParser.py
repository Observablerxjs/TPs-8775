import argparse


class ArgParser:
    @staticmethod
    def parse():
        parser = argparse.ArgumentParser(description='Testing Algorithms')

        parser.add_argument('-a', help='Sorting mode', choices=['counting', 'quick', 'quickSeuil', 'quickRandomSeuil'], default='counting')
        parser.add_argument('-e', help='Image to process', default='./asl_alphabet_test/I_test.jpg')
        parser.add_argument('-p', help='Data set', default='./TrainingSet/')
        parser.add_argument('-t', help='Model path', default='./TrainedModel/model.txt')
        return parser.parse_args()