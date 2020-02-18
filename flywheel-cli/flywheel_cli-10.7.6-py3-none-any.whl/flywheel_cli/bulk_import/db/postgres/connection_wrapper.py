"""Wrap database connection, to normalize differences between sqlite and psycopyg2"""

def convert_params(qs):
    """Convert from qmark to %s params"""
    return qs.replace('%', '%%').replace('?', '%s')

class CursorWrapper:
    """
    Provides rewriting parameters from qmark (?) to format (%s)
    and a functional lastrowid.
    """
    def __init__(self, conn, impl):
        self._conn = conn
        self._impl = impl

    def execute(self, query, args=None):
        """Execute the given query/command

        Arguments:
            query {str} -- Query

        Keyword Arguments:
            args {tuple} -- Query params (default: {None})
        """
        query = convert_params(query)
        if args is None:
            args = ()
        return self._impl.execute(query, args)

    def executemany(self, query, args_seq):
        """Execute query/command against all parameter sequences

        Arguments:
            query {str} -- Query
            args_seq {iterable} -- parameter sequences
        """
        query = convert_params(query)
        args_seq = [() if args is None else args for args in args_seq]
        return self._impl.executemany(query, args_seq)

    def callproc(self, proc_name, args=None):
        """Call stored procedure with given parameters

        Arguments:
            proc_name {str} -- Procedure name

        Keyword Arguments:
            args {tuple} -- Parameters (default: {None})
        """
        proc_name = convert_params(proc_name)
        if args is None:
            args = ()
        return self._impl.callproc(proc_name, args)

    @property
    def lastrowid(self):
        """Return last row id by selecting lastval"""
        with self._conn.cursor() as cursor:
            cursor.execute('SELECT lastval()')
            return next(cursor)[0]

    def __getattr__(self, attr):
        return getattr(self._impl, attr)

    def __next__(self):
        return self._impl.__next__()

class ConnectionWrapper:
    """Wrapper that provides query wrapping and lastrowid for psycopg"""
    def __init__(self, impl):
        self._impl = impl

    def cursor(self):
        """Create cursor"""
        return CursorWrapper(self._impl, self._impl.cursor())

    def __enter__(self):
        self._impl.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._impl.__exit__(exc_type, exc_val, exc_tb)

    def __getattr__(self, attr):
        return getattr(self._impl, attr)
