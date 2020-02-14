import numpy as np
import pandas as pd

def getPlayoffSeeding(gamelog):
    seeds = getSeeds(gamelog, [1,2,3,4,5,6,7,8], list(set(gamelog['Player'].values)))
    for i, seed in enumerate(seeds):
        seeds[i]['Seed'] = seed['Seed'] * 2 - (1 if seed['Division'] == 'B' else 0)
    return pd.DataFrame(seeds)

def getSeeds(gamelog, seeds, winners):
    wins = gamelog.groupby(['Player','Division'])['Wins'].sum()
    seeding = []
    for div, g in wins.groupby('Division'):
        filtered = g[[x in winners for x in g.index.get_level_values('Player').values]]
        w_rank = filtered.rank(method='min', ascending=False).values
        for s, seed in enumerate(seeds):
            iv = filtered[w_rank <= s + 1].index.values
            indices = [x for x in iv if x[0] not in [x['Player'] for x in seeding]]
            winner = breakTies(gamelog, [{'Player':t} for t, d in indices])
            seeding.append({'Division':div,'Player':winner,'Seed':seed})
    return seeding

def breakTies(gamelog, tiedplayers):
    if len(tiedplayers) == 1:
        return tiedplayers[0]['Player']
    remainder = [x['Player'] for x in tiedplayers]
    filtered = gamelog[gamelog['Player'].isin(remainder)]
    grouped = filtered.groupby(['Player'])['Pts'].sum().reset_index()
    remainder = grouped[(grouped['Pts'].values == grouped['Pts'].values.max())]['Player'].values
    if len(remainder) == 1:
        return remainder[0]
    elif len(remainder) == 2 and len(tiedplayers) != 2:
        return breakTies(gamelog, [x for x in tiedplayers if x['Player'] in remainder])
    filtered = gamelog[gamelog['Player'].isin(remainder) & gamelog['Opponent'].isin(remainder)]
    if not filtered.empty:
        grouped = filtered.groupby(['Player']).agg({'Pts':'sum'}).reset_index()
        remainder = grouped[(grouped['Pts'].values == grouped['Pts'].values.max())]['Player'].values
    if len(remainder) == 1:
        return remainder[0]
    elif len(remainder) == 2 and len(tiedplayers) != 2:
        return breakTies(gamelog, [x for x in tiedplayers if x['Player'] in remainder])
    return np.random.choice(remainder)