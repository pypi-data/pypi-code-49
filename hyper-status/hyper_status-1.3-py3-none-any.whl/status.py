'''
> hyper_status
> Copyright (c) 2020 Xithrius
> MIT license, Refer to LICENSE for more info
'''


import datetime


c = {
    'date': '\033[93m',
    'fail': '\033[91m',
    'warn': '\033[95m',
    'ok': '\033[92m',
    'bold': '\033[1m',
    'under': '\033[4m',
    'end': '\033[0m'
}


class Status:

    def __init__(self, warning=' ', status=None):
        '''Creates attributes and formats everything for output

        Args:
            status (str): The status of what's currently happening
            warning (str): The custom string that the user wants to use.

        '''
        self.c = c
        self.warning = warning
        self.status = status

        self.insert_items()

    def _join(self, lst: list, _sep=' ') -> str:
        return _sep.join(str(y) for y in lst)

    def insert_items(self, starter='~>'):
        '''Gets information collected so far and returns the custom status.

        Args:
            n (str): the datetime.datetime object to be formatted.

        Returns:
            A joined list of all formatted items.

        Raises:
            Possible IndexErrors if color cannot be found.

        '''
        # Bold, and the color indicating the end of the previous one
        b = self.c['bold']
        e = self.c['end']

        # Creating the time.
        n = datetime.datetime.now()

        # Formatting time
        t = self._join(n.strftime('%I %M %S').split(), ':')
        n = f"{n.strftime('%b %d %Y, %A')} {t}{n.strftime('%p').lower()}"

        if self.status:
            # Setting title and color
            title = self.status.title()
            color = self.status

            # Making all status strings use the same length
            spacer = max(map(len, self.c.keys())) + 6
            spacer = (spacer - len(self.status)) // 2
            spacer = int(spacer) * ' '
        
        # Putting everything into a list.
        lst = [
            # Formatted date within brackets.
            f"{starter} {b}[{e} {self.c['date']}{n}{e} {b}]{e}",
            # The status given by the user
            f"> {b}[{e}{spacer}{self.c[color]}{title}{e}{spacer}{b}]{e}:" if self.status else '>',
            # Putting the warning string into the status, with a small amount of formatting.
            f"{self.warning.capitalize() if not self.warning[0].isupper() else self.warning}"
        ]

        # Returns the list as a string, joined together by a space.
        print(self._join(lst))


def preview():
    Status('This is a test warning. Be warned!', 'warn')
    Status('Oh no, something has totally failed!', 'fail')
    Status('This is fine. Everything is fine.', 'ok')
    Status('Something happened.')
    Status()

    all_colors = ', '.join(f'{v}{k}{c["end"]}' for k, v in c.items() if k != 'end')
    Status(f'All colors: {all_colors}')


if __name__ == "__main__":
    preview()
