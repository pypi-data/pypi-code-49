import argparse as ap
import logging as log
from os import getenv
from sys import argv
from typing import List

from discord import Activity, ActivityType, Message

import filmaster as fm
from filmaster import bot, nlu, tmdb

log.basicConfig(
    format='<%(asctime)s> {%(name)s} [%(levelname)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S', level=log.WARNING
)
logger = log.getLogger(fm.__name__)

# Fight Club reference easter egg
_DNTAFC = getenv('DO_NOT_TALK_ABOUT_FIGHT_CLUB')


def _prefix_type(string: str) -> str:
    if len(string) == 1:
        return string
    raise ap.ArgumentTypeError('must be a single character')


parser = ap.ArgumentParser(fm.__name__, description=fm.__doc__)
parser.add_argument(
    '-V', '--version', action='version',
    version=f'{fm.__name__} {fm.__version__}'
)
parser.add_argument(
    '-v', '--verbose', action='count', default=0,
    help='increase the verbosity level'
)
parser.add_argument(
    '-t', '--tmdb-api-key', required=True,
    help='use this key to authenticate with TMDB'
)
parser.add_argument(
    '-d', '--discord-token', required=True,
    help='use this token to authenticate with Discord'
)
parser.add_argument(
    '-p', '--prefix', default=bot.PREFIX, type=_prefix_type,
    help=f'use this command prefix (default: {bot.PREFIX})'
)


@bot.client.event
async def on_ready():
    logger.info('Hello, human. My name is Film Master.')
    await bot.client.change_presence(activity=Activity(
        name='The Matrix', type=ActivityType.watching
    ))


@bot.client.event
async def on_message(message: Message):
    user = bot.client.user
    if message.author is user:
        return  # ignore own messages
    query = message.clean_content
    if not (query[:1] == bot.PREFIX or user in message.mentions):
        return  # only respond to prefix or mention
    logger.info('received: %s', query)
    parsed = nlu.engine.parse(query.lstrip(bot.PREFIX))
    logger.debug('parsed: %s', parsed)
    intent = parsed['intent']['intentName']
    if intent in nlu.responses:
        await message.channel.send(
            f'{message.author.mention} {nlu.responses[intent]}'
        )
    elif _DNTAFC and 'fight club' in query.lower():
        await message.channel.send('We do not talk about Fight Club.')
    elif intent in ('film_info', 'film_cast'):
        msg = await message.channel.send('Processing...')
        try:
            _get = tmdb.get_film if intent == 'film_info' else tmdb.get_cast
            embed = bot.FilmEmbed.from_film(_get(**{
                s['slotName']: s['value']['value'] for s in parsed['slots']
            }), cast=(intent == 'film_cast'))
        except tmdb.ApiError as err:
            log.warning(str(err))
            await message.channel.send(f'{message.author.mention} {err}')
        except Exception as exc:
            logger.exception(exc)
            await message.channel.send(
                f'{message.author.mention} Something went'
                ' horribly wrong. Contact an administrator.'
            )
        else:
            await message.channel.send(message.author.mention, embed=embed)
        finally:
            await msg.delete()
    else:
        log.warning('no intent found for: %s', query)
        await message.channel.send(
            f'{message.author.mention} Sorry. I could'
            ' not understand you. Please try again.'
        )


def run(args: List[str] = argv[1:]):
    args = parser.parse_args(args)
    if args.verbose == 1:
        logger.setLevel(log.INFO)
    elif args.verbose == 2:
        logger.setLevel(log.DEBUG)
    elif args.verbose == 3:
        log.getLogger().setLevel(log.INFO)
        logger.setLevel(log.DEBUG)
    elif args.verbose > 3:
        log.getLogger().setLevel(log.DEBUG)
    tmdb.api.TMDB_API_KEY = args.tmdb_api_key
    bot.PREFIX = args.prefix
    bot.client.run(args.discord_token)


if __name__ == '__main__':
    run()
