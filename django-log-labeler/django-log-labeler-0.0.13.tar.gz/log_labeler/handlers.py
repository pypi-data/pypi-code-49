import sys
import logging
import structlog

try:
    unicode
    _unicode = True
except NameError:
    _unicode = False


class StructlogRawMessageHandler(logging.StreamHandler):
    level = logging.DEBUG
    filters = []
    lock = None
    _name = "StructlogRawMessageHandler"

    def __init__(self, stream=None):
        """
        Initialize the handler.

        If stream is not specified, sys.stderr is used.
        """
        logging.StreamHandler.__init__(self)
        if stream is None:
            stream = sys.stderr
        self.stream = stream

    def emit(self, record):
        try:
            print("#########################################")
            print("#########################################")
            print("#########################################")
            print("#########################################")
            print(self.format(record))
            msg = record.msg
            stream = self.stream
            fs = "%s\n"
            if not _unicode:  # if no unicode support...
                stream.write(fs % msg)
            else:
                try:
                    if (isinstance(msg, unicode) and
                            getattr(stream, 'encoding', None)):
                        ufs = u'%s\n'
                        try:
                            stream.write(ufs % msg)
                        except UnicodeEncodeError:
                            # Printing to terminals sometimes fails. For example,
                            # with an encoding of 'cp1251', the above write will
                            # work if written to a stream opened or wrapped by
                            # the codecs module, but fail when writing to a
                            # terminal even when the codepage is set to cp1251.
                            # An extra encoding step seems to be needed.
                            stream.write((ufs % msg).encode(stream.encoding))
                    else:
                        stream.write(fs % msg)
                except UnicodeError:
                    stream.write(fs % msg.encode("UTF-8"))
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
