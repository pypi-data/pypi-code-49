"""Snips NLU engine module."""
from pathlib import PurePath

from snips_nlu import SnipsNLUEngine

#: The trained NLU engine of the bot.
engine = SnipsNLUEngine.from_path(
    PurePath(__file__).parent.with_name('nlu_engine')
)

#: Predefined responses to some basic intents.
responses = {
    'greeting': 'Hello! What would you like to do?',
    'goodbye': 'See you later!',
    'help': (
        'I can find the details or cast of films. '
        'Most of the time...\nGo here for examples: '
        'https://gitlab.com/ObserverOfTime/filmaster#examples'
    )
}

__all__ = ['engine', 'responses']
