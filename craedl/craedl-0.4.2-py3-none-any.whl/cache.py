import sqlite3

class Cache():
    """
    This class handles all cache database operations. It is used largely in
    support of recursive file uploads and downloads.

    It operates by storing a SHA1 hash representing the time stamps for children
    within a given directory and a status bit that indicates whether the
    contents were successfully transferred at the time the hash was created.
    """

    db_conn = None
    db_cursor = None

    def close(self):
        """
        Close the database connection.
        """
        self.db_conn.close()

    def open(self, path):
        """
        Open the database connection. Create the database and requisite tables
        if they do not exist.

        :param path: the path to the database file
        :type path: string
        """
        self.db_conn = sqlite3.connect(path)
        self.db_cursor = self.db_conn.cursor()

        # create table if it does not already exist
        self.db_cursor.execute('''
            SELECT count(name)
            FROM sqlite_master
            WHERE type='table'
                AND name='dirs'
        ''')
        if self.db_cursor.fetchone()[0] != 1:
            self.db_cursor.execute('''
                CREATE TABLE dirs (
                    complete bit,
                    hash varchar(40) NOT NULL,
                    path varchar(1024) NOT NULL UNIQUE
                )
            ''')

    def check(self, dir_path, dir_hash):
        """
        Check whether a directory's hash matches and has successfully completed.
        In this case the check passes, returning `True`, so the directory may be
        safely skipped. Should the directory not exist, the hash not match, or
        the synchronization be incomplete, this returns `False` because it is
        unsafe to skip this directory.

        :param dir_path: the directory path
        :type: string
        :param dir_hash: the SHA1 hash for the timestamps of children of this
            directory
        :type dir_hash: string
        :returns: True if the directory and hash match the stored value and the
            transfer successfully completed; False otherwise
        """
        self.db_cursor.execute('''
            SELECT count(hash)
            FROM dirs
            WHERE hash=?
                AND path=?
                AND complete=1
        ''', (
            dir_hash,
            dir_path
        ))
        if self.db_cursor.fetchone()[0] == 1:
            return True
        return False

    def finish(self, dir_path, dir_hash):
        """
        Finish a transfer. Mark a directory with matching hash as complete.

        :param dir_path: the directory path
        :type: string
        :param dir_hash: the SHA1 hash for the timestamps of children of this
            directory
        :type dir_hash: string
        """
        self.db_cursor.execute('''
            UPDATE dirs
            SET complete=1
            WHERE hash=?
                AND path=?
        ''', (
            dir_hash,
            dir_path
        ))
        self.db_conn.commit()

    def start(self, dir_path, dir_hash):
        """
        Start a transfer. Create the directory and hash entry, and mark it as
        incomplete.

        :param dir_path: the directory path
        :type: string
        :param dir_hash: the SHA1 hash for the timestamps of children of this
            directory
        :type dir_hash: string
        """
        try:
            self.db_cursor.execute('''
                INSERT INTO dirs VALUES (
                    ?,
                    ?,
                    ?
                )
            ''', (
                0,
                dir_hash,
                dir_path,
            ))
            self.db_conn.commit()
        except sqlite3.IntegrityError:
            self.db_cursor.execute('''
                UPDATE dirs
                SET complete=0, hash=?
                WHERE path=?
            ''', (
                dir_hash,
                dir_path
            ))
            self.db_conn.commit()
