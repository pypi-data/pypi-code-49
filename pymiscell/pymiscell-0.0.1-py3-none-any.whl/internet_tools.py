"""Internet related tools.

Intended to be used within a Python 3 environment.
Developed by Rodrigo Rivero.
https://github.com/rodrigo1392

"""

import requests


def send_message_2telegram_bot(bot_token, bot_chat_id, bot_message):
    """Send telegram message through a bot.

    Parameters
    ----------
    bot_token : str
        Token of telegram bot
    bot_chat_id : str
        ID from bot chat.
    bot_message : str
        Message to be sent.

    Returns
    -------
    json
        Details of the telegram message object.
    """
    send_text = 'https://api.telegram.org/bot' + bot_token +\
                '/sendMessage?chat_id=' + bot_chat_id + \
                '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
