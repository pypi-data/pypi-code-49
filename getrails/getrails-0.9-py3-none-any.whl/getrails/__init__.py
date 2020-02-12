#!/usr/bin/env python3
from duckduckgo import go_duck
from google import go_gle

def search (query):
    try:
        result = go_gle(query)
    except:
        result = go_duck(query)
    return result
