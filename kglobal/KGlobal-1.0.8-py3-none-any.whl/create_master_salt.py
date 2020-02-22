def create_master_salt_key():
    from . import master_salt_filepath
    from .data import create_salt
    salt_filepath = master_salt_filepath()
    create_salt(os.path.dirname(salt_filepath), os.path.basename(salt_filepath))

if __name__ == '__main__':
    create_master_salt_key()
