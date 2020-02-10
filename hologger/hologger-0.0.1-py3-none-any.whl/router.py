class HoLoggingRouter:

    @staticmethod
    def db_for_read(model, **hints):
        if hasattr(model, 'ho_logger'):
            return 'ho_logger'
        return None

    @staticmethod
    def db_for_write(model, **hints):
        if hasattr(model, 'ho_logger'):
            return 'ho_logger'
        return None

    @staticmethod
    def allow_relation(obj1, obj2, **hints):
        obj1_db = "default"
        obj2_db = "default"
        if hasattr(obj1, 'ho_logger'):
            obj1_db = "ho_logger"
        if hasattr(obj2, 'ho_logger'):
            obj2_db = "ho_logger"

        if obj1_db == obj2_db:
            return True
        return None

    @staticmethod
    def allow_migrate(db, app_label, model_name=None, **hints):
        return True
