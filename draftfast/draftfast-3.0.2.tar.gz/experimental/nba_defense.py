# Copy curl and take JSON from terminal
import crayons

# https://stats.nba.com/teams/defense/?sort=W&dir=-1
NBA_STATS = {"resource":"leaguedashteamstats","parameters":{"MeasureType":"Defense","PerMode":"PerGame","PlusMinus":"N","PaceAdjust":"N","Rank":"N","LeagueID":"00","Season":"2018-19","SeasonType":"Regular Season","PORound":0,"Outcome":None,"Location":None,"Month":0,"SeasonSegment":None,"DateFrom":None,"DateTo":None,"OpponentTeamID":0,"VsConference":None,"VsDivision":None,"TeamID":0,"Conference":None,"Division":None,"GameSegment":None,"Period":0,"ShotClockRange":None,"LastNGames":0,"GameScope":None,"PlayerExperience":None,"PlayerPosition":None,"StarterBench":None},"resultSets":[{"name":"LeagueDashTeamStats","headers":["TEAM_ID","TEAM_NAME","GP","W","L","W_PCT","MIN","DEF_RATING","DREB","DREB_PCT","STL","BLK","OPP_PTS_OFF_TOV","OPP_PTS_2ND_CHANCE","OPP_PTS_FB","OPP_PTS_PAINT","GP_RANK","W_RANK","L_RANK","W_PCT_RANK","MIN_RANK","DEF_RATING_RANK","DREB_RANK","DREB_PCT_RANK","STL_RANK","BLK_RANK","OPP_PTS_OFF_TOV_RANK","OPP_PTS_2ND_CHANCE_RANK","OPP_PTS_FB_RANK","OPP_PTS_PAINT_RANK","CFID","CFPARAMS"],"rowSet":[[1610612737,"Atlanta Hawks",14,3,11,0.214000,48.0,109.7,34.600000,0.705,8.400000,5.600000,24.1,17.0,16.5,45.1,9,28,26,28,20,22,14,25,11,13,30,28,28,7,10,"Atlanta Hawks"],[1610612738,"Boston Celtics",14,8,6,0.571000,48.4,101.0,36.500000,0.747,7.400000,5.200000,13.5,12.3,11.3,45.3,9,8,9,9,8,1,5,6,17,18,1,13,4,8,10,"Boston Celtics"],[1610612751,"Brooklyn Nets",15,6,9,0.400000,48.3,110.1,31.700000,0.686,7.100000,4.400000,18.7,15.7,11.5,46.4,2,20,23,23,18,23,27,28,20,25,22,27,6,10,10,"Brooklyn Nets"],[1610612766,"Charlotte Hornets",14,7,7,0.500000,48.4,107.9,34.300000,0.716,6.900000,6.400000,14.9,13.8,12.6,48.9,9,14,15,16,8,15,18,21,21,3,3,19,11,19,10,"Charlotte Hornets"],[1610612741,"Chicago Bulls",15,4,11,0.267000,49.0,110.3,34.600000,0.71,7.300000,5.200000,17.8,12.7,13.2,44.9,2,26,26,26,2,25,15,23,18,19,20,15,13,6,10,"Chicago Bulls"],[1610612739,"Cleveland Cavaliers",14,2,12,0.143000,48.0,112.8,32.300000,0.729,7.600000,2.600000,20.1,13.4,15.2,50.7,9,30,30,30,20,30,25,13,16,30,27,17,20,25,10,"Cleveland Cavaliers"],[1610612742,"Dallas Mavericks",14,6,8,0.429000,48.4,106.7,34.900000,0.76,7.200000,5.000000,17.7,11.6,14.6,43.3,9,20,20,21,8,9,13,4,19,21,19,7,17,3,10,"Dallas Mavericks"],[1610612743,"Denver Nuggets",14,9,5,0.643000,48.4,105.3,34.400000,0.765,8.600000,4.800000,16.6,11.7,12.1,47.9,9,5,5,5,8,5,16,1,8,23,12,9,9,14,10,"Denver Nuggets"],[1610612765,"Detroit Pistons",13,7,6,0.538000,49.2,106.1,35.500000,0.762,6.700000,4.000000,15.5,11.2,10.7,50.8,26,14,9,14,1,8,10,2,25,28,6,3,2,26,10,"Detroit Pistons"],[1610612744,"Golden State Warriors",15,12,3,0.800000,48.3,107.8,36.100000,0.732,7.700000,6.100000,17.1,12.3,13.3,48.9,2,1,1,1,18,14,7,11,14,6,17,12,14,20,10,"Golden State Warriors"],[1610612745,"Houston Rockets",13,6,7,0.462000,48.0,109.3,30.400000,0.717,8.400000,6.000000,16.7,11.2,11.2,49.4,26,20,15,20,20,21,29,19,10,7,13,4,3,21,10,"Houston Rockets"],[1610612754,"Indiana Pacers",14,8,6,0.571000,48.0,106.0,32.200000,0.721,8.700000,5.400000,15.3,10.9,13.4,39.4,9,8,9,9,20,7,26,16,5,17,5,2,15,1,10,"Indiana Pacers"],[1610612746,"LA Clippers",13,8,5,0.615000,48.8,106.7,37.700000,0.719,5.800000,6.000000,17.5,15.2,15.4,48.8,26,8,5,7,4,10,4,18,30,7,18,24,23,18,10,"LA Clippers"],[1610612747,"Los Angeles Lakers",14,8,6,0.571000,48.4,108.7,35.100000,0.708,9.200000,6.100000,18.9,13.7,16.2,53.7,9,8,9,9,8,20,12,24,4,5,23,18,26,29,10,"Los Angeles Lakers"],[1610612763,"Memphis Grizzlies",13,8,5,0.615000,48.4,104.8,30.300000,0.715,9.700000,4.300000,16.2,11.8,15.3,44.3,26,8,5,7,7,3,30,22,2,26,9,10,22,4,10,"Memphis Grizzlies"],[1610612748,"Miami Heat",14,6,8,0.429000,48.4,107.8,35.600000,0.717,6.600000,6.900000,20.4,17.2,11.6,45.3,9,20,20,21,8,13,9,20,26,1,28,29,7,8,10,"Miami Heat"],[1610612749,"Milwaukee Bucks",14,10,4,0.714000,48.4,104.8,40.900000,0.756,6.700000,6.500000,15.2,10.7,9.6,40.4,9,3,3,3,8,4,1,5,24,2,4,1,1,2,10,"Milwaukee Bucks"],[1610612750,"Minnesota Timberwolves",15,6,9,0.400000,48.0,112.7,32.300000,0.674,9.500000,5.900000,16.9,17.5,15.3,50.7,2,20,23,23,20,29,24,30,3,10,16,30,21,24,10,"Minnesota Timberwolves"],[1610612740,"New Orleans Pelicans",14,7,7,0.500000,48.0,110.2,36.200000,0.74,6.900000,5.800000,16.9,11.5,16.6,50.0,9,14,15,16,20,24,6,8,22,12,14,6,29,23,10,"New Orleans Pelicans"],[1610612752,"New York Knicks",15,4,11,0.267000,48.7,110.5,33.100000,0.731,7.700000,4.900000,19.1,14.3,11.4,51.2,2,26,26,26,6,26,21,12,14,22,25,22,5,27,10,"New York Knicks"],[1610612760,"Oklahoma City Thunder",14,9,5,0.643000,48.0,103.3,33.600000,0.72,11.400000,5.600000,15.6,11.9,14.0,49.6,9,5,5,5,20,2,19,17,1,13,7,11,16,22,10,"Oklahoma City Thunder"],[1610612753,"Orlando Magic",15,7,8,0.467000,48.0,108.3,33.300000,0.727,7.800000,6.000000,16.3,12.5,12.1,44.5,2,14,20,19,20,18,20,15,13,7,10,14,10,5,10,"Orlando Magic"],[1610612755,"Philadelphia 76ers",16,9,7,0.563000,48.9,107.1,38.700000,0.736,6.400000,5.900000,19.8,14.0,12.9,48.1,1,5,15,13,3,12,3,10,28,11,26,20,12,15,10,"Philadelphia 76ers"],[1610612756,"Phoenix Suns",14,3,11,0.214000,48.4,112.4,33.000000,0.728,6.900000,3.600000,22.6,14.1,19.9,54.3,9,28,26,28,8,28,22,14,22,29,29,21,30,30,10,"Phoenix Suns"],[1610612757,"Portland Trail Blazers",14,10,4,0.714000,48.4,105.6,39.900000,0.738,6.000000,5.100000,14.6,13.3,14.9,47.6,9,3,3,3,8,6,2,9,29,20,2,16,18,12,10,"Portland Trail Blazers"],[1610612758,"Sacramento Kings",14,8,6,0.571000,48.0,108.0,35.400000,0.703,8.500000,4.800000,16.9,15.7,16.3,52.3,9,8,9,9,20,17,11,26,9,23,15,26,27,28,10,"Sacramento Kings"],[1610612759,"San Antonio Spurs",13,7,6,0.538000,48.8,108.0,34.400000,0.746,6.500000,4.200000,15.8,11.7,16.2,48.6,26,14,9,14,4,16,17,7,27,27,8,8,25,17,10,"San Antonio Spurs"],[1610612761,"Toronto Raptors",15,12,3,0.800000,48.0,107.0,35.900000,0.697,8.700000,5.500000,16.5,14.5,15.1,48.3,2,1,1,1,20,11,8,27,7,15,11,23,19,16,10,"Toronto Raptors"],[1610612762,"Utah Jazz",14,7,7,0.500000,48.0,108.5,32.600000,0.761,8.200000,5.400000,18.5,11.3,12.0,47.7,9,14,15,16,20,19,23,3,12,16,21,5,8,13,10,"Utah Jazz"],[1610612764,"Washington Wizards",14,5,9,0.357000,48.4,112.3,31.400000,0.677,8.700000,6.300000,18.9,15.6,15.6,46.4,9,25,23,25,8,27,28,29,5,4,24,25,24,11,10,"Washington Wizards"]]}]}

rows = NBA_STATS['resultSets'][0]['rowSet']
print(rows)

MAPPING_DICT = {
    'Atlanta Hawks': 'ATL',
    'Boston Celtics': 'BOS',
    'Brooklyn Nets': 'BKN',
    'Charlotte Hornets': 'CHA',
    'Chicago Bulls': 'CHI',
    'Cleveland Cavaliers': 'CLE',
    'Dallas Mavericks': 'DAL',
    'Denver Nuggets': 'DEN',
    'Detroit Pistons': 'DET',
    'Golden State Warriors': 'GS',
    'Houston Rockets': 'HOU',
    'Indiana Pacers': 'IND',
    'LA Clippers': 'LAC',
    'Los Angeles Lakers': 'LAL',
    'Memphis Grizzlies': 'MEM',
    'Miami Heat': 'MIA',
    'Milwaukee Bucks': 'MIL',
    'Minnesota Timberwolves': 'MIN',
    'New Orleans Pelicans': 'NO',
    'New York Knicks': 'NY',
    'Oklahoma City Thunder': 'OKC',
    'Orlando Magic': 'ORL',
    'Philadelphia 76ers': 'PHI',
    'Phoenix Suns': 'PHO',
    'Portland Trail Blazers': 'POR',
    'Sacramento Kings': 'SAC',
    'San Antonio Spurs': 'SA',
    'Toronto Raptors': 'TOR',
    'Utah Jazz': 'UTA',
    'Washington Wizards': 'WAS',
}

DEFENSE_DICT = {}
for row in rows:
    team_name = row[1]
    def_rating = row[7]
    print(crayons.green(('Got {} at rating {}'.format(team_name, def_rating))))

    abbrev = MAPPING_DICT[team_name]
    DEFENSE_DICT[abbrev] = def_rating