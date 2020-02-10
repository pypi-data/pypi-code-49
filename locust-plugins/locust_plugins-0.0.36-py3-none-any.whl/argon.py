import gevent


class ArgonLocust(Locust):
    """
    A Locust for argon communication
    """

    def __init__(self):
        super(ArgonLocust, self).__init__()
        self.client = ArgonClient()
