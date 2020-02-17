class Deck:
    deck_count = 0
    card_back_url = ""

    def __init__(self, name="", card_back_url=None):
        self.name = name
        self.cards = []
        Deck.card_back_url = card_back_url
        self.cardFrontUrl = []
        self.json = self.build_basic_deck(Deck.deck_count)
        Deck.deck_count += 1

    def __len__(self):
        return len(self.cards)

    def add_card(self, card):
        self.cards.append(card)
        self.json["DeckIDs"].append(card.ttsId)
        self.json["ContainedObjects"].append(card.get_json_dict())

    def get_json_dict(self):
        # for image_sheet in ImageSheetManager.imageSheets:
        #    self.json["CustomDeck"].update(image_sheet.get_json_dict())
        for card in self.cards:
            self.json["CustomDeck"].update(card.imageSheet.get_json_dict())
        for key in self.json["CustomDeck"]:
            self.json["CustomDeck"][key]["BackURL"] = self.card_back_url
        return self.json

    def build_basic_deck(self, index):
        return {
            "Transform": {
                "posX": 0 - (index * 4),
                "posY": 1,
                "posZ": 0,
                "rotX": 0,
                "rotY": 180,
                "rotZ": 180,
                "scaleX": 1,
                "scaleY": 1,
                "scaleZ": 1
            },
            "Name": "DeckCustom",
            "Nickname": self.name,
            "ContainedObjects": [],
            "DeckIDs": [],
            "CustomDeck": {}
        }
