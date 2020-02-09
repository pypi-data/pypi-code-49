class User:
    """This class represents an User no matter if it's an real user or an bot

    :param id_unique: Unique id of the target
    :type id_unique: int
    :param is_bot: Gives information whether the user is a bot or not
    :type is_bot: bool
    :param first_name: User's or bot's first name
    :type first_name: str
    :param last_name: User's or bot's last name
    :type last_name: str, optional
    :param username: User's or bot's username
    :type username: str, optional
    :param language_code: IETF language tag of the user's language
    :type language_code: str, optional
    """
    def __init__(self, *, id_unique, is_bot, first_name, last_name=None, username=None, language_code=None):
        self.id_unique = id_unique
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.language_code = language_code
