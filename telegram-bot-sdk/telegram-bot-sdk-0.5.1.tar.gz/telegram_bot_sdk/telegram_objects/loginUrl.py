class LoginUrl:
    """This class represents a parameter of the inline keyboard button used to automatically authorize a user

    :param url: An HTTP URL to be opened with user authorization data added to the query string when the button is \
    pressed. If the user refuses to provide authorization data, the original URL without information about the user \
    will be opened
    :type url: str
    :param forward_text: Optional: New text of the button in forwarded messages
    :type forward_text: str
    :param bot_username: Optional: Username of a bot, which will be user for user authorization. If not specified, \
    the bot's username will be assumed. The url's domain must be the same as the domain linked with the bot
    :type bot_username: str
    :param request_write_access: Optional: Pass True to request the permission for your bot to send messages to \
    the user
    :type request_write_access: bool
    """
    def __init__(self, *, url, forward_text=None, bot_username=None, request_write_access=None):
        self.url = url
        self.forward_text = forward_text
        self.bot_username = bot_username
        self.request_write_access = request_write_access
