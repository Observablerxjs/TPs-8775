import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import sys

df = pd.read_csv('resultats.csv').groupby(['algo', 'serie', 'taille']).mean().reset_index()

A = [
    ['counting', lambda x, k: (x + k), '$n + k$'],
    ['quick', lambda x, k: x**2, '$n^2$'],
    ['quickSeuil', lambda x, k: x**2, '$n^2$'],
    ['quickRandomSeuil', lambda x, k: x*np.log(x), '$nlog(n)'],
]

plt.figure(figsize=(12, 4))

for pos, a in enumerate(A):

    ax = plt.subplot(2, 2, pos + 1)

    for serie in range(1, 4):

        algo, hyp_f, hyp_str = a
        data = df[(df.algo == algo) & (df.serie == 'testset'+str(serie))].copy()

        max = None
        if algo == 'counting':
            max = data.maxi

        data['rapport'] = data.temps / hyp_f(x=data.taille, k=max)

        ax.plot(data.taille, data.rapport, label='testset'+str(serie))
        ax.set_title('Test rapport ' + str(algo))
        ax.set_ylim(data.rapport.min()*0.9, data.rapport.max()*1.1)
        ax.set_ylabel('f(x) / ' + hyp_str)
        ax.set_xlabel('taille')

plt.tight_layout()
plt.legend(loc='best')
plt.show()
