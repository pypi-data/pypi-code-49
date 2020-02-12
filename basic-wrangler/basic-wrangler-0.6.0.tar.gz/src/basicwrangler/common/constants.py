""" This module contains constants accessed by other modules. """

RE_QUOTES = r'(?=([^"]*"[^"]*")*[^"]*$)'  # this selects things NOT inside quotes
NO_TOKENIZER = [
    "generic",
    "freebasic",
    "qbasic",
    "gwbasic",
    "riscos",
    "amiga",
    "gsoft",
]
CBM_BASIC = ["pet", "vic20", "c64", "plus4", "c128"]
