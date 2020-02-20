from keyring.backend import KeyringBackend
from keyring.util import properties
from keyrings.lastpass.lpass import load_notes, save_notes
from keyrings.lastpass.cli import lastpass_installed

# from keyring import errors

PRIORITY = 10


class LastPassKeyring(KeyringBackend):
    @properties.ClassProperty
    @classmethod
    def priority(cls):
        if not lastpass_installed():
            raise RuntimeError("Requires lastpass cli")

        return PRIORITY

    def get_password(self, service, username):
        # print("get: " + service + " " + username)
        notes = load_notes(service)
        if username in notes:
            return notes[username]
        else:
            return None

    def set_password(self, service, username, password):
        # print("set: " + service + " " + username + " " + password)
        notes = load_notes(service)
        notes[username] = password
        save_notes(service, notes)
        # raise errors.PasswordSetError("reason")

    def delete_password(self, service, username):
        # print("delete: " + service + " " + username)
        notes = load_notes(service)
        del notes[username]
        save_notes(service, notes)
