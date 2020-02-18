from os import environ

# Main server url | Need for modules
global server_url
server_url = 'https://raw.githubusercontent.com/LimerBoy/hackpy/master/modules/'

# Install path
try:
    global main_path
    global temp_path
    main_path = environ['TEMP'] + '\\hackpy\\'
    temp_path = main_path + 'tempdata\\'
except:
    raise OSError('ERROR! Hackpy created only for Windows systems!')
