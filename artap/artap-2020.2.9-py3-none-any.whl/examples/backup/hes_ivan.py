import os

from artap.executor import CondorJobExecutor
from artap.problem import Problem
from artap.algorithm_bayesopt import BayesOptSerial
from artap.algorithm_nlopt import NLopt, LN_BOBYQA

from artap.results import Results, GraphicalResults


class OptProblem(Problem):
    def __init__(self, name):
        # important - nutne prepsat dle modelu (precision neumi algoritmy pouzit klidne smazat)
        """
        parameters = {'A': {'initial_value': 16e-3, 'bounds': [15e-3, 30e-3]},
                      'B': {'initial_value': 20e-3, 'bounds': [16e-3, 30e-3]},
                      'delta': {'initial_value': 2e-3, 'bounds': [1e-3, 5e-3]},
                      'Dind1': {'initial_value': 180e-3, 'bounds': [170e-3, 300e-3]},
                      'C_par': {'initial_value': 3e-3, 'bounds': [2e-3, 10e-3]},
                      'D_par': {'initial_value': 3e-3, 'bounds': [2e-3, 10e-3]}}
        """
        parameters = {'A': {'initial_value': 16e-3, 'bounds': [16e-3, 16.1e-3]},
                      'B': {'initial_value': 20e-3, 'bounds': [20e-3, 20e-3]},
                      'delta': {'initial_value': 2e-3, 'bounds': [1.9e-3, 2.1e-3]},
                      'Dind1': {'initial_value': 180e-3, 'bounds': [180e-3, 180e-3]},
                      'C_par': {'initial_value': 3e-3, 'bounds': [3e-3, 3e-3]},
                      'D_par': {'initial_value': 3e-3, 'bounds': [3e-3, 3e-3]}}

        # cilove funkce a jejich jmena
        costs = ['F']
        # kde je model?
        working_dir = os.getcwd() + os.sep + "hes_ivan"
        # os.remove(working_dir + "data.sqlite")

        super().__init__(name, parameters, costs, working_dir=working_dir)

        # nemenit - pousti se comsol na condoru
        self.executor = CondorJobExecutor(self,
                                          command="run.sh",
                                          model_file="HES_titan_opt2_artap.mph",
                                          output_file="outfile.txt",
                                          supplementary_files=["run.sh"])

    def evaluate(self, x):
        result = self.executor.eval(x)

        # DEFINICE CILOVE FUNKCE
        of = abs(result[1] - result[0])
        # VYSTUP NA OBR - LZE MENIT
        print(x, result, of)

        return [of]

    def parse_results(self, content):
        lines = content.split("\n")
        line_with_results1 = lines[6].split()  # 5th line contains result
        line_with_results2 = lines[7].split()  # 5th line contains result
        print(line_with_results1)
        min = float(line_with_results1[2])
        max = float(line_with_results2[2])

        return [min, max]


if __name__ == '__main__':
    problem = OptProblem("Opt")

    algorithm = NLopt(problem)
    algorithm.options['algorithm'] = LN_BOBYQA

    # algorithm = BayesOptSerial(problem)
    algorithm.options['verbose_level'] = 1
    algorithm.options['n_iterations'] = 2
    algorithm.run()

    results = Results(problem)

    results = GraphicalResults(problem)
    optimum = results.find_minimum(name='F')
    results.plot_scatter('F_1', 'F_2', filename="/tmp/scatter.pdf")
    # results.plot_scatter('x_1', 'x_2')
    # results.plot_individuals('F_1')
