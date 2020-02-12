import os
class Cli:
    def __init__(self):
        self._exclude = []
        self._args = {}

    def parse_args(self, list_args:list):
        """get a list of args and convert do dict of all args and values
        """    
        for i in range(len(list_args)):
            if list_args[i][0] == "-":
                try:
                    _next_arg = list_args[i + 1]
                    if _next_arg[0] != "-":
                        if _next_arg[0]=="'" or _next_arg[0]=='"':
                            arg_parts = []
                            firstKey = _next_arg[0]
                            for word in list_args[i+1:]:
                                arg_parts.append(word)
                                self._exclude.append(word)
                                if word[-1] == firstKey:
                                    break
                            self._args[list_args[i]] = ' '.join(arg_parts)[1:-1]
                            
                        else:
                            self._args[list_args[i]] = list_args[i + 1]
                            self._exclude.append(list_args[i + 1])
                    else:
                        self._args[list_args[i]] = True

                except IndexError:
                    self._args[list_args[i]] = True

            elif list_args[i] not in self._exclude:
                self._args[i] = list_args[i]
    
    def cmd__help(self, arg:any, list_args:dict, **kwargs)->None:
        help = """"
        This Class help you to build a cli more easyer:
        """
        print(help)

    def __get_cmds__(self)->dict:
        cmds = {}
        for method in self.__dir__():
            if "cmd_" == method[:4]:
                cmds[f'-{method[4:]}'.replace('_','-')] = self.__getattribute__(method)

        return cmds

        
    def run_commands(self, **kwargs)->None:
        _cmd = self.__get_cmds__()

        for key in self._args.keys():
            try:
                _cmd[key](self._args[key], self._args, **kwargs)
            except KeyError as k:
                _key = str(k)
                print(
                    f"Comando {_key if not _key.isdigit() else self._args[int(_key)]} não encontrado"
                )
            except TypeError as t:
                if type(_cmd[key]) == bool:
                    pass
                if type(_cmd[key]) == str:
                    print(_cmd[key])

            return None
        
    def listen_os(self,**kwargs):
        self.parse_args(os.sys.argv[1:])
        self.run_commands(**kwargs)
        
