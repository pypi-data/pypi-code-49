from dota import dota
from time import sleep
from tqdm import tqdm
dota_obj = dota("swifty")

#players = dota_obj.get_players()
#print(players)

'''start_val = 0
pbar = tqdm(total=len(players)-start_val)
for i in range(start_val,len(players)):
	if len(players[i]['team'])> 0:
		print(players[i]['team'])
		try:
			data = dota_obj.get_team_info(players[i]['team'],True)
		except Exception:	
			print("no page")
			pbar.update(1)	
			continue
		if len(data['results']) > 0:
			print("got results")
		else:
			print("no result")	
		sleep(15)
	pbar.update(1)	
pbar.close()'''

#print(dota_obj.get_player_info('Arteezy',True))	
#print(dota_obj.get_player_info('633',True))	


#print(dota_obj.get_team_info('Evil Geniuses',True))	
#print(dota_obj.get_team_info('Team Secret',True))


#print(dota_obj.get_transfers())	

#print(dota_obj.get_upcoming_and_ongoing_games())

#print(dota_obj.get_heros())

#print(dota_obj.get_items())

#print(dota_obj.get_patches())

print(dota_obj.get_tournaments())

#print(dota_obj.get_pro_circuit_details())