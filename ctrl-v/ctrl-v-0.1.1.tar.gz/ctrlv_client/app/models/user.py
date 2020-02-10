from ctrlv_client.app import login_manager, SITE_CONFIG_FILE
from werkzeug.security import check_password_hash
import json
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, username):
        self.username = username

    def verify_password(self, password):
        try:
            with open(SITE_CONFIG_FILE, "r") as jsonFile:
                site_config = json.load(jsonFile)
                return (
                    site_config["username"] == self.username and
                    check_password_hash(
                        site_config.get("password_hash"),
                        password
                    )
                )
        except FileNotFoundError:
            return False

    def get_id(self):
        return self.username


@login_manager.user_loader
def load_user(username):
    return User(username)
