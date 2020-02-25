import statsmodels.formula.api as smf
import pandas as pd
import numpy as np
import pymc3 as pm
from bambi import Model, Prior, Family
import matplotlib.pyplot as plt
from scipy.special import logit

df = pd.read_csv('paper_results/glmm_data.tsv', sep='\t')
df = df.loc[df['vecs'] != 'wiki+subs']
df['wiki'] = pd.get_dummies(df['vecs'])['wiki'] - .5
df['analogies'] = pd.get_dummies(df['kind'])['analogies'] - (1/3)
df['norms'] = pd.get_dummies(df['kind'])['norms'] - (1/3)
df['log10_wordcount'] = np.log10(df['wordcount'])
df['score'] = logit(df['score'])

print(df.head())


model = Model(df)
results = model.fit(
    'score ~ log10_wordcount + wiki * analogies + wiki * norms',
    random=['1|source', '1|lang'],
    samples=2000, n_init=1000, chains=2
)


'''
model = Model(df)
results = model.fit(
    'score ~ log10_wordcount + wiki',
    random=['1|kind'],
    samples=2000, n_init=2000, chains=2
)
'''


pm.traceplot(model.backend.trace)
plt.show()
print(results.summary())
