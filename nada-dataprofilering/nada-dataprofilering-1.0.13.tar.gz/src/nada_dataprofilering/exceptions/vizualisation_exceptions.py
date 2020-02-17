class VizualKeysNotFound(Exception):
    def __init__(self, mesg):
        self._mesg = mesg

    def __str__(self):
        return f"""
                Publish failed:
                {self._mesg}
                """
