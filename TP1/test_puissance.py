import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sys
import numpy

df = pd.read_csv('resultats.csv').groupby(['algo','serie','taille']).mean().reset_index()

g = sns.FacetGrid(df, col='serie', hue='algo', size=4, aspect=1)
g = g.map(plt.plot, 'taille', 'temps')
g.set(xscale='log')
g.set(yscale='log')
g.add_legend()
plt.savefig('test_puissance')