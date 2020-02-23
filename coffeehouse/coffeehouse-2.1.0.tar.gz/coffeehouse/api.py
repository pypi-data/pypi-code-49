class API(object):

    def __init__(self, access_key, endpoint="https://api.intellivoid.info/coffeehouse"):
        """
        Public constructor for CoffeeHouse API

        :param access_key:
        :param endpoint:
        :return:
        """
        self.access_key = access_key
        self.endpoint = endpoint
