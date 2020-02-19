import requests
from ttsdm_pkg.Model.Deck import Deck
from ttsdm_pkg.Model.Card import Card
from ttsdm_pkg.Utils.ImageSheetManager import ImageSheetManager
from ttsdm_pkg.Utils.Url import get_download_url
from ttsdm_pkg.Utils.Cards import *
from ttsdm_pkg.Model.ObjectStates import ObjectStates

DEFAULT_CARD_BACK = "https://i.imgur.com/vasjHQ5.png"


def build_decks(deck_list_url, card_back=DEFAULT_CARD_BACK):
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

    Deck.deck_count = 0
    return tts_saved_data
