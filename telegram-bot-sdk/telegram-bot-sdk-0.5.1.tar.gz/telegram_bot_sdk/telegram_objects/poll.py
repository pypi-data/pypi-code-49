from telegram_bot_sdk.telegram_objects.pollOption import PollOption


class Poll:
    """This class contains information about a poll

    :param id_unique: Unique poll identifier
    :type id_unique: str
    :param question: Poll question, 1-255 characters
    :type question: str
    :param options: List of poll options
    :type options: list of :ref:`object_poll_option`
    :param is_closed: True, if the poll is closed
    :type is_closed: bool
    """
    def __init__(self, *, id_unique, question, options, is_closed):
        self.id_unique = id_unique
        self.question = question
        self.options = [PollOption(**x) for x in options] if options else None
        self.is_closed = is_closed
