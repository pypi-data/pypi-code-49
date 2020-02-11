#!/usr/bin/env python3

# TODO
# add clap
# add argument for log level
# add arguement for log file
# add argument for starting a demo for performance metrics
# add argument for setting a database file path
# add a clean option to remove old entries from the database
# move most of the setup to functions in reme.py

import reme 
import discord
import logging
import asyncio
from datetime import datetime

async def main():
    # set log level
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger("discord").setLevel(logging.INFO)
    logging.getLogger("discord.client").setLevel(logging.WARNING)
    logging.getLogger("discord.gateway").setLevel(logging.WARNING)
    logging.getLogger("websockets").setLevel(logging.WARNING)

    bot = reme.Reme()
    await bot.bootstrap()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except SystemExit:
        logging.info("Reme - A SystemExit signal has been received. Exiting!")
    except RuntimeError as e:
        logging.error(f"Reme - A RunTimeError occurred | {e}")
    except KeyboardInterrupt:
        logging.info("Reme - A KeyboardInterupt signal has been received. Exiting!")
    except Exception as e:
        logging.error(f"Reme - An unknown error occurred | {type(e)}: {e}")
        exit(1)