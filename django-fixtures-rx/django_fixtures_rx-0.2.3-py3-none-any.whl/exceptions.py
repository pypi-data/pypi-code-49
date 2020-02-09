class FixturesException(Exception):
    pass


class FixturesNotFound(Exception):
    def __init__(self, app_label: str):
        super().__init__(f'Unable to found fixtures in \'{app_label}\'.')


class FixtureNotFound(Exception):
    def __init__(self, accessor: str):
        super().__init__(f'Unable to found \'{accessor}\' fixture.')
