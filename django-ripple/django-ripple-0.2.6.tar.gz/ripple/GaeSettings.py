from google.cloud import datastore


class Settings:
    """
    Get sensitive data setting from DataStore.

    key:String -> value:String
    key:String -> Exception

    Thanks to: Martin Omander @ Stackoverflow
    https://stackoverflow.com/a/35261091/1463812
    """

    client = datastore.Client()

    @staticmethod
    def get(name, default=None):

        query = Settings.client.query(kind='Settings')
        query.add_filter('name', '=', name)

        l = list(query.fetch())
        retval = None
        if len(l)>0:
            retval = list(query.fetch())[0]

        if not retval:
            if default is not None:
                return default
            Settings.set(name, 'Not Set')
            raise Exception(('Setting %s not found in the database. A placeholder ' +
                             'record has been created. Go to the Developers Console for your app ' +
                             'in App Engine, look up the Settings record with name=%s and enter ' +
                             'its value in that record\'s value field.') % (name, name))

        if str(retval['value']) == 'True' or str(retval['value']) == 'true':
            return True

        if str(retval['value']) == 'False' or str(retval['value']) == 'false':
            return False

        return retval['value']

    @staticmethod
    def set(name, value):

        key = Settings.client.key('Settings')
        entity = datastore.Entity(key=key)
        entity.update({'name': name, 'value': value})
        Settings.client.put(entity)
