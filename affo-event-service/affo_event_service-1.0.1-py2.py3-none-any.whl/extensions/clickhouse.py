from infi.clickhouse_orm.database import Database


class ClickHouse(object):

    param_names = [
        "DB_NAME",
        "DB_URL",
        "USERNAME",
        "PASSWORD",
        "READONLY",
        "AUTOCREATE",
        "TIMEOUT",
        "VERIFY_SSL_CERT",
        "LOG_STATEMENTS",
    ]

    def __init__(self, app=None, config_prefix="CLICKHOUSE"):
        self.config_prefix = config_prefix
        self.db = None
        if app is not None:
            self.init_app(app, config_prefix)

    def init_app(self, app, config_prefix="CLICKHOUSE"):
        """Initialize the `app` for use with this :class:`~ClickHouse`. This is
        called automatically if `app` is passed to :meth:`~ClickHouse.__init__`.

        The app is configured according to the configuration variables
        ``PREFIX_DB_NAME``, ``PREFIX_DB_URL``, ``PREFIX_USERNAME``,
        ``PREFIX_PASSWORD``, ``PREFIX_READONLY``, ``PREFIX_AUTOCREATE``,
        ``PREFIX_TIMEOUT``, ``PREFIX_VERIFY_SSL_CERT`` and
        ``LOG_STATEMENTS``,
        where "PREFIX" defaults to "CLICKHOUSE".

        :param flask.Flask app: the application to configure for use with
           this :class:`~ClickHouse`
        :param str config_prefix: determines the set of configuration
           variables used to configure this :class:`~ClickHouse`
        """
        self.config_prefix = config_prefix

        if "clickhouse" not in app.extensions:
            app.extensions["clickhouse"] = {}

        if config_prefix in app.extensions["clickhouse"]:
            raise Exception('duplicate config_prefix "%s"' % config_prefix)

        def key(suffix):
            return "%s_%s" % (config_prefix, suffix)

        app.config.setdefault(key("DB_URL"), "http://localhost:8123")
        app.config.setdefault(key("DB_NAME"), app.name)

        kwargs = {}

        for param in self.param_names:
            value = app.config.get(key(param))
            if value is not None:
                kwargs[param.lower()] = value

        self.db = Database(**kwargs,)

        app.extensions["clickhouse"][config_prefix] = self

    def __getattr__(self, name):
        return getattr(self.db, name)

    def __str__(self):
        return f"<ClickHouse: {self.host}>"
