class PollOption:
    """This class contains information about one answer option in a poll

    :param text: Option text, 1-100 characters
    :type text: str
    :param voter_count: Number of users that voted for this option
    :type voter_count: int
    """
    def __init__(self, *, text, voter_count):
        self.text = text
        self.voter_count = voter_count
