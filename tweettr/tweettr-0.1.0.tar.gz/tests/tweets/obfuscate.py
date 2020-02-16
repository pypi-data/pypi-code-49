"""obfuscate tweet data for tests"""
from datetime import datetime
import json
import time


tdict = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                      "WWWWWWWWWWWWWWWWWWWWWWWWWWwwwwwwwwwwwwwwwwwwwwwwwwww")


def obfuscate(data, key=None):
    if isinstance(data, list):
        out = []
        for item in data:
            out.append(obfuscate(item))
        return out
    elif isinstance(data, dict):
        out = {}
        for key, item in data.items():
            out[key] = obfuscate(item, key=key)
        return out
    else:
        if key == "created_at":
            x = datetime.utcnow().utctimetuple()
            x = time.strftime("%a %b %d %H:%M:%S %z %Y", x)
            return x
        elif key == "id":
            return 11223344556677889900
        elif key == "id_str":
            return '11223344556677889900'
        elif key == "screen_name":
            return "A" * len(data)
        elif isinstance(data, str):
            return data.translate(tdict)

        return data


if __name__ == '__main__':

    import pprint
    import sys

    if not len(sys.argv) == 3:
        print(__file__, 'infile', 'outfile')
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        data = json.load(f)

    new_data = obfuscate(data)

    pprint.pprint(new_data)

    with open(sys.argv[2], 'w') as f:
        json.dump(new_data, f, indent=2)
