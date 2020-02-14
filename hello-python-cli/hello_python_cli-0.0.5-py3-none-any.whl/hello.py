import hello_module.utils


class Hello():

    def __init__(self, name=''):
        self.name = name
        self.title = ''

    def hello(self):
        title = ''
        if self.title:
            title = '{} '.format(self.title)
        return 'Hello {}{}'.format(title, self.name)

    def transform(self):
        """Silly example on how to call function from another file."""
        return hello_module.utils.lower(self.hello())
