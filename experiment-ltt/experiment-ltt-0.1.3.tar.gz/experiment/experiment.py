import yaml

def _create_default_instance_table(conn):
    cur = conn.cursor()
    cur.execute('''CREATE TABLE instance (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(512),
            kind VARCHAR(512))''')
    # Add unique constraint for all fields
    query = '''ALTER TABLE instance ADD UNIQUE unique_index (name, kind) '''
    cur.execute(query)
    conn.commit()

def _create_default_method_table(conn):
    cur = conn.cursor()
    cur.execute('''CREATE TABLE method(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(256))''')

def _create_default_iteration_table(conn):
    cur = conn.cursor()
    cur.execute('''CREATE TABLE iteration(
            id INT AUTO_INCREMENT PRIMARY KEY,
            method_id INT REFERENCES method(id),
            instance_id INT REFERENCES instance(id),
            best DOUBLE,
            mean DOUBLE,
            std DOUBLE,
            best_solution MEDIUMBLOB,
            num_iteration INT,
            num_evaluation INT,
            seed INT)''')
    query = 'ALTER TABLE iteration ADD UNIQUE unique_index (method_id, instance_id, num_iteration, seed)'
    cur.execute(query)
    conn.commit()

def create_experiment(conn, config):
    '''Create database and tables for the experiment.
    Create a table "experiment" that contain the experimental
    summarization

    Parameters:
        - conn (object): mysql connection
        - config (dict): contain db name
    '''
    cur = conn.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS %s' % config['db'])
    conn.select_db(config['db'])
    _create_default_instance_table(conn)
    _create_default_method_table(conn)
    _create_default_iteration_table(conn)
    if config['verbose']:
        print('[experiment|ok] create_experiment(%s)' % config['db'])

def drop_experiment(conn, config):
    '''Drop database contain experimental results

    Parameters:
        - conn (object): mysql connection
        - config (dict): contain db name
    '''
    cur = conn.cursor()
    cur.execute('DROP DATABASE IF EXISTS %s' % config['db'])
    if config['verbose']:
        print('[experiment|ok] drop_experiment(%s)' % config['db'])
