import sys, os, shutil, json
import urllib.request, traceback
from io import BytesIO
from zipfile import ZipFile
from types import ModuleType
from . import libflip
from .utils import load_module
from libflip.constants import *

def bootstrap():
    if len(sys.argv) == 1:
        print('Fivelines Instructional Platform\n')
        print('Running a Game:')
        print('   flip some_file.py\n')
        print('Create a New Game:')
        print('   flip new some_game\n')
        print('Download a Game:')
        print('   flip pull some_game')
        print('   flip fetch some_game\n')

        sys.exit()
    if sys.argv[1] == 'new':
        new_game()
    elif sys.argv[1] == 'list':
        get_games()
    elif sys.argv[1] == 'pull' or sys.argv[1] == 'fetch':
        fetch_game()
    else:
        main()

def err():
    print('Error: Invalid Python file provided')
    sys.exit()

def main():
    try:
        run_mod = sys.argv[1:][0]
    except:
        err()

    path = os.path.join(os.getcwd(), run_mod)
    from . import api
    code, mod = load_module(path, api)

    dummy_mod = ModuleType('dummy')

    try:
        exec(code, dummy_mod.__dict__)
    except:
        pass
    finally:
        WIDTH = getattr(dummy_mod, 'WIDTH', 16)
        HEIGHT = getattr(dummy_mod, 'HEIGHT', 16)
        TITLE = getattr(dummy_mod, 'TITLE', '{flip}')
        SIZE = getattr(dummy_mod, 'SIZE', 50)
        COLLISIONS = getattr(dummy_mod, 'PIXEL_COLLISIONS', True)

    libflip.init(path, WIDTH * SIZE, HEIGHT * SIZE, TITLE, grid = SIZE, collisions = COLLISIONS)

    exec(code, mod.__dict__)

    while True:
        libflip.main_loop()

def fetch_game():
    if len(sys.argv) != 3:
        print('Usage: flip fetch <game>')
        sys.exit()
    game = sys.argv[2]

    if os.path.exists(game):
        prompt = input('{} already exists. Overwrite? (Y or N): '.format(game))
        if prompt.upper() == 'Y':
            shutil.rmtree(game)
        else:
            sys.exit()

    url = 'http://fivelines.io/games/' + game + '.zip'
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            with ZipFile(BytesIO(data)) as dnld:
                dnld.extractall()
            print('Download Complete!')
    except:
        print('Unable to fetch game {} from {}. Does it exist?'.format(game, url))
        traceback.print_exc()

def new_game():
    if len(sys.argv) != 3:
        print('Usage: flip new <game>')
        sys.exit()
    game = sys.argv[2]
    if os.path.exists(game):
        prompt = input('{} already exists. Overwrite? (Y or N): '.format(game))
        if prompt.upper() == 'Y':
            shutil.rmtree(game)
        else:
            sys.exit()
    os.mkdir(game)
    os.mkdir(game + '/backgrounds')
    os.mkdir(game + '/images')
    os.mkdir(game + '/sounds')
    os.mkdir(game + '/actors')
    file = open(game + '/game.py', 'w')
    file.write('WIDTH = 30\n')
    file.write('HEIGHT = 20\n')
    file.write('TITLE = \'Simple Game\'\n')
    file.close()
