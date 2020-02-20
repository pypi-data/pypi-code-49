import pymysql

def add_instance(conn, config, name, kind):
    cur = conn.cursor()
    query = '''INSERT INTO instance (name, kind) VALUES ('%s', '%s')''' % (name, kind)
    try:
        cur.execute(query)
        conn.commit()
    except pymysql.err.IntegrityError:
        if config['verbose']:
            print('[instance|error] add_instance(%s, %s), reason: instance duplicated' % (name, kind))
    else:
        if config['verbose']:
            print('[instance|ok] add_instance(%s, %s)' % (name, kind))

def get_instance_id(conn, config, name, kind):
    cur = conn.cursor()
    query = '''SELECT id FROM instance WHERE name='%s' AND kind='%s' ''' % (name, kind)
    cur.execute(query)
    return cur.fetchone()[0]

def get_instance_by_id(conn, config, instance_id):
    cur = conn.cursor()
    query = 'SELECT * FROM instance WHERE id=%d' % instance_id
    cur.execute(query)
    return cur.fetchone()
