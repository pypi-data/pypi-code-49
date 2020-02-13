#!/usr/bin/env python3
from getrails.duckduckgo.search import go_duck
from getrails.google.search import go_gle

def search (query):
    try:
        result = go_gle(query)
    except:
        result = go_duck(query)
    return result
