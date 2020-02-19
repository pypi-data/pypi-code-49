from scipy import stats
import numpy as np
import pandas as pd
import re

class PWR(object):
    def __init__(self, weight=1, regress_to=None, values=None):
        self.weight = weight
        self.regress_to = regress_to
        if values is None:
            self.values = None
        else:
            self.values = values.copy()
        
    def calculate(self, **kwargs):
        self.pwrcol = [x for x in list(self.values) if x not in ['Player']][0]
        return self
        
    def regress(self, df):
        self.values[self.pwrcol] = self.regress_to.regress(df, self.pwrcol)

class SRS(PWR):
    def __init__(self, weight=1, regress_to=None):
        PWR.__init__(self, weight, regress_to)
    
    def calculate(self, **kwargs):
        self.pwrcol = 'SRS'
        if kwargs['season'] == 1:
            df = kwargs['gamelog'].groupby('Player').agg({'Pts':'mean'})
            df = df.rename(columns={'Pts':'SRS'}).reset_index()
            self.values = df[['Player','SRS']]
        else:
            grouped = kwargs['gamelog'].groupby('Player').agg({'Difference':'sum','Opponent':lambda x: list(x)})
            grouped['Games Played'] = grouped['Opponent'].str.len()
            grouped['Margin'] = grouped['Difference'].values / grouped['Games Played'].values
            grouped['SRS'] = grouped['Margin']
            grouped['OldSRS'] = grouped['Margin']
            players = grouped.to_dict('index')
            for i in range(10000):
                delta = 0.0
                for name, player in players.items():
                    sos = 0.0
                    for opponent in player['Opponent']:
                        sos += players[opponent]['SRS']
                    players[name]['OldSRS'] = player['SRS']
                    players[name]['SRS'] = player['Margin'] + (sos / player['Games Played'])
                    delta = max(delta, abs(players[name]['SRS'] - players[name]['OldSRS']))
                if delta < 0.001:
                    break
            srs_sum = 0.0
            for name, player in players.items():
                srs_sum += players[name]['SRS']
            srs_avg = srs_sum / len(players)
            for name, player in players.items():
                players[name]['SRS'] = player['SRS'] - srs_avg
            df = pd.DataFrame.from_dict(players, orient='index').reset_index()
            self.values = df.rename({'index':'Player'}, axis=1)[['Player','SRS']]
        return self
        
class PWRsystems(object):
    def __init__(self, regress_to=None, srs=None, others=None, scale=None):
        self.regress_to = regress_to
        self.systems = []
        self.scale = None
        if isinstance(scale, dict):
            self.scale = scale
        elif scale:
            self.setDefaultScale()
        if (srs is None) and (others is None):
            self.systems.append(SRS())
        else:
            pairs = [(srs, SRS)]
            for system in [{'Arg':x,'Class':y} for x, y in pairs]:
                if type(system['Arg']) is bool:
                    if system['Arg']:
                        self.systems.append(system['Class']())
                elif system['Arg'] is not None:
                    self.systems.append(system['Arg'])
            if others is not None:
                if isinstance(others, PWR):
                    self.systems.append(others)
                else:
                    for system in others:
                        self.systems.append(system)
                        
    def setDefaultScale(self):
        self.scale = {'st_dev':1.05,'mean':0}
    
    def combine(self):
        if (len(self.systems) > 1) and (self.scale is None):
            self.setDefaultScale()
        self.combined = self.systems[0].values[['Player']]
        for system in self.systems:
            self.combined = pd.merge(self.combined, system.values, on='Player', suffixes=('','_'))
            new_z = stats.zscore(self.combined[system.pwrcol].values)
            new_weights = [system.weight] * self.combined.shape[0]
            if 'z_scores' not in self.combined:    
                self.combined['z_scores'] = [[x] for x in new_z]
                self.combined['weights'] = [[x] for x in new_weights]
            else:
                self.combined['z_scores'] = [x[0] + [x[1]] for x in list(zip(self.combined['z_scores'].values, new_z))]
                self.combined['weights'] = [x[0] + [x[1]] for x in list(zip(self.combined['weights'].values, new_weights))]
        zipped = zip(self.combined['z_scores'].values, self.combined['weights'].values)
        self.combined['Avg_z'] = [np.inner(x, y) / np.sum(y) for x, y in zipped]
        if self.scale is None:
            self.combined['PWR'] = self.combined[self.systems[0].pwrcol].values
        else:
            self.combined['PWR'] = self.combined['Avg_z'].values * self.scale['st_dev'] + self.scale['mean']
        return PWR(regress_to=self.regress_to, values=self.combined[['Player','PWR']]).calculate()