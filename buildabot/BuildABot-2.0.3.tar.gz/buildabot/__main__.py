import logging
import json
from .bot import Bot


if __name__ == "__main__":
    # Setup logging
    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(
        filename='discord.log', encoding='utf-8', mode='a+')
    handler.setFormatter(logging.Formatter(
        '[%(asctime)s] <%(levelname)s> [%(name)s] %(message)s'))
    # logger.addHandler(handler)

    bot_logger = logging.getLogger('bot')
    bot_logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(
        filename='bot.log', encoding='utf-8', mode='a+')
    handler.setFormatter(logging.Formatter(
        '[%(asctime)s] <%(levelname)s> %(message)s'))
    bot_logger.addHandler(handler)

    bot = Bot(config=json.load(open('config.json')))

    bot.run()
