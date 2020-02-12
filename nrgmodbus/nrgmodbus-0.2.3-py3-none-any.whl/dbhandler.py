# from datetime import datetime
# import os
# import sqlite3


# class db(object):
#     """
#     sqlite3 database handler for nrgmodbus

#     """
#     def __init__(self, db_name=''):
#         self.db_name = db_name

#         if db_name == '':
#             self.db_name = "{0}_nrg_db.db".format(datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
#             pass

#     def create_db(self):
#         """
#         create a new sqlite3 database
#         """
#         os.makedirs(os.path.dirname(self.db_name), exist_ok=True)
#         try:
#             conn = sqlite3.connect(self.db_name)
#         except Exception as e:
#             print(e)
#         finally:
#             conn.close()

    
    def open_db(self):
        """
        open an existing sqlite3 database
        """
        pass


    def write_to_db(self):
        """
        write data to sqlite3 database
        """
        pass


    def read_from_db(self):
        """
        read from sqlite3 database
        """
        pass

