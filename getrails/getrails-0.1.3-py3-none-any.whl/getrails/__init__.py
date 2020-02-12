#!/usr/bin/env python3
from sys import argv, exit
from duckduckgo.search import go_duck
from google.search import go_gle

def search (query):
    try:
        result = go_gle(query)
        result = go_duck(query)
    except:
        result = go_duck(query)
    return { "data": result, "length": len(result) }

