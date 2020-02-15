class Module(object):
    def __init__(self, module_path, api_dict):
        self.__module_path = module_path
        self.__api_list = sorted(api_dict.keys())
        self.__dict__.update(api_dict)

    def __repr__(self):
        return '<module \'{module_path}\' with api: {api_list}>'.format(
            module_path=self.__module_path,
            api_list=self.__api_list
        )
