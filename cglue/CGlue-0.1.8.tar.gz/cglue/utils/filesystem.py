import os
import shutil
from contextlib import suppress


class FileTransaction:
    def __init__(self, root):
        self._root = root
        self._new_folders = []
        self._files = {}

    def create_folder(self, folder):
        self._new_folders.append(folder.replace('/', os.path.sep))

    def update_file(self, file_name, contents):
        self._files[file_name.replace('/', os.path.sep)] = contents

    def apply(self, delete_backups=False):
        backups = {}
        new_files = []
        try:
            self._create_new_folders()

            for file_name, contents in self._files.items():
                self._apply_file_change(file_name, contents, backups, new_files)

            if delete_backups:
                self._delete_backups(backups)

        except Exception:
            self._revert(backups, new_files)
            raise

    def _apply_file_change(self, file_name, new_contents, backups, new_files):
        file_path = os.path.join(self._root, file_name)
        result = change_file(file_path, new_contents)
        if type(result) is str:
            print(f'Modified: {file_path}')
            backups[file_path] = result
        elif result:
            print(f'Created: {file_path}')
            new_files.append(file_path)
        else:
            print(f'Up to date: {file_path}')

    def _delete_backups(self, backups):
        for file_name, backup in backups.items():
            print(f'Deleted: {backup}')
            delete(backup)

    def _create_new_folders(self):
        for folder in self._new_folders:
            try:
                os.makedirs(os.path.join(self._root, folder))
                print(f'New folder: {folder}')
            except OSError:
                print(f'Skipped folder: {folder}')

    def _revert(self, backups, new_files):
        for file_name in new_files:
            delete(file_name)
        for file_name, backup in backups.items():
            delete(file_name)
            shutil.move(backup, file_name)
        for folder in self._new_folders:
            shutil.rmtree(folder)


def change_file(filename, contents, delete_backup=False):
    """
    Update filename with contents

    If the file already exists, copies it to a unique backup file
    :param delete_backup: Delete backup file on success
    :param filename: the filename to write to
    :param contents: new file contents
    :return: True if the file is created, False if up to date, string if a backup was created before write
    """
    try:
        with open(filename, "r") as f:
            file_changed = contents != f.read()
        file_exists = True
    except FileNotFoundError:
        file_changed = True
        file_exists = False

    if file_exists:
        if not file_changed:
            return False

        i = 0
        backup = filename + ".bak"
        while os.path.isfile(backup):
            i += 1
            backup = f"{filename}.bak{i}"

        copy_file(filename, backup)

        with open(filename, "w+") as f:
            f.write(contents)

        if delete_backup:
            delete(backup)
            backup = True

        return backup
    else:
        with open(filename, "w+") as f:
            f.write(contents)

        return True


def delete(path):
    with suppress(FileNotFoundError):
        os.remove(path)


def copy_file(src, dst):
    shutil.copy(src, dst)
    print(f'Copied: {src} -> {dst}')
