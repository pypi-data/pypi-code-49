from django.db.backends.utils import CursorWrapper as BaseCursorWrapper


class CursorWrapper(BaseCursorWrapper):
    def _execute(self, sql, params, *ignored_wrapper_args):
        self.db.validate_no_broken_transaction()
        with self.db.wrap_database_errors:
            if params is None:
                try:
                    return self.cursor.execute(sql)
                except:
                    import ipdb; ipdb.set_trace()
                    print(sql)
            else:
                try:
                    return self.cursor.execute(sql, params)
                except:
                    import ipdb; ipdb.set_trace()
                    print(sql)
