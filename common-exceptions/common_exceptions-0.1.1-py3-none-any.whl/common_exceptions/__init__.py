
class UserNotExistError(Exception):
    def __init__(self, msg=''):
        self.msg = msg

    def __str__(self):
        return f'User not exist! {self.msg}'


class UserBannedError(Exception):
    def __init__(self, msg=''):
        self.msg = msg

    def __str__(self):
        return f'User is banned! {self.msg}'


class ArticleNotExistError(Exception):
    def __init__(self, msg=''):
        self.msg = msg

    def __str__(self):
        return f'Article is banned! {self.msg}'


class ArticleBannedError(Exception):
    def __init__(self, msg=''):
        self.msg = msg

    def __str__(self):
        return f'Article is banned! {self.msg}'
