from ttsdm_pkg.Utils.Scrython import get_card_by_name, get_card_by_id


class Card:
    tokens = []

    def __init__(self, name, image_sheet_manager, card_id=""):
        def get_oracle_text(card_data):
            try:
                return card_data.oracle_text()
            except KeyError:
                return ""

        def get_power(card_data):
            try:
                return card_data.power()
            except KeyError:
                return ""

        def get_toughness(card_data):
            try:
                return card_data.toughness()
            except KeyError:
                return ""

        data = None
        if card_id:
            data = get_card_by_id(card_id)
        else:
            data = get_card_by_name(name)
        self.scryFallId = data.id()
        self.name = data.name()
        self.type = data.type_line()
        self.text = get_oracle_text(data)
        self.power = get_power(data)
        self.toughness = get_toughness(data)
        self.cmc = data.cmc()
        self.imageUrl = data.image_uris(image_type="normal")
        self.imageSheetManager = image_sheet_manager
        self.ttsId, self.imageSheet = self.imageSheetManager.add_image(self.imageUrl)
        if "token" not in data.layout():
            try:
                for part in data.all_parts():
                    if "token" in part.get("component", ""):
                        Card.tokens.append(Card(part["name"], image_sheet_manager, part["id"]))
            except KeyError:
                pass

    def get_json_dict(self):
        return {"Name": "Card",
                "Nickname": self.build_card_description(),
                "Description": "",
                "Transform": {"posX": 0,
                              "posY": 0,
                              "posZ": 0,
                              "rotX": 0,
                              "rotY": 180,
                              "rotZ": 180,
                              "scaleX": 1,
                              "scaleY": 1,
                              "scaleZ": 1},
                "CardID": self.ttsId
                }

    def build_card_description(self):
        name = (self.name, '\n',
                "-----------\n",
                self.type, '\n',
                "-----------\n",
                self.text, '\n',
                "-----------\n",
                "cmc:" + str(self.cmc), " pwr:", str(self.power), " tgh:", str(self.toughness), '\n',
                "-----------\n",
                self.power, "/", self.toughness, '\n',
                "-----------\n"
                )
        return ''.join([x for x in name if x])
