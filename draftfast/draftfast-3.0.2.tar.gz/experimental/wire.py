import requests
import csv
from bs4 import BeautifulSoup


def scrape(game, projection_file):
    if game == 'fanduel':
        game = 'FanDuel'
    else:
        game = 'DraftKings'

    rotowire_url = 'https://www.rotowire.com/daily/wnba/optimizer.php?site={}'.format(
        game
    )

    s = requests.session()
    r = s.get(rotowire_url)

    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup)

    players = soup.find_all('td', {'class': 'rwo-name'})
    pts = soup.find_all('div', {'class': 'wa'})
    print(pts)

    # TODO - get way more here - there is a bunch offered
    # like salaries and O/Us
    assert len(pts) == len(players), 'Got {} projections and {} players'.format(len(pts), len(players))

    hold = []
    for idx in range(len(pts)):
        p = players[idx].text
        if p[-1] == '.':
            p = p[0:-1]
            print(p)
        hold.append({
            'playername': p.strip(),
            'points': float(pts[idx].get('value')),
        })

    print('Getting {} players from rotowire for {}'.format(len(pts), game))

    with open('wnba.csv', 'w+') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['playername', 'points'])
        writer.writeheader()
        writer.writerows(hold)

    return hold

scrape('fanduel', '')

