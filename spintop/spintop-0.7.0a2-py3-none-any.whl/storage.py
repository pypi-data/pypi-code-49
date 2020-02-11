import os
import appdirs

from tempfile import gettempdir

APPNAME = 'spintop'
APPAUTHOR = 'tackv'

SITE_DATA_DIR = appdirs.user_data_dir(appname=APPNAME, appauthor=APPAUTHOR)

if not os.path.exists(SITE_DATA_DIR):
    os.makedirs(SITE_DATA_DIR)  
    
TEMP_DIR = os.path.join(gettempdir(), 'spintop')
