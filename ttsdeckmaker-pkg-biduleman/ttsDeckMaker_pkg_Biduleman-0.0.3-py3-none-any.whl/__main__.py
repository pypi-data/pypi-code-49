import json

import requests
from ttsdm_pkg.Model.Deck import Deck
from ttsdm_pkg.Model.Card import Card
from ttsdm_pkg.Utils.ImageSheetManager import ImageSheetManager
from ttsdm_pkg.Utils.Url import get_download_url
from ttsdm_pkg.Utils.Cards import *
from ttsdm_pkg.Model.ObjectStates import ObjectStates
import argparse

DEFAULT_CARD_BACK = "https://i.imgur.com/vasjHQ5.png"


def build_decks(deck_list_url, card_back):
    image_sheet_manager = ImageSheetManager()
    deck_list = requests.get(get_download_url(deck_list_url)).text.splitlines()
    decks = [Deck(name="Mainboard", card_back_url=card_back)]
    for line in deck_list:
        if line_is_card(line):
            card = Card(clean_card_name(line), image_sheet_manager)
            for i in range(get_card_count(line)):
                decks[-1].add_card(card)
        else:
            if "deckstats" in deck_list_url:
                if "sideboard" in line.lower():
                    decks.append(Deck(name="Sideboard"))
            if "tappedout" in deck_list_url:
                if "sideboard" in line.lower():
                    decks.append(Deck(name="Sideboard"))
            else:
                decks.append(Deck(card_back_url=card_back))
    if Card.tokens:
        decks.append(Deck(name="Tokens", card_back_url=card_back))
        for card in Card.tokens:
            decks[-1].add_card(card)

    tts_saved_data = ObjectStates()
    for deck in decks:
        tts_saved_data.add_object_state(deck.get_json_dict())

    return tts_saved_data


parser = argparse.ArgumentParser()

parser.add_argument('-d', '--deckUrl', help='Deck URL', type=str)
parser.add_argument('-b', '--backUrl', help='Custom Card Back URL', type=str, default=DEFAULT_CARD_BACK)
parser.add_argument('--dir', help='Saves a deck.json in this directory', type=str)
parser.add_argument('-f', '--filename', help='If a directory is specified the deck will use this filename', type=str,
                    default="deck.json")
args = parser.parse_args()

decks = build_decks(args.deckUrl, args.backUrl)

print(decks.get_json())
if args.dir:
    with open(args.dir + '\\' + args.filename, 'w') as fp:
        json.dump(decks.get_dict(), fp)
pass
