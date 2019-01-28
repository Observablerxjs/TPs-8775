from .Utils.ArgParser import ArgParser
from .Shared.Borg import Borg
from .Shared.Parameters import Parameters

from TP1.SortingAlgo.countingSort import coutingSort
from TP1.SortingAlgo.quickSort import quickSort


class Bootstrap(Borg):
    def __init__(self):
        args = ArgParser.parse()
        Parameters.set_parameters({
            'a': args.sortingMode,
            'e': args.input_exemplaire,
            'p': args.sortingDisplay,
            't': args.timingDisplay
        })

    def run(self):
        p = Parameters().get_parameters()

        algo = ''
        result = ''
        timing = ''

        if p['a'] == 'counting':
            algo = coutingSort()
        elif p['a'] == 'quick':
            algo = quickSort()

        [result, timing] = algo.run()

        if p['p']:
            print(result)

        if p['t']:
            print(timing)

        #
        # elif p['mode'] == 'classification':
        #
        # else:
