from .util import check_column_exist
from .util import add_column
import pymysql

def alter_method(conn, config):
    '''Alter the method table
    Purpose: to add more hyperparameters to the table

    Parameter:
        - conn (object): mysql connection
        - config (dict): specify the hyperparameter name and
                         data type
    '''

    # Add new fields if not exists in `method` table
    cur = conn.cursor()
    for column in config['method']:
        datatype = config['method'][column]
        if check_column_exist(conn, config['db'], 'method', column):
            if config['verbose']:
                print('[method|error] alter_method(%s, %s), reason: field existed' % (column, datatype))
        else:
            if config['verbose']:
                add_column(conn, 'method', column, datatype)
                print('[method|ok] alter_method(%s, %s)' % (column, datatype))
#    # Add unique constraint for all fields
#    fields = ','.join(config['method'].keys())
#    query = '''ALTER TABLE method ADD UNIQUE unique_index (%s) ''' % (fields)
#    print(query)
#    cur.execute(query)
#    conn.commit()

def add_method(conn, config, **kwargs):
    '''Add the method with hyperparameters

    Parameter:
        - conn (object): mysql connection
        - kwargs: <key> is hyperparameter name
                  corresponding <value> is the value
    '''
    cur = conn.cursor()
    fields = ','.join(kwargs.keys())
    values = []
    for _ in kwargs.values():
        if type(_) == str:
            values.append("'%s'" % _)
        else:
            values.append(str(_))
    values = ','.join(values)
    query = 'INSERT INTO method (%s) VALUES (%s)' % (fields, values)
    try:
        cur.execute(query)
        conn.commit()
    except pymysql.err.IntegrityError:
        if config['verbose']:
            print('[method|error] add_method(%s), reason: method duplicated' % values)
    else:
        if config['verbose']:
            print('[method|ok] add_method(%s)' % values)

def get_method_id(conn, config, **kwargs):
    cur = conn.cursor()
    values = []
    for key in kwargs.keys():
        value = kwargs[key]
        if type(value) == str:
            values.append("%s='%s'" % (key, value))
        else:
            values.append("%s=%s" % (key, str(value)))
    query = '''SELECT id FROM method WHERE %s''' % ' AND '.join(values)
    cur.execute(query)
    return cur.fetchone()[0]

















