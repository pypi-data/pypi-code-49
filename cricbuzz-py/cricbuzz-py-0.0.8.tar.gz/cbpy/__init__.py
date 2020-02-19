name = "cricbuzz_py"
author = "Akshay T"
import requests
import json

id_list=list()
try:
	r=requests.get('https://www.cricbuzz.com/match-api/matches.json')
	r_text = r.text
except Exception as e:
	print("Connection_error")
	exit()

file = open('data.json',"w")
data = json.loads(r_text)
x=data['matches']

def fchdata():
	try:
		global r,r_text,file,data,x,id_list
		r=requests.get('https://www.cricbuzz.com/match-api/matches.json')
		r_text = r.text
		file = open('data.json',"w")
		data = json.loads(r_text)
		x=data['matches']
		id_list.clear()
		for key,value in x.items():
			id_list.append(key)
	except Exception as e:
		print("Connection error")
		exit()

def pmatchlist():
	fchdata()
	n = 0
	for match in id_list:
		t = str(match)
		mt = x[t]
		team1 = mt['team1']
		team1name = team1['name']
		team2 = mt['team2']
		team2name = team2['name']
		print('{} - {} vs {}'.format(n+1,team1name,team2name))
		n=n+1
	return 0;

def gmatchlist():
	fchdata()
	n = 0
	listmatch = list()
	for match in id_list:
		t = str(match)
		mt = x[t]
		team1 = mt['team1']
		team1name = team1['name']
		team2 = mt['team2']
		team2name = team2['name']
		elematch = team1name + " VS " +team2name
		listmatch.append(elematch)
		n=n+1
	return listmatch
		

def gteam1players(n):
	fchdata()
	plyrs = get_players(n)
	t1players = list()
	t1bench = list()
	if n > len(id_list):
		print( "Error : Invalid !")
		exit()
	n=n-1
	mt = x[str(id_list[n])]
	team1 = mt['team1']
	t1squad = team1['squad']
	t1squadbench = team1['squad_bench']
	for k,v in plyrs.items():
		if int(k) in t1squad:
			t1players.append(v)
		if int(k) in t1squadbench:
			t1bench.append(v)
	return t1players,t1bench


def gteam2players(n):
	fchdata()
	plyrs = get_players(n)
	t2players = list()
	t2bench = list()
	if n > len(id_list):
		print( "Error : Invalid !")
		exit()
	n=n-1
	mt = x[str(id_list[n])]
	team2 = mt['team2']
	t2squad = team2['squad']
	t2squadbench = team2['squad_bench']
	for k,v in plyrs.items():
		if int(k) in t2squad:
			t2players.append(v)
		if int(k) in t2squadbench:
			t2bench.append(v)
	return t2players,t2bench

def get_players(n):
	fchdata()
	teamp =dict()
	if n > len(id_list):
		print( "Error : Invalid !")
		exit()
	n = n - 1
	mch = x[str(id_list[n])]
	team1 = mch['team1']
	players = mch['players']
	for b in players:	
		teamp[str(b["id"])] = b["name"]
	return teamp

def plivescore(n):
	fchdata()
	teamp = get_players(n)
	
	teamd = dict()
	if n > len(id_list):
		print( "Error : Invalid !")
		exit()
	n = n - 1
	mch = x[str(id_list[n])]
	team1 = mch['team1']
	teamd[str(team1['id'])] = team1['name']
	team2 = mch['team2']
	teamd[str(team2['id'])] = team2['name']
	print("_________{} MATCH_________".format(mch['type']))
	if mch['status'] == "":
		msg = "Upcoming"
		print(msg)
	elif mch['state_title'] == 'Abandon':
		print("\n Status = {} ".format(mch['status']))
	else:
		scores = mch['score']
		batting = scores['batting']
		bowling = scores['bowling']
		batsman = scores['batsman']
		bowler = scores['bowler']
		innbat = batting['innings']
		innbow = bowling['innings']
		print("\n____________Batting____________")
		print('Current run rate = {}'.format(scores['crr']))
		for op in innbat:
			print("Innings = {} \nScore = {} \nWickets = {} \nOver = {}\n\n".format(op['id'],op['score'],op['wkts'],op['overs']))

		
		print('\nTeam = {} \nScore = {}'.format(teamd[str(batting['id'])],batting['score']))
		print("\n____________Bowling____________")
		for op in innbow:
			print("Innings = {} \nScore = {} \nWickets = {} \nOver = {}\n\n".format(op['id'],op['score'],op['wkts'],op['overs']))

		print('Team = {} \nScore = {}'.format(teamd[str(bowling['id'])],bowling['score']))
		print("\n____________Batsman____________")
		for bm in batsman:
			l=""
			if bm['strike'] == 1:
				l="*"
			print("Batsman = {} \nScore : {} ({})\n {}".format(teamp[str(bm['id'])],bm['r'],bm['b'],l))
			print("\n")
		print("\n____________Bowler____________")
		for bw in bowler:
			print("Bowler = {} \nStats : {} ({})\n Wickets = {}".format(teamp[str(bw['id'])],bw['r'],bw['o'],bw['w']))
			print("\n")
		print("\n Status = {} ".format(mch['status']))


def glivescore(n):
	fchdata()
	teamp = get_players(n)
	
	teamd = dict()
	if n > len(id_list):
		return ['invalid match number']
		exit()
	n = n - 1
	mch = x[str(id_list[n])]
	team1 = mch['team1']
	teamd[str(team1['id'])] = team1['name']
	team2 = mch['team2']
	teamd[str(team2['id'])] = team2['name']
	if mch['status'] == "":
		return ['Upcoming']
	elif mch['state_title'] == 'Abandon':
		return [match['Status']]
	else:
		scores = mch['score']
		batting = scores['batting']
		bowling = scores['bowling']
		batsman = scores['batsman']
		bowler = scores['bowler']
		innbat = batting['innings']
		innbow = bowling['innings']
		retlist = [mch['type'],batting,innbat,bowling,innbow,batsman,bowler,mch['status'],teamd]
		return retlist




