from flask import render_template


# Custom error pages
def page_not_found(e):
    return render_template('error/404.html'), 404


def internal_server_error(e):
    return render_template('error/500.html'), 500


class Production:
    DEBUG = False
    TESTING = False
    ENV = 'production'
    # This will be overwritten by the values in
    # instance/config.py
    SECRET_KEY = 'production_secret_key'
    # Will create the file in the current folder
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../ctrlv_client.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Max age in seconds for CSRF tokens. Default is 3600.
    # If set to None, the CSRF token is valid for the life of the session.
    # https://flask-wtf.readthedocs.io/en/stable/config.html
    WTF_CSRF_TIME_LIMIT = None
    # https://stackoverflow.com/questions/42300316/
    # session-is-shared-between-two-flask-apps-on-localhost
    # The name of the session cookie.
    # Can be changed in case you already have a cookie with the same name.
    # Default: 'session'
    SESSION_COOKIE_NAME = 'ctrl-v-session'

    @staticmethod
    def init_app(app):
        # flask-quickstart/instance/config.py
        app.config.from_pyfile('config.py', silent=True)
        app.register_error_handler(404, page_not_found)
        app.register_error_handler(500, internal_server_error)
        return


class Development:
    DEBUG = True
    TESTING = False
    ENV = 'development'
    SECRET_KEY = 'development_secret_key'
    # Will create the file in the current folder
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_NAME = 'ctrl-v-development-session'
    # SQLALCHEMY_ECHO = True

    @staticmethod
    def init_app(app):
        app.register_error_handler(404, page_not_found)
        return


class Testing:
    DEBUG = False
    TESTING = True
    ENV = 'testing'
    SECRET_KEY = 'testing_secret_key'
    # Set to False CSRF tokens not handled
    # in unit tests
    # Testing logins
    WTF_CSRF_ENABLED = False
    # PRESERVE_CONTEXT_ON_EXCEPTION = False
    # https://gehrcke.de/2015/05/in-memory-sqlite-database-and-flask-a-threading-trap/
    # https://stackoverflow.com/questions/21766960/operationalerror-no-such-table-in-flask-with-sqlalchemy
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_COOKIE_NAME = 'ctrl-v-testing-session'

    @staticmethod
    def init_app(app):
        pass


config = {
    'production': Production,
    'development': Development,
    'testing': Testing
}
