class Table:

    def __init__(self, db, name, *args, **kwargs):

        self.schema = db.credentials['db']
        self.name = name

        # Default state
        self.sql = None
        self.columns = '*'
        self.filters = {}
        self._limit = None
        self.order = None
        self.primary_key = None

        # Database connections
        self.db = db
        self.conn, self.curs = db.conn, db.curs
        self.host = db.credentials['host']

    def select(self, columns, *args, **kwargs):
        """Defines the columns selected"""

        # Type checking
        if columns == '*':

            self.columns = ['*']

        elif isinstance(columns, str):

            self.columns = [columns]

        elif not isinstance(columns, list):

            raise TypeError('columns must be str or list')

        return self

    def order_by(self, order, *args, **kwargs):
        """Appends a ORDER BY clausule to the query"""

        if not isinstance(order, dict):
            raise TypeError('order must be a dict {"column": "ASC|DESC"}')

        for value in order.values():

            if value not in ['ASC', 'DESC']:
                raise AttributeError('order directoin must be ASC or DESC')

        self.order = order

        return self

    def where(self, *filters):
        """Appends a where clausule to the query.
        Premisses:
            lists are converted to IN() statements.
            strings and ints are converted to = statements.
        """

        for f in filters:
            self.filters.update(f)

        return self

    def limit(self, limit, *args, **kwargs):
        """Appends a LIMIT clausule to the query"""

        if not isinstance(limit, int):
            raise TypeError('limit must be a int')

        if limit != 0:

            self._limit = limit

        return self

    def build(self, *args, **kwargs):
        """Builds the SQL"""

        self.sql = "/*Application: Tethys*/\n"
        self.sql += "SELECT {}".format(', '.join(self.columns))
        self.sql += ", CAST(UNIX_TIMESTAMP() * POW(10, 6) AS DECIMAL(25,9)) AS _sequence\n"
        self.sql += "FROM {}.{}\n".format(self.schema, self.name)

        if self.filters != {}:

            self.sql += "WHERE\n\t1=1\n"

            for c, f in self.filters.items():

                if isinstance(f, list):

                    self.sql += "\tAND {} IN({})\n".format(
                        c, ','.join([repr(v) for v in f])
                    )

                if isinstance(f, (str, int,)):

                    self.sql += "\tAND {} = {}\n".format(
                        c, repr(f)
                    )

        if self.order is not None:

            self.sql += "ORDER BY {}\n".format(
                ','.join(['{} {}'.format(k,v) for k, v in self.order.items()])
            )

        if self._limit is not None:
            self.sql += "LIMIT {}".format(self._limit)

        return self

    def execute(self):
        """Executes a query to check the table metadata and then executes the
        built sql"""

        self.build()

        self.curs.execute(self.sql)

        return self

    @property
    def fields(self):
        """Returns the table schema"""

        MYSQL_TYPE_MAP = {
            0: 'float64', 1: 'int2', 2: 'int2', 3: 'int4', 4: 'float64',
            5: 'float64', 6: 'null', 7: 'timestamp', 8: 'int64', 9: 'int64',
            10: 'date', 11: 'time', 12: 'datetime', 13: 'year', 14: 'date',
            15: 'string', 16: 'int2', 17: 'datetime', 18: 'datetime',
            19: 'time', 245: 'string', 246: 'float64', 247: 'string',
            248: 'string', 249: 'string', 250: 'string', 251: 'string',
            252: 'string', 253: 'string', 254: 'string', 255: 'string',
        }

        fields = {
            field[0]: {
                'type': MYSQL_TYPE_MAP.get(field[1])
            } for field in self.curs.description if field[0] != '_sequence'
        }

        return fields

    @property
    def pk(self):
        """Returns the table primary key"""

        # This a cache. Do not remove!
        if self.primary_key is None:

            sql = f"""
            SELECT
                u.COLUMN_NAME
            FROM information_schema.TABLE_CONSTRAINTS c
            INNER JOIN information_schema.KEY_COLUMN_USAGE u
                ON c.TABLE_SCHEMA = u.TABLE_SCHEMA
                AND c.TABLE_NAME = u.TABLE_NAME
                AND c.CONSTRAINT_NAME = u.CONSTRAINT_NAME
            WHERE
                c.TABLE_SCHEMA = '{self.schema}'
                AND c.TABLE_NAME = '{self.name}'
                AND c.CONSTRAINT_TYPE = 'PRIMARY KEY'
            ORDER BY u.ORDINAL_POSITION ASC;
            """

            with self.conn as cursor:

                cursor.execute(sql)

                self.primary_key = [
                    row['COLUMN_NAME'] for row in cursor.fetchall()
                ]

        return self.primary_key

    def fetchall(self):
        """Fetches all the records."""

        for row in self.curs.fetchall():
            yield row

    def fetchmany(self, n=1000):
        """Fetches as many records as specified. Defaul: 1000"""

        return self.curs.fetchmany(n)

    def __iter__(self):
        """Iterates over the table records."""

        return self.fetchall()
