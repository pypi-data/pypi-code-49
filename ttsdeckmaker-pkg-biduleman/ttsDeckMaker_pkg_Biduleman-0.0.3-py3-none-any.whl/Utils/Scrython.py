import scrython


def get_card_by_name(card_name):
    return scrython.cards.Named(fuzzy=card_name)


def get_card_by_id(card_id):
    return scrython.cards.Id(id=card_id)
