"""
Global setting of VN Trader.
"""

from logging import CRITICAL

from .utility import load_json,save_json

SETTINGS = {
    "type":"none",
    "font.family": "Arial",
    "font.size": 12,

    "log.active": True,
    "log.level": CRITICAL,
    "log.console": True,
    "log.file": True,

    "email.server": "smtp.qq.com",
    "email.port": 465,
    "email.username": "",
    "email.password": "",
    "email.sender": "",
    "email.receiver": "",

    "rqdata.username": "",
    "rqdata.password": "",

    "database.driver": "mongodb",  # see database.Driver
    "database.database": "quant",  # for sqlite, use this as filepath
    "database.digit_currency": "btc",  # for sqlite, use this as filepath
    "database.host": "182.151.7.177",
    "database.port": 27017,
    "database.user": "admin",
    "database.password": "admin",
    "database.authentication_source": "admin",  # for mongodb

    "jqdata.username": "17745021310",
	"jqdata.password": "021310",
}

# Load global setting from json file.
SETTING_FILENAME = "settings.json"
# SETTINGS.update(load_json(SETTING_FILENAME))
save_json(SETTING_FILENAME,SETTINGS)

def get_settings(prefix: str = ""):
    prefix_length = len(prefix)
    return {k[prefix_length:]: v for k, v in SETTINGS.items() if k.startswith(prefix)}

def save_settings():
    save_json(SETTING_FILENAME, SETTINGS)
    return