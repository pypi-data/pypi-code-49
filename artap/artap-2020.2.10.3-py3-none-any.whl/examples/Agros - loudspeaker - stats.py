#!/usr/bin/python3

from artap.problem import Problem
from artap.results import Results, GraphicalResults
from artap.datastore import FileDataStore

from shutil import copyfile

#database_name = "tmp/loudspeaker_multi_tmp.db"
#copyfile("tmp/loudspeaker_multi.db", database_name)
#database_name = "tmp/loudspeaker_single_tmp.db"
#copyfile("tmp/loudspeaker_single.db", database_name)

problem = Problem()
problem.data_store = FileDataStore(problem, database_name=database_name, mode="read")
results = Results(problem)

ind = 0
for population in problem.data_store.populations:
    ind = ind + len(population.individuals)

print("individuals = {}".format(ind))
print(results.parameters())
print(results.costs())

results = GraphicalResults(problem)
results.plot_scatter('F1', 'F2', filename="/tmp/scatter.pdf", population_number=None)
#results.plot_individuals('F', filename="/tmp/individuals.pdf")

"""
# CSV
import csv
with open('tmp/results.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for population in problem.data_store.populations:
        for individual in population.individuals:
            spamwriter.writerow([individual.vector[0], individual.vector[1], individual.vector[2], individual.vector[3],
                                 individual.costs[0]])
"""