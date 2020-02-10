import configparser as cfg
import logging

CONFIG_PATH = 'configs/database.cfg'


parser = cfg.ConfigParser()
try:
    parser.read(CONFIG_PATH)
except Exception as exc:
    print(exc)


MONGO_CONNECTION_STRING = parser.get('connection', 'MONGO_CONNECTION_STRING')

DATABASE_NAME = parser.get('database', 'DATABASE_NAME')
USERS_TABLE_NAME = parser.get('database', 'USERS_TABLE_NAME')
GUILDS_TABLE_NAME = parser.get('database', 'GUILDS_TABLE_NAME')

DEBUG = parser.get('debug', 'DEBUG', fallback=False)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('pvlv_database')

if DEBUG:
    logger.setLevel(logging.INFO)
else:
    logger.setLevel(logging.ERROR)


# data log retention in DB
MAX_RETENTION_HOUR = parser.get('values', 'MAX_RETENTION_HOUR', fallback=72)
MAX_RETENTION_DAY = parser.get('values', 'MAX_RETENTION_DAY', fallback=90)
MAX_RETENTION_MONTH = parser.get('values', 'MAX_RETENTION_MONTH', fallback=120)

# USER_DATA_LOG CONFIG
SAMPLE_STRING_LEN = parser.get('values', 'SAMPLE_STRING_LEN', fallback=30)
# Time spent to type
TIME_SAMPLE_VALUE = parser.get('values', 'TIME_SAMPLE_VALUE', fallback=11)
# XP gain by message
XP_SAMPLE_VALUE = parser.get('values', 'XP_SAMPLE_VALUE', fallback=12)
XP_MAX_VALUE = parser.get('values', 'XP_MAX_VALUE', fallback=15)
# XP for next level
XP_NEXT_LEVEL = parser.get('values', 'XP_NEXT_LEVEL', fallback=300)

# BITS gain by message
BITS_SAMPLE_VALUE = parser.get('values', 'BITS_SAMPLE_VALUE', fallback=5)
BITS_MAX_VALUE = parser.get('values', 'BITS_MAX_VALUE', fallback=2)

# cache
CACHE_INTERVAL_SECONDS = parser.get('cache', 'DB_SAVE_INTERVAL', fallback=600)  # 10 min
CACHE_MAX_ITEMS = parser.get('cache', 'MAX_CACHE_ITEMS', fallback=100)

# User MESSAGE destination
MSG_DISABLED = 0
MSG_DIRECT = 1
MSG_ON_SAME_CHAT = 2
MSG_ON_DEFAULT_CHAT = 3
MSG_ON_LOG_CHAT = 3
