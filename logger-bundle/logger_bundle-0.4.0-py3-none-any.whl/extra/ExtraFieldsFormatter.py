import colorlog
from logging import PercentStyle
from loggerbundle.extra.ExtraKeysResolver import ExtraKeysResolver

class ExtraFieldsFormatter(colorlog.ColoredFormatter):

    def __init__(self, *args, **kwargs):
        self.__origFmt = args[0]

        super().__init__(*args, **kwargs)

    def format(self, record):
        extraKeys = ExtraKeysResolver.getExtraKeys(record)

        if not extraKeys:
            return super().format(record)

        def mapPlaceholder(fieldName):
            return '{}: %({})s'.format(fieldName, fieldName) # pylint: disable = duplicate-string-formatting-argument

        extraKeysPlaceholders = list(map(mapPlaceholder, extraKeys))

        self.__setFormat(self.__origFmt + '\n' + '{' + ', '.join(extraKeysPlaceholders) + '}')
        formated = super().format(record)
        self.__setFormat(self.__origFmt)

        return formated

    def __setFormat(self, fmt: str):
        self._fmt = fmt
        self._style = PercentStyle(self._fmt)
