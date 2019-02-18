import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('resultats.csv').groupby(['algo', 'serie', 'taille']).mean().reset_index()

A = [
    ['counting', lambda x, k: (x + k), '$n + k$'],
    ['quick', lambda x, k: x*np.log(x), '$nlog(n)'],
    ['quickSeuil', lambda x, k: x*np.log(x), '$nlog(n)$'],
    ['quickRandomSeuil', lambda x, k: x*np.log(x), '$nlog(n)$'],
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

        data['hyp'] = hyp_f(data.taille, max)
        fit = np.polyfit(data.hyp, data.temps, 1)
        fit_fn = np.poly1d(fit)

        ax.plot(data.hyp, fit_fn(data.hyp), label='testset'+str(serie))
        ax.set_title('Test des constantes ' + str(algo))
        ax.set_ylim(data.temps.min()*0.9, data.temps.max()*1.1)
        ax.set_xlim(0, data.hyp.max()*1.1)
        ax.set_ylabel('temps')
        ax.set_xlabel('f(x) / ' + hyp_str)

    
plt.tight_layout()
plt.legend(loc='best')
plt.show()
