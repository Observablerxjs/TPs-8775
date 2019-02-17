import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sys
import numpy

df = pd.read_csv('resultats.csv').groupby(['algo', 'serie', 'taille']).mean().reset_index()
arr = numpy.array(df)

for line in arr:
    if line[0] == 'counting':
        line[3] /= line[2]
    elif line[0] == 'quick':
        line[3] /= line[2]
    elif line[0] == 'quickSeuil':
        line[3] /= line[2]
    else:
        line[3] /= line[2]
d = {'algo': arr[:, 0], 'serie': arr[:, 1], 'taille': arr[:, 2], 'temps': arr[:, 3]}
newDf = pd.DataFrame(data=d)


# g = sns.FacetGrid(newDf, col='serie', hue='algo', size=4, aspect=1)
# g = g.map(plt.plot, 'taille', 'temps')
# g.set(xscale='log')
# g.set(yscale='log')
# g.add_legend()
# plt.savefig('test_rapport')
