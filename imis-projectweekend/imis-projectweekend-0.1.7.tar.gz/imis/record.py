from imis.utils import snake_case


class BasicRecord:

    def __init__(self, **kwargs):
        self.__dict__ = {snake_case(k): v for k, v in  kwargs.items()}

    def __getattr__(self, name):
        try:
            return self.__dict__[name.lower()]
        except KeyError:
            raise AttributeError(f'{name} does not exist on this object')

    def __setattr__(self, name, value):
        super().__setattr__(snake_case(name), value)

    def __repr__(self):
        return '<BasicRecord>'

    def __str__(self):
        return repr(self)
