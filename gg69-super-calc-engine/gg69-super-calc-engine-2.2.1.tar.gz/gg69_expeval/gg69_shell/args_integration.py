from typing import Type, List, Tuple
from gg69_expeval.ulib.useful import UsefulObj
from .shell import GG69Shell


class Option(UsefulObj):
    args_trick = ["name", "short", "procedure", "description"]
    name: str
    short: str
    description: str
    procedure: Type


class ArgsIntegrationProcedure:
    def __init__(self, shell: GG69Shell, options: List[Option], args: List[str]):
        self.app = shell
        self.args = args
        self.options_shorted = {}
        self.options_full = {}
        self.data = {"__root__": []}
        # Crutch
        for option in options:
            if option.short:
                self.options_shorted[option.short] = option
            self.options_full[option.name] = option

    def get_option_from_rnd_name(self, name: str):
        # TODO: remove Crutch
        try:
            res = self.options_shorted[name]
        except KeyError:
            res = self.options_full[name]
        return res

    def __call__(self):
        # TODO: remove all crutches
        in_option = False
        # TODO: replace by None
        cur_option = Option()
        cur_procedure = OptionProcedure(self)
        for arg in self.args[1:]:
            if in_option:
                if cur_procedure.known_count[0]:
                    if len(cur_procedure.data) == cur_procedure.known_count[1]:
                        self.data[cur_option.name] = cur_procedure.data
                        in_option = False
                    else:
                        cur_procedure.data.append(arg)
                        continue
                else:
                    res = cur_procedure.add(arg)
                    if res:
                        in_option = False
                        self.data[cur_option.name] = cur_procedure.data
                    else:
                        continue

            if arg[0] == "-":
                cur_option = self.get_option_from_rnd_name(arg[1:])
                cur_procedure = cur_option.procedure()
                in_option = True
            else:
                self.data["__root__"].append(arg)


class OptionProcedure(UsefulObj):
    manager: ArgsIntegrationProcedure
    args_trick = ["manager"]
    data = []
    known_count: Tuple[bool, int] = (False, 0)

    def add(self, attr) -> bool:
        pass

    def treat(self):
        # TODO: make it useful
        pass
