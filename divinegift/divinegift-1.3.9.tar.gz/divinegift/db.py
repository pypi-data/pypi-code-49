from string import Template
import os
from sqlalchemy import create_engine, MetaData, Table
from deprecation import deprecated


class MethodNotAllowedError(Exception):
    pass


class Connection:
    def __init__(self, db_conn: dict, do_initialize=True):
        self.db_conn = db_conn

        self.engine = None
        self.conn = None
        self.metadata = None

        if do_initialize:
            self.set_conn()

    def set_conn(self):
        """
        Create connection for SQLAlchemy
        :param db_conn: DB connection (user, password, host, port, db_name, dialect)
        :return: Engine, Connection, Metadata
        """
        if self.db_conn.get('dialect') == 'mssql+pytds':
            from sqlalchemy.dialects import registry
            registry.register("mssql.pytds", "sqlalchemy_pytds.dialect", "MSDialect_pytds")
        if self.db_conn.get('db_host') and self.db_conn.get('db_port'):
            connect_str = '{dialect}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'.format(**self.db_conn)
        else:
            connect_str = '{dialect}://{db_user}:{db_pass}@{db_name}'.format(**self.db_conn)
        self.engine = create_engine(connect_str)
        self.conn = self.engine.connect()
        self.metadata = MetaData()

    def set_raw_conn(self):
        """
        Create raw connection for SQLAlchemy
        :param db_conn: DB connection (user, password, host, port, db_name, dialect)
        :return: Connection
        """
        if self.db_conn.get('dialect') == 'mssql+pytds':
            from sqlalchemy.dialects import registry
            registry.register("mssql.pytds", "sqlalchemy_pytds.dialect", "MSDialect_pytds")
        if self.db_conn.get('db_host') and self.db_conn.get('db_port'):
            connect_str = '{dialect}://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'.format(**self.db_conn)
        else:
            connect_str = '{dialect}://{db_user}:{db_pass}@{db_name}'.format(**self.db_conn)    
        self.engine = create_engine(connect_str)
        self.conn = self.engine.raw_connection()
        self.metadata = MetaData()

    def get_conn(self, fields = 'conn'):
        if isinstance(fields, str):
            return self.__dict__.get(fields)
        elif isinstance(fields, list):
            return tuple([self.__dict__.get(x) for x in fields])
        else:
            raise MethodNotAllowedError('This type of fields is not allowed')

    def close_conn(self):
        self.conn.close()

    @staticmethod
    def get_sql(filename: str, encoding: str = 'utf-8'):
        """
        Get sql string from file
        :param filename: File name
        :param encoding: Encoding of file
        :return: String with sql
        """
        with open(filename, 'r', encoding=encoding) as file:
            sql = file.read()
        return sql

    def get_data(self, sql: str, encoding: str = 'utf-8', print_script=False, **kwargs):
        """
        Get raw data from sql data as dict
        :param sql: File with sql which need to execute
        :param db_conn: DB connect creditions
        :param encoding: Encoding of file
        :param kwargs: List with additional data
        :return: Dictionary
        """
        if os.path.exists(sql):
            script_t = Template(self.get_sql(sql, encoding))
        else:
            script_t = Template(sql)
        script = script_t.safe_substitute(**kwargs)
        
        if print_script:
            print(script)

        res = self.conn.execute(script)
        ress = [dict(row.items()) for row in res]

        return ress

    def get_data_row(self, sql: str, index: int = 0, encoding: str = 'utf-8', **kwargs):
        """
        Get raw data from sql data as dict
        :param sql: File with sql which need to execute
        :param db_conn: DB connect creditions
        :param index: index of returning row
        :param encoding: Encoding of file
        :param kwargs: List with additional data
        :return: Dictionary
        """
        if os.path.exists(sql):
            script_t = Template(self.get_sql(sql, encoding))
        else:
            script_t = Template(sql)
        script = script_t.safe_substitute(**kwargs)

        res = self.conn.execute(script)
        ress = [dict(row.items()) for row in res]

        try:
            ress = ress[index]
        except:
            ress = None

        return ress

    def run_script(self, sql: str, encoding: str = 'utf-8', **kwargs):
        """
        Run custom script
        :param sql: File with sql which need to execute
        :param db_conn: DB connect creditions
        :param encoding: Encoding of file
        :param kwargs: List with additional data
        :return: None
        """    
        if os.path.exists(sql):
            script_t = Template(self.get_sql(sql, encoding))
        else:
            script_t = Template(sql)
        script = script_t.safe_substitute(**kwargs)

        self.conn.execute(script)


@deprecated(deprecated_in='1.3.9', current_version='1.3.9', details='Use class Connection instead')
def get_conn(db_conn: dict):
    conn_obj = Connection(db_conn)
    conn_obj.set_conn()
    return conn_obj.get_conn(['engine', 'conn', 'metadata'])


@deprecated(deprecated_in='1.3.9', current_version='1.3.9', details='Use class Connection instead')
def get_raw_conn(db_conn: dict):
    conn_obj = Connection(db_conn)
    conn_obj.set_raw_conn()
    return conn_obj.get_conn('conn')


@deprecated(deprecated_in='1.3.9', current_version='1.3.9', details='Use class Connection instead')
def get_sql(filename: str, encoding: str = 'utf-8'):
    """
    Get sql string from file
    :param filename: File name
    :param encoding: Encoding of file
    :return: String with sql
    """
    file = open(filename, 'r', encoding=encoding)
    sql = file.read()
    file.close()
    return sql


@deprecated(deprecated_in='1.3.9', current_version='1.3.9', details='Use class Connection instead')
def get_data(sql: str, db_conn, encoding: str = 'utf-8', print_script=False, **kwargs):
    conn_obj = Connection(db_conn)
    if isinstance(db_conn, dict):
        conn_obj.set_conn()
    else:
        conn_obj.conn = db_conn
    ress = conn_obj.get_data(sql, encoding, print_script, **kwargs)

    return ress


@deprecated(deprecated_in='1.3.9', current_version='1.3.9', details='Use class Connection instead')
def get_data_row(sql: str, db_conn: dict, index: int = 0, encoding: str = 'utf-8', **kwargs):
    conn_obj = Connection(db_conn)
    if isinstance(db_conn, dict):
        conn_obj.set_conn()
    else:
        conn_obj.conn = db_conn
    ress = conn_obj.get_data_row(sql, index, encoding, **kwargs)

    return ress


@deprecated(deprecated_in='1.3.9', current_version='1.3.9', details='Use class Connection instead')
def run_script(sql: str, db_conn: dict, encoding: str = 'utf-8', **kwargs):
    conn_obj = Connection(db_conn)
    if isinstance(db_conn, dict):
        conn_obj.set_conn()
    else:
        conn_obj.conn = db_conn
    conn_obj.run_script(sql, encoding, **kwargs)


if __name__ == '__main__':
    pass
