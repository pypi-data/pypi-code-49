import pg8000 as pg
import os

class ParseSQLFiles:
    def __init__(self, file_path):

        self.file_path = file_path
        self.file_string = ''
        self.sql_list = []

    def read_file(self):
        with open(self.file_path, "r", encoding='utf-8') as f:
            self.file_string = f.read()
        
    def make_sql_list(self):
        self.sql_list = self.file_string.split(';')

    def clean_sql_list(self):
        for i in range(len(self.sql_list)):
            self.sql_list[i] = self.sql_list[i].replace('\n',' ')
        self.sql_list.pop()
    	
    def get_sql_list(self):
        return self.sql_list


class DbConnecter:
    def __init__(self, config):
        self.config = config
        self.db_host = config["db_host"]
        self.db_name = config["db_name"]
        self.db_user = config["db_user"]
        self.db_pass = config["db_pass"]
        self.db_port = config["db_port"]
        self.db_con = None
        self.db_cur = None
        print(self.db_host)
        print(self.db_name)
        print(self.db_user)
        print(self.db_pass)
        print(self.db_port)

        self._establish_connection_()

    def __del__(self):

        self.db_con.close()
        print("Connection has been closed.")

    def commit_changes(self):

        self.db_con.commit()

    def _establish_connection_(self):

        self.db_con = pg.connect(
            host=self.db_host,
            port=self.db_port,
            database=self.db_name,
            user=self.db_user,
            password=self.db_pass,
        )
        self.db_cur = self.db_con.cursor()
        print("Connection has been established.")

    def execute_query(self, query):
        print(query)
        self.db_cur.execute(query)

    def execute_query_many(self, sql_template, tup):
        # You should use the method called transform_data_for_insert from this toolbox
        # in order to make data in the [(), (), ()..] format which is required here
        # tup is actually a list of tuples
        print(sql_template)
        self.db_cur.executemany(sql_template, tup)

    def read_query(self, query):

        self.db_cur.execute(query)
        result = self.db_cur.fetchall()

        return result

    def multiple_insert(self, schema, table, columns, values):

        if not isinstance(values[0], tuple) and isinstance(values, list):
            print("The input of multiple insert is not list of tuples.")
            sys.exit()

        values_string = ", ".join(["%s" for col in range(len(values[0]))])

        if isinstance(columns, list) or isinstance(columns, tuple):
            columns_string = ", ".join(columns)

        sql_template = (
            f"INSERT INTO {schema}.{table} ({columns_string}) VALUES ({values_string})"
        )

        self.execute_query_many(sql_template, values)

    def execute_queries_list(self, queries_list):

        for qr in queries_list:
            self.execute_query(qr)

    def transform_data_for_insert(self, *args):
        return list(zip(*args))


class QueriesRunner:
    def __init__(self, db_con, path):
        self.db_con = db_con
        self.path = path
        self.sql_list = []


    def read_queries(self):
        sql_parser = ParseSQLFiles(self.path)
        sql_parser.read_file()
        sql_parser.make_sql_list()
        sql_parser.clean_sql_list()
        self.sql_list = sql_parser.get_sql_list()


    def run_queries(self):
        self.db_con.execute_queries_list(self.sql_list)
        self.db_con.commit_changes()



def connect_to_database(config=None):
    if (config is None):
        config = {
            'db_host': os.environ['FANTASY_PI_DB_HOST'],
            'db_name': os.environ['FANTASY_PI_DB_NAME'],
            'db_user': os.environ['FANTASY_PI_DB_USER'],
            'db_pass': os.environ['FANTASY_PI_DB_PORT'],
            'db_port': os.environ['FANTASY_PI_DB_PASS']
        }
    db_con = DbConnecter(config)

    return db_con

