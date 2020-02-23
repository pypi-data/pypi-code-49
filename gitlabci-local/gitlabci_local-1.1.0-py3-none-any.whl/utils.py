#!/usr/bin/env python3

# Libraries
import regex

# Dictionnaries getter
def dictGet(data, path):

    # Variables
    queries = path.split('.')
    result = None

    # Iterate through queries
    for query in queries:

        # Parse query to key and index
        parse = regex.match(r'([^\[]*)(\[(\d)\])*', query)
        if parse.group(1) and parse.captures(3):
            key = parse.group(1)
            indexes = [int(value) for value in parse.captures(3)]
        else:
            key = query
            indexes = []

        # Extract key
        if key:
            if result:
                if isinstance(result, list):
                    result = [value.get(key, None) if value else None for value in result]
                else:
                    result = result.get(key, None)
            else:
                result = data.get(key, None)

        # Extract index
        for index in indexes:
            if result and result[index]:
                result = result[index]
            else:
                result = None

        # Empty node
        if not result:
            break

    # Result
    return result