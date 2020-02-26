COLLECTOR_APPS = ['diagnosis', 'medicine', 'collection', 'topic']


class Router:
    def db_for_read(self, model, **hints):
        if model._meta.app_label in COLLECTOR_APPS:
            return 'collection'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in COLLECTOR_APPS:
            return 'collection'
        return 'default'

    # def allow_relation(self, obj1, obj2, **hints):
    #     '''Allow any relation between apps that use the same database.'''
    #     # db_obj1 = obj1._meta.app_label
    #     # db_obj2 = obj2._meta.app_label
    #     # if db_obj1 and db_obj2:
    #     #     if db_obj1 == db_obj2:
    #     #         return True
    #     #     else:
    #     #         return False
    #     return True

    # def allow_syncdb(self, db, model):
    #     """Make sure that apps only appear in the related database."""

    #     return True

    # def allow_migrate(self, db, app_label, model=None, **hints):
    #     """ Make sure the auth app only appears in the 'auth_db' database. """
    #     print("db: ", db)
    #     print("app_label: ", app_label)
    #     if app_label in ['medicine']:
    #         return 'collection'
    #     return 'default'
