from src.pvlv_database import ModuleConfigurationsData


class ModuleStatusData(object):

    def extract_data(self, raw_data):
        """
        The raw data (json) to wrap as class
        :param raw_data: json object
        :return: an instance of the class
        """

        try:
            for key in raw_data.keys():
                setattr(
                    self, key,
                    ModuleConfigurationsData().extract_data(raw_data.get(key, ModuleConfigurationsData().build_data()))
                )
        except Exception as exc:
            print('New User used Commands, db creation exception (accepted): ' + str(exc))
            pass

        return self

    def build_data(self):
        """

        :return: a json object
        """
        data_out = {}
        attrs = self.__dict__
        for key in attrs.keys():
            data_out[key] = attrs.get(key).build_data()

        return data_out

    def module(self, command_name):
        """
        Get the command object by his name

        :param command_name: the name of the command as in the command declaration file
        :return the command class
        """
        command_name = command_name.replace('.', '_')
        if command_name.replace('.', '_') in self.__dict__.keys():
            return getattr(self, command_name)
