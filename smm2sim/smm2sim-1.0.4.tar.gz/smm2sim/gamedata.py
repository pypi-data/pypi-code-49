from requests import get
from io import StringIO
import numpy as np
import pandas as pd

def getPlayers(season=None):
    df = pd.read_csv(StringIO(get('https://pastebin.com/raw/WEf5d2fm').text))
    if season is None:
        season = df['Season'].max()
    return df[df['Season'] == season][['Player','Division']]

def getMatches(season=None):
    games = pd.read_csv(StringIO(get('https://pastebin.com/raw/eTmbZM46').text))
    if season is None:
        season = games['Season'].max()
    games = games[games['Season'] == season]
    games_grouped = games.groupby(['MatchID','Division','Week','Match'])
    lm = lambda x:max(set(list(x)), key=list(x).count)
    matches = pd.merge(games_grouped.agg({'Winner':lm,'Loser':lm}), 
                       games_grouped.agg(lambda x: tuple(x)), 
                       left_index=True, right_index=True, suffixes=('','_list')).reset_index()
    #calculate penalties for mid-match forfeits
    lm = lambda x:sum(np.where(np.repeat(x[0], len(x[1])) == np.array(x[1]), np.isnan(x[2]), 0))
    w_pts = 4 if season == 1 else 3
    w_penalty = [lm(x) * 2 for x in matches[['Loser','Winner_list','L Clears']].values]
    l_penalty = [(lm(x) in [1, 2]) * 2 for x in matches[['Loser','Loser_list','L Clears']].values]
    no_penalty = [sum(np.where(np.isnan(x), 1, 0)) == 3 for x in matches['W Clears'].values]
    #calculate match point totals
    is_sweep = [~np.isin(x[0], x[1]) for x in matches[['Loser','Winner_list']].values]
    matches['W Pts'] = np.where(is_sweep, w_pts, w_pts - 1) - np.where(no_penalty, 0, w_penalty)
    matches['L Pts'] = np.where(is_sweep, 0, 1) - np.where(no_penalty, 0, l_penalty)
    repl_df = pd.read_csv(StringIO(get('https://pastebin.com/raw/0kyaPRqX').text))
    replacements = repl_df.to_dict('records')
    for repl in replacements:
        matches['Winner'] = matches['Winner'].str.replace(repl['Old'], repl['New'])
        matches['Loser'] = matches['Loser'].str.replace(repl['Old'], repl['New'])
    return matches[['Winner','Loser','W Pts','L Pts']]
    
def getPointLog(season=None):
    games = pd.read_csv(StringIO(get('https://pastebin.com/raw/eTmbZM46').text))
    if season is None:
        season = games['Season'].max()
    games = games[games['Season'] == season]
    if season == 1:
        points = pd.DataFrame(games[['Winner','Loser','W Clears','W GmOv','W TB']].values.tolist() +
                              games[['Loser','Winner','L Clears','L GmOv','L TB']].values.tolist(), 
                              columns= ['Player','Opponent','Clears','GmOv','TB'])
        points = points[~np.isnan(points['Clears'])]
        points['Pts'] = points['Clears'] - points['GmOv']
        return points
    else:
        points = pd.DataFrame(games[['Winner','Loser','W Clears','W TB','L Clears','L TB']].values.tolist() +
                              games[['Loser','Winner','L Clears','L TB','W Clears','W TB']].values.tolist(), 
                              columns= ['Player','Opponent','Clears','TB','OppClears','OppTB'])
        league_avg = points['Clears'].mean()
        clears = points.copy()
        clears['Opponent'] = 'League'
        clears['OppClears'] = league_avg
        clears['OppTB'] = 0
        clears_dup = pd.DataFrame(clears[['Player','Opponent','Clears','TB','OppClears','OppTB']].values.tolist() +
                                  clears[['Opponent','Player','OppClears','OppTB','Clears','TB']].values.tolist(), 
                                  columns= ['Player','Opponent','Clears','TB','OppClears','OppTB'])
        full_df = pd.concat([points, clears_dup])
        full_df = full_df[~np.isnan(full_df['Clears'])]
        full_df = full_df[~np.isnan(full_df['OppClears'])]
        full_df['Difference'] = full_df['Clears'] - full_df['OppClears']
        return full_df

def getUnplayed(season=None):
    df = pd.read_csv(StringIO(get('https://pastebin.com/raw/rmb6A8uW').text))
    if season is None:
        season = df['Season'].max()
    return df[df['Season'] == season][['Home','Away']]