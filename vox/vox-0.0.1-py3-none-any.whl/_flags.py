from vox import flaggy

_DEFAULTS = {
    "arg_sep": " ",
    "flag_sep": "=",
    "flag_join": ",",
    "commands": flaggy.Flags,
    "mapping": {},
    "name": flaggy.Null(),
    "flag": True,
    "order": 10,
}

_DEFAULT_FLAGS = {
    "--program": flaggy.Options(flag=False, order=0),
    "--files": flaggy.Options(flag=False, order=1),
}


class FlagsBuilder(flaggy.Builder):
    def __init__(self, flags=None, **options):
        if flags is None:
            flags = {}
        _flags = flaggy.deep_copy(_DEFAULT_FLAGS)
        flaggy.deep_update(_flags, flags)
        super().__init__(
            flaggy.Options(_DEFAULTS, **options), _flags,
        )
