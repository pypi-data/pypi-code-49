import os
import appdirs

from tempfile import gettempdir

APPNAME = 'spintop'
APPAUTHOR = 'tackv'

SITE_DATA_DIR = appdirs.user_data_dir(appname=APPNAME, appauthor=APPAUTHOR)

try:
    if not os.path.exists(SITE_DATA_DIR):
        os.makedirs(SITE_DATA_DIR)  
except OSError as e:
    print('Unable to create SITE_DATA_DIR. Do you have write access ? {}'.format(str(e)))
    
TEMP_DIR = os.path.join(gettempdir(), 'spintop')
