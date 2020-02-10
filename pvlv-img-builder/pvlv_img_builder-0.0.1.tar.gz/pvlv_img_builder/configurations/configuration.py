import os
import configparser as cfg


CONFIG_PATH = 'configs/img_builder.cfg'


parser = cfg.ConfigParser()
try:
    parser.read(CONFIG_PATH)
except Exception as exc:
    print(exc)

# Debug
DEBUG = parser.get('debug', 'DEBUG', fallback=False)

# colors
GRAY = parser.get('colors', 'GRAY', fallback=(105, 105, 105))
GRAY_BLUE = parser.get('colors', 'GRAY_BLUE', fallback=(180, 180, 255))
DARK_GRAY = parser.get('colors', 'DARK_GRAY', fallback=(62, 62, 62))
LIGHT_GRAY = parser.get('colors', 'LIGHT_GRAY', fallback=(180, 180, 180))
LIGHT_GRAY1 = parser.get('colors', 'LIGHT_GRAY1', fallback=(200, 200, 200))
LIGHT_GRAY2 = parser.get('colors', 'LIGHT_GRAY2', fallback=(230, 230, 230))

WHITE = parser.get('colors', 'WHITE', fallback=(255, 255, 255))
BLACK = parser.get('colors', 'BLACK', fallback=(0, 0, 0))
BLUE = parser.get('colors', 'BLUE', fallback=(0, 0, 255))
RED = parser.get('colors', 'RED', fallback=(255, 0, 0))
GREEN = parser.get('colors', 'GREEN', fallback=(0, 128, 0))

GOLD = parser.get('colors', 'GOLD', fallback=(212, 175, 55))
SILVER = parser.get('colors', 'SILVER', fallback=(192, 192, 192))
BRONZE = parser.get('colors', 'BRONZE', fallback=(205, 127, 50))

# Colors for print out data
BACKGROUND_COLOR = parser.get('default', 'BACKGROUND_COLOR', fallback=DARK_GRAY)
TITLE_COLOR = parser.get('default', 'TITLE_COLOR', fallback=LIGHT_GRAY2)
TEXT_COLOR = parser.get('default', 'TEXT_COLOR', fallback=LIGHT_GRAY)

# Configuration of Graph bars
DEFAULT_TOWER_1_COLOR = parser.get('graph', 'DEFAULT_TOWER_1_COLOR', fallback=GRAY)
DEFAULT_TOWER_2_COLOR = parser.get('graph', 'DEFAULT_TOWER_2_COLOR', fallback=GRAY_BLUE)
DEFAULT_TOWER_3_COLOR = parser.get('graph', 'DEFAULT_TOWER_3_COLOR', fallback=GRAY_BLUE)

# Configuration of XP bar
BAR_A_COLOR = parser.get('xp_bar', 'BAR_A_COLOR', fallback=LIGHT_GRAY2)
BAR_B_COLOR = parser.get('xp_bar', 'BAR_B_COLOR', fallback=GRAY)
BAR_INSIDE_TEXT_A_COLOR = parser.get('xp_bar', 'BAR_INSIDE_TEXT_A_COLOR', fallback=GRAY)
BAR_INSIDE_TEXT_B_COLOR = parser.get('xp_bar', 'BAR_INSIDE_TEXT_B_COLOR', fallback=LIGHT_GRAY2)

# to adjust the font dimension (cause every font have its own measures)
FONT_MULTIPLIER = parser.get('fonts', 'FONT_MULTIPLIER', fallback=0)

dir_path = os.path.dirname(os.path.realpath(__file__))
DIR_DEFAULT_FONT = parser.get('fonts', 'DIR_DEFAULT_FONT', fallback='/fonts/Roboto-Black.ttf')
