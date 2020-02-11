from colorama import Fore, Style
import traceback
import time
import sys
from gg69_expeval.gg69_shell.detector import Detector
from gg69_expeval import ExpEval, ExpEvalProcedure
from .signal import Signal


class GG69Shell:
    def __init__(self):
        self.ex = ExpEval()
        # self.args_manager = ArgsIntegrationProcedure(self, std_options, sys.argv)
        # self.args_manager()
        # if self.args_manager.data["__root__"][0] == "help":
        #     for option in std_options:
        #         if option.description:
        #             print("%s (%s) - %s" % (option.name, option.short, option.description))
        #     sys.exit()
        # if "secret-key" in self.args_manager.data and self.args_manager.data["secret-key"][0] == 88005553535:
        #     print("Try me soon...")
        #     sys.exit()
        # else:
        #     detection_level = 0
        # self.detector = Detector(detection_level)
        self.detector = Detector(0)

    def __call__(self):
        while True:
            query = input(Fore.CYAN + "> " + Fore.RESET)
            try:
                time_start = time.time()
                result = ExpEvalProcedure(self.ex, query)()
                time_ready = time.time()
                print(Fore.YELLOW + query + Fore.WHITE + "=" + Fore.GREEN + self.detector.color_marked(str(result), Fore.GREEN) + Style.RESET_ALL)
                print("It took %d seconds to execute" % (time_ready - time_start))
            except Exception as err:
                if isinstance(err, Signal):
                    err: Signal
                    if err.name == "exit":
                        break
                else:
                    print(Fore.RED, end="")
                    print(traceback.format_exc(), end="")
                    print(Fore.RESET)
