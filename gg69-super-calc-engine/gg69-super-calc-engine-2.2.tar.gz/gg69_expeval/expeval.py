from queue import Queue
import traceback
import logging
from typing import Dict, Tuple
from .expeval_std import std_names, std_specific_operators, CharOperator, Namespace, Operator
from .ulib.killable_thread import KillableThread
from gg69_expeval.gg69_shell.signal import Signal


class CalculationTimeoutExpired(Exception):
    pass


class ExpEval:
    names: Namespace
    specific_operators: Dict[str, CharOperator]

    @staticmethod
    def is_this_code_for_sending_result(code):
        return code == 0

    def __init__(self, names=None, specific_operators=None):
        # config
        if names is None:
            self.names = std_names
        else:
            self.names = names
        if specific_operators is None:
            self.specific_operators = std_specific_operators
        else:
            self.specific_operators = specific_operators
        self.other_symbols = list("()[]{},;.")  # They all 1 char length
        # {"second": "first"}
        self.pares = {">": "<", "\\": "/"}
        self.brackets = {"(": ")", "[": "]", "{": "}"}
        self.sep = ","

        # execution levels
        self.execution_levels_pre_set = set()

        def manage_namespace_for_operators_e_l(ns: Namespace):
            for ns_name in ns.cont.values():
                if isinstance(ns_name, Namespace):
                    manage_namespace_for_operators_e_l(ns_name)
                elif isinstance(ns_name, Operator):
                    self.execution_levels_pre_set.add(ns_name.level)
        manage_namespace_for_operators_e_l(self.names)
        self.execution_levels = sorted(list(self.execution_levels_pre_set), reverse=True)

        # operator_symbols
        self.operator_symbols = set()
        for name in list(self.specific_operators) + list(self.pares):
            for ch in name:
                self.operator_symbols.add(ch)

        # max operator size
        self.mx_op_size = max(map(lambda n: len(n), self.specific_operators.keys()))

        self.logger = logging.getLogger(__name__)

    def comp_exp(self, query) -> Tuple[str, bool]:
        """
        :param query: calculation query text
        :return: result, success (0 - success, 1 - exception, 2 - signal)
        """
        def exp_thread(config, request, queue):
            try:
                queue.put((ExpEvalProcedure(config, request)(), 0))
            except Exception as err:
                if isinstance(err, Signal):
                    queue.put((err, 2))
                else:
                    queue.put((traceback.format_exc(), 1))

        q = Queue()
        thread = KillableThread(target=exp_thread, args=(self, query, q))
        thread.start()
        thread.join(1)
        if thread.is_alive():
            thread.kill()
            raise CalculationTimeoutExpired()
        res = q.get()
        return res


class ExpEvalProcedure:
    def __init__(self, config: ExpEval, query):
        self.config = config
        self.query = query

    def __call__(self):
        tokenizer = Tokenizer(self, self.query)
        tokens = tokenizer()
        executor = Executor(self, tokens)
        return executor()


from .tokenizer import Tokenizer
from .executor import Executor
