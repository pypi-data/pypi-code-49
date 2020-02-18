import re


def line_is_card(card_line):
    return any(char.isdigit() for char in card_line)


def clean_card_name(card_line):
    card_name = re.sub(r"SB: ", "", card_line)
    card_name = re.sub(r"\[.*\]", "", card_name)
    card_name = ''.join([ii for ii in card_name if not ii.isdigit()]).strip()
    return card_name


def get_card_count(card_line):
    return int(re.search(r'\d+', card_line).group())
